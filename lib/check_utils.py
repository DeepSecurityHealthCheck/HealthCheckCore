from collections import namedtuple
from enum import Enum
import operator

def list_len_gt(arg_list: list, expected_len: int):
    #Assuming Empty list if None
    return len(arg_list) > expected_len if arg_list is not None else False

def list_len_ngt(arg_list: list, expected_len: int):
    return not list_len_gt(arg_list,expected_len)  

def contains_list(arg_list, base_list):
    if arg_list is None:
        return False
    for item in arg_list:
        if item not in base_list:
            return False
    return True

def not_contains_list(arg_list, base_list):
    if arg_list is None:
        return False
    for item in arg_list:
        if item in base_list:
            return False
    return True
class Operator():

    ops = {
        "LESS_THAN": operator.lt,
        "LESS_THAN_OR_EQUAL": operator.le,
        "EQUAL": operator.eq,
        "GREATER_THAN_OR_EQUAL": operator.ge,
        "GREATER_THAN": operator.gt,
        "NOT_EQUAL": operator.ne,
        "CONTAINS": contains_list,
        "NOT_CONTAINS": not_contains_list,
        "LENGTH_GREATER_THAN": list_len_gt,
        "LENGTH_NOT_GREATER_THAN": list_len_ngt
    }


class CheckItem(object):
    """Individual Item for a Checklist.

    Attributes:
        attr_path: Path to the attribute to check, nested attributes separated by '.'
        operator: Type of operation to use for check as described in the Operator enum
        operand: Value to compare to
        item_weight: the numerical weight this item has on the checklist score computation
        description: A dict storing the verbose description of the checklist, e.g.
            description:
              module: "stateful_configuration"
              failure_item: "Deny fragmented packets"
              text: "Fragmented packets should not be denied"
    """

    def __init__(self, attr_path, operator, operand, item_weight, description=None):
        super(CheckItem, self).__init__()
        self.attr_path = attr_path
        self.operator = operator
        self.operand = operand
        self.item_weight = max ( min(10,item_weight), 0 ) #clamp
        self.description = description
        self.failed_times = 0
        self.criticity_score = self.item_weight
        self.description["failure_item"] += " (Expected: {} {}) ".format(str(self.operator).replace("_"," ").lower(),str(self.operand))
        # Used to calculate criticity_score, values can be adjusted
        self.coeficent = (1.8*(self.item_weight/10))**2
        #print("Construi", self.attr_path, self.operator, self.operand, str(self.item_weight))
    def __repr__(self):
        #return("\n\t"+str(self.attr_path) + " " + str(self.operator) + " " + str(self.operand) + " " + str(self.item_weight) + "\t" + self.description["failure_item"])
        return( "{} - {}\t[Weight: {}/10]".format(self.description["module"],self.description["failure_item"],self.item_weight) )
    
    def to_dict(self):
        return self.__dict__

    def recalc_criticity(self):
        self.failed_times += 1
        #self.criticity_score = self.coeficent*self.failed_times #(0.5+(self.failed_times/10))*self.item_weight #(self.item_weight + self.failed_times) ** 2


class CheckList(object):
    """
    List of CheckItems including a title and a general description of the list's purposes
    """
    def __init__(self,title="",items=[],description=""):
        self.title = title
        self.items = items
        self.description = description

class CheckResult(object):
    """ Used as return for run_checklist

    Atributes:
        conformity_rate: % based on (curr_score/max_score)
        curr_score: sum of the weights of CheckItems that passed the check
        max_score: sum of the weights of all CheckItems
        failed_items: List of all CheckItems that failed the check
    """
    def __init__(self, curr_score: int, max_score: int, failed_items: list):
        #super(CheckResult, self).__init__()
        self.curr_score = curr_score
        self.max_score = max_score
        self.failed_items = failed_items
        try:
            self.conformity_rate = round(100 * (self.curr_score/self.max_score), 0)
        except Exception as e:
            self.conformity_rate = 0

    def to_dict(self):
        return{
            "curr_score": self.curr_score,
            "max_score":self.max_score,
            "failed_items": list(f.to_dict() for f in self.failed_items),
            "conformity_rate":self.conformity_rate
        }

    def __repr__(self):
        return ("Score {}/{}\t[{} % Conformity]").format(str(self.curr_score), str(self.max_score), str(self.conformity_rate))


    def __iadd__(self, other_result):
        if type(other_result) != CheckResult:
            raise TypeError
        
        self.curr_score += other_result.curr_score
        self.max_score += other_result.max_score
        self.failed_items += other_result.failed_items
        self.failed_items = list(set(self.failed_items))
        try:
            self.conformity_rate = round(100 * (self.curr_score/self.max_score), 0)
        except Exception as e:
            self.conformity_rate = 0
        return self


    def expand(self):
        return self.failed_items

def run_checklist(obj,check_list, return_failures=True, logger=None):
    """ Runs checks of a list of CheckItem on a single object

    Args:
        obj: Object to be compared with the checklist.
        param check_list (list): Checklist of the object's attributes and expected values.
        return_failures (bool): return or not the list of failed items.

    Returns:
        CheckResult object
    """
    curr_score = 0
    max_score = 0
    failures=[]
    for item in check_list:
        """Allows nested attribute checks"""
        attribute_path = item.attr_path.split(".")

        attribute_path_len = len(attribute_path)
        attr_actual_value = None

        """Attribute in-depth search for nested attributes"""
        if  attribute_path_len > 1:
            attr_actual_value = obj
            for a in attribute_path:
                attr_actual_value = getattr(attr_actual_value,a)
        else:
            attr_actual_value = getattr(obj, item.attr_path)

        operation_result=None

        """Operator Checking"""

        if item.operator not in Operator.ops.keys():
            raise("run_checklist Exception - Bad Operator")

        if logger:
            if type(item.operand) != type(attr_actual_value):
                logger.debug("{}\tgot: {}({})\t expected: {} {}({})"
                .format(item.attr_path, attr_actual_value, type(attr_actual_value), item.operator, item.operand, type(item.operand)))

        operation_result = Operator.ops[item.operator](attr_actual_value, item.operand)
        """Operator Result"""
        if operation_result:
            curr_score += item.item_weight
            max_score += item.item_weight

        else:
            item.recalc_criticity()
            failures.append(item)
            max_score += item.item_weight


    """Return failed items"""
    if return_failures:
        return CheckResult(curr_score, max_score, failures)
    else:
        return CheckResult(curr_score, max_score,[])
