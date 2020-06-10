import os
import shutil
from .yaml_parser import YAMLParser
from jinja2 import Template, Environment, FileSystemLoader
from zipfile import ZipFile
#from subprocess import Popen
import subprocess
import operator #sorted
import re # Remove words
import datetime
import json
import lzma
from .crypto_spa_report import pack_data
import inflect
import lib.constants as constants

class ReportGenerator():
	"""
	Generic Report Generator. Only provides base functionality for specialized
	generators.
	"""
	def __init__(self):
		"""
		report_data: Dict containing all required data to populate the report,
			 regardless of report template.
		report_options: Other report options unrelated to the actual data
			 such as color pallettes, etc.
		"""
		self.tech_report_path = '.report_templates/tech_report/TechnicalReport/'
		self.tech_report_build = self.tech_report_path + 'dist/'

		self.jinja_env = Environment(
			loader = FileSystemLoader(os.path.abspath(constants.HTML_BASE_PATH))
		)

		self.REPORT_TEMP_FILEPATH = "report.html.temp"
		self.REPORT_DETAILS_FILEPATH = "./config/report_details.yml"
		self.REPORT_RENDERED_FILEPATH = "./report_pdfs/"
		self.OS_RELEASES_FILEPATH = './config/os_releases.yml'
		# #Filepath for the report template - to be changed according to the child class
		# self.REPORT_TEMPLATE_FILEPATH='BPG_Report_Template.html'
		self.REPORT_TEMPLATE_FILEPATH = "report_base.html.j2"


		self.report_data={}
		self.report_options={}

		"""
		Loads all other details needed such as customer's name, etc
		These values are to be placed on the report_options dict when generating
		the report.
		"""
		self.yaml_parser = YAMLParser()
		report_details = self.yaml_parser.load_file(self.REPORT_DETAILS_FILEPATH)
				
		#Sanity check against empty file
		if report_details:
			p = inflect.engine()
			gen_day = p.ordinal(datetime.datetime.now().day)

			expire_date = datetime.datetime.now() + datetime.timedelta(days=45)
			exp_day = p.ordinal(expire_date.day)
			self.report_options.update({
				"include_customer_logo": self._find_customer_logo(report_details.setdefault("customer_name", "")),
				"partner_name" : report_details.setdefault("partner_name",""),
				"partner_contacts": report_details.setdefault("partner_contacts",{}),
				"trend_contacts" : report_details.setdefault("trend_contacts",{}),
				"generation_date" : datetime.datetime.now(),
				"generation_month": datetime.datetime.now().strftime("%B"),
				"generation_day": gen_day,
				"expiration_date" : expire_date,
				"expiration_day" : exp_day,	
				"expiration_month" : expire_date.strftime("%B"),				
			})

		else:
			print("WARNING: No {} found! exiting...".format(self.REPORT_DETAILS_FILEPATH))
			exit(1)

	def _process_data(self):
		"""
		Processes all the raw data collected from the *checker modules into human-readable
		HTML-required information.
		"""
		pass

	def _dict_count_to_dict_percentage(self,dictionary, max_count):
		"""
		Converts a dict of counts to a dict of percentages
		"""
		return {k: round( 100 * ( v/max_count ) , 1 )  for k,v in dictionary.items()}

	def _dict_from_keys_and_list(self,orig_dict,list):
		"""
		Creates a dict with the keys of an original dict with values indexed in a
		list.

		Args:
			orig_dict: The source of the keys
			list: List with the new values

		Returns:
			new_dict Dictionary of original keys and values

		Raises:
			IndexError if list length < keys
		"""
		if(len(orig_dict.keys()) > len(list)):
			raise IndexError("Error: More keys than values")

		new_dict={}
		for index, key in enumerate(orig_dict.keys()):
			new_dict[key] = list[index]
		return new_dict


	def _truncate_dict_by_sort(self,dictionary, sort_field_index, max_items):
		"""
		Sorts a dictionary by a sort_field_index, selecting the max_items-1 largest
		items and mapping all other items into a "others" field.

		Args:
			dictionary		The dictionary to truncate
			sort_field_index	Field to be used for sorting
			max_items		Number of maximum items in the final dict
		"""
		if len(dictionary.items()) >= max_items:
			#list of tuples ('key',{count:0,percentage:0}) ordered by sort_field_index
			#               i[0]   i[1]['count']
			sorted_dict_tuple = sorted(dictionary.items(), key=lambda i: i[1][sort_field_index])
			others = {'count':0,'percentage':0}
			for k in range(0, len(sorted_dict_tuple) - max_items + 1 ):
				others['count'] += sorted_dict_tuple[k][1]['count']
				others['percentage'] += sorted_dict_tuple[k][1]['percentage']
				del dictionary[sorted_dict_tuple[k][0]] # del dict(windows)
			# Only round
			dictionary["Others"] = others


	def _beautify_string(self,str):
		"""
		Splits a string at '_' and capitalizes each split part
		"""
		return " ".join(s.capitalize() for s in str.split("_"))
	

	def _find_customer_logo(self, customer_name):
		"""
		Returns true if the a .png file with the customer's name is found
		"""
		path = "report_templates/HTML/img/customer_logos/"+customer_name+".png"
		if os.path.isfile(path):
			return True
		else:
			return False


	def load_customer_info_from_data(self):
		try:
			self.report_options.update({
				"customer_name" : self.report_data["customer_info"]["customer_name"],
				"customer_contacts" : self.report_data["customer_info"]["customer_contacts"],
			})
		except:
			self.yaml_parser = YAMLParser()
			report_details = self.yaml_parser.load_file(self.REPORT_DETAILS_FILEPATH)
			self.report_options.update({
				"customer_name": report_details.setdefault("customer_name", ""),
				"customer_contacts": report_details.setdefault("customer_contacts", {}),
			})


		#Leaves only alphanumerical characters in the name
		self.report_name = re.sub(r'\W+', '',self.report_options['customer_name']) + "-{0:%Y-%m-%d-%f}".format(self.report_options["generation_date"])
		
	def generate_exec_report(self):
		"""
		Function that generates the pdf report

		Args:
			-
		Retruns:
			-
		Raises:
			-
	 	"""
		#loop = None
		#while loop != 'n':

		#pega info do datapack
		self.load_customer_info_from_data()

		report = self.jinja_env.get_template(self.REPORT_TEMPLATE_FILEPATH)
		try:
			rendered_report = report.render(report_data=self.report_data, report_options=self.report_options)#, SUMMARY_TEMPLATE_FILEPATH=self.SUMMARY_TEMPLATE_FILEPATH)
		except Exception as e:
			print('Error on gen jinja => {}'.format(e))
			return

		report_file = open(constants.HTML_BASE_PATH + self.REPORT_TEMP_FILEPATH,"w")
		report_file.write(rendered_report)
		report_file.close()
		p = subprocess.Popen(['php','TO_PDF.php', self.REPORT_TEMP_FILEPATH],cwd=constants.HTML_BASE_PATH, stdout=subprocess.DEVNULL)
		p.communicate()
		os.remove(constants.HTML_BASE_PATH + self.REPORT_TEMP_FILEPATH)
		#shutil.move(constants.HTML_BASE_PATH + "report.pdf", self.REPORT_RENDERED_FILEPATH + self.report_name+".pdf")

	def report_data_to_json(self, report_data):
		with open("./report_pdfs/tech_report_data.json",'w') as raw_json:
			for key in report_data.keys():
				report_data[key] = recursive_generic_to_dict_values(report_data[key])
			raw_json.write(json.dumps(report_data,indent=4,sort_keys=True))


	def generate_tech_report(self, computers, policies, results, valid_modules, aes_key = None):

		"""
		Generate a json to be used tech report, with array of dictionaries 

		Args:
			computers: List of all computers.
			policies: List of all policies
			results: bundle of bundles
		
		Return as:
			{
				"computers": [computer_results],
				"policies" :  [policy_results]
			}
		"""
		self.load_customer_info_from_data()
		package = {}
		package['customer'] = self.report_options['customer_name']
		package['computers'] = []
		package['policies'] = []
		package['modules'] = {self._beautify_string(long_name): short_name for short_name, long_name in valid_modules.items()}
		mapped_policy = results['mapped_policies']

		with open("{}src/assets/tech_report_data.json".format(self.tech_report_path), "w") as raw_json:
			for computer in computers:
					if computer.id not in results['computer_results']: continue
					result = results['computer_results'][computer.id]
					group_name = results['computer_groups'].get(computer.group_id, None)
					policy_name = results['policies_results'].get(computer.policy_id, None)

					if group_name is not None: group_name = group_name['name']
					if policy_name is not None: policy_name = policy_name['name']

					package['computers'].append({
						'hostname'		 		 :	computer.host_name,
						'agent_version'  		 :  computer.agent_version,
						'id'					 :	computer.id,
						'policy_id'				 :  computer.policy_id,
						'policy_name'			 :  policy_name,
						'results'		 	     : 	result['total'].conformity_rate,
						'group_name'			 :  group_name,
						'plataform'				 :  computer.platform,
						'modules'				 :  {valid_module:result[valid_module].to_dict() for valid_module in valid_modules.values()}
					})

			for policy_id, mapped_policy in mapped_policy.items():
					result = results['policies_results'][policy_id]
					
					package['policies'].append({
						'name'				: mapped_policy['name'],
						'id'  				: policy_id,
						'modules'			: {valid_module:result[valid_module].to_dict() for valid_module in valid_modules.values()},
						'results'			: result['total'].conformity_rate,
						'computers_using'	: mapped_policy['computers_using']
 					})
			
			json_raw = json.dumps(package)
			json_compress = lzma.compress(json_raw.encode(), format=lzma.FORMAT_ALONE)
			json_raw = None
			
			raw_json.write(pack_data(json_compress,aes_key))
			raw_json.flush() # Write buffered file in disk

			p = subprocess.Popen(['npm','run', 'build'],cwd=self.tech_report_path,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
			p.communicate()
			#shutil.move(self.tech_report_build, "./report_pdfs/tech_report")
			# raw_json.write(json.dumps(package, indent=4))

	def pack_report(self,output_path = ''):
		"""
		Packs the Executive and Tech reports into a zip file

		Args:
			output_path: Filepath for the zip-file.
		"""

		if os.environ.get('ENV') == 'DOCKER' and not os.environ.get('AWS', False):
			if len(output_path.split('/')) > 1:
				print("Invalid path format for docker enviroment {}, need only filename\naborting...".format(output_path))
				exit(1)

			if output_path != '':
				output_path = os.path.join(self.REPORT_RENDERED_FILEPATH, output_path)
			else:
				output_path = os.path.join(self.REPORT_RENDERED_FILEPATH, self.report_name) + ".zip"
		
		file_paths = []
		for root, directories, files in os.walk(self.tech_report_build):
			for filename in files:
				filepath = os.path.join(root, filename)
				file_paths.append(filepath)


		extension = output_path[len(output_path)-3:]
		if 'zip' not in extension:
			output_path = os.path.join(os.path.abspath(output_path), self.report_name) + ".zip"
			print("No zip file name provided, saving as {}".format(output_path))
		
		with ZipFile(output_path, 'w') as zip_file:
			for filepath in file_paths: 
				zip_file.write(filepath, '/'.join(filepath.split('/')[5:]))
			
			zip_file.write(constants.HTML_BASE_PATH + "report.pdf", "Executive Report.pdf")
			zip_file.write("BPG_guide.pdf", "Deep Security Best Practice Guide.pdf")

		return output_path

	def generate_analytics(self):
	# "total-machines" : $input.json('$.total-machines'),
    # "managed-machines" : $input.json('$.managed-machines'),
    # "checked-modules" : $input.json('$.checked-modules'),
    # "total-compliance" : $input.json('$.total-compliance'),
    # "detected-plataforms" : $input.json('$.detected-plataforms'),
    # "modules-compliance" : $input.json('$.modules-compliance'),
    # "conformity-distribution" : $input.json('$.conformity-distribution'),
    # "agent-versions" : $input.json('$.agent-versions'),
    # "issue-count" : $input.json('$.issue-count'),
    # "core-oses" : $input.json('$.core-oses'),
    # "compliance-type" : $input.json('$.compliance-type'),
    # "unique-anonymous-id" : $input.json('$.unique-anonymous-id'),

		if "Others" in self.report_data["agent_operating_system"]:
			del self.report_data["agent_operating_system"]["Others"]

		analytics = {
			"total-machines"	 	 :  self.report_data["num_computers"],
			"managed-machines"	 	 : 	self.report_data["num_managed_computers"],
			"checked-modules"    	 :	self.report_data["modules_to_check"],
			"total-compliance"   	 :	self.report_data["computers_average_conformity"],
			"detected-plataforms"	 :	{scenario_name: scenario_obj.status_count for scenario_name, scenario_obj in self.report_data["agent_deployment_scenarios"].items()},
            "modules-compliance" 	 :  {k: v.conformity_rate for k, v in self.report_data["module_results"].items()},
			"core-oses"			 	 :  {so_name: so_info["count"] for so_name, so_info in self.report_data["all_operating_system"].items()},
			"agent-versions"	 	 :  [x for x,i in self.report_data["agent_release"]],
			"issue-count"		 	 :  {criticity_level: len(criticity_info["issues"]) for criticity_level, criticity_info in self.report_options['env_issues'].items()},
			"conformity-distribution":  {level: round(level_info['percent'],2) for level, level_info in self.report_options["agent_average_conformity_slices"].items()},
			"compliance-type"		 : self.report_options["conformity_standard"]
		}


		return analytics

				
def recursive_generic_to_dict_values(obj):
	"""
	Perform a recursive depth-walk in a given object, 
	returning raw primitives or dictonary representations of objects

	To be used in the values of a parent dictonary to them to 
	JSON Serializable objects
	"""
	if isinstance(obj,(list,tuple)):
		json_objects = []
		for item in list(obj):
			json_objects.append(recursive_generic_to_dict_values(item))
		return json_objects
	elif isinstance(obj,dict):
		for k,v in obj.items():
			obj[k] = recursive_generic_to_dict_values(v)
		return obj
	#PRIMITIVE DATA TYPES
	elif isinstance(obj, (int,float,str)):
		return obj
	else:
		try:
			return obj.to_dict()
		except:
			return obj.__dict__	

class BPGGenerator(ReportGenerator):

	def __init__(self, report_data, add_report_options):
		"""
		report_data - Dictionary combining the results from of the checkers
		add_report_options - Additional report options sent from elsewhere. The keys must be the same as the ones used in Jinja
		"""
		super(BPGGenerator, self).__init__()
		self.report_data = report_data
		
		#This is ugly and not optimal, but it was the quickest way to put the pretty module names
		#May god have mercy on our souls
		self.report_data["dict_modules_not_to_check"] = \
		 {k:self._beautify_string(v) for k,v in self.report_data["dict_modules_not_to_check"].items() }
		self.report_data["dict_modules_to_check"] = \
		 {k:self._beautify_string(v) for k,v in self.report_data["dict_modules_to_check"].items() }
		
		self.report_options.update({
			"pretty_module_names": { k:self._beautify_string(k) for k in self.report_data["module_deployment_count"].keys() },
			"module_descriptions": self.yaml_parser.load_file(constants.MODULE_DESCRIPTIONS_FILEPATH),
			"agent_average_conformity_slices": {
				"High Conformity":{
					"range":(75,100),
					"count": 0,
					"percent":0,
					"css_style": "conformity_high"
				},
				"Medium Conformity":{
					"range":(50,74),
					"count": 0,
					"percent":0,
					"css_style": "conformity_medium"
				},
				"Low Conformity":{
					"range":(25,49),
					"count": 0,
					"percent":0,
					"css_style":"conformity_low"
				},
				"Caution":{
					"range":(0,24),
					"count": 0,
					"percent":0,
					"css_style": "conformity_caution"
				},
			}
		})
		self.report_options.update(add_report_options)
		self.PIE_GRAPH_MAX_SLICES = 8
		self._process_data()
		# self.report_data_to_json({
		# 	"computers":self.report_data["computers"],
		# 	"computer_results":self.report_data["computer_results"],
		# 	"policies":self.report_data["policies"],
		# 	"policy_results":self.report_data["policies_results"],
		# 	})
		

	def _agent_release_ordered_list(self,agent_release_dict):
		"""
		Order agent release versions, most updated first
		agent_release_dict keys are agent versions, e.g. '11.0.0'

		Return:
			List of tuples (agent_version, {'count':x,'percentage':y} )
		"""

		agents_versions = sorted(agent_release_dict.items(), key = lambda i: float('.'.join(i[0].split('.')[:2])),reverse=True)

		# FIX DSVA
		for i, info in enumerate(agents_versions):
			new_name = ""
			if info[0][0] == '0': # DSVA
				new_name = "Agentless"
			else:
				new_name = '.'.join(info[0].split('.')[:-1])

			agents_versions[i] = (new_name, agents_versions[i][1])
		
		return agents_versions

	def _beautify_os_names(self,os_count_and_percentage):
		"""
		Beautify OS names, removing verbosity (e.g. 'Microsoft', '(64-bit)', etc.)
		Args: 
			Dictionary with count and perentage of OSes
		"""
		regex_rule = 'Microsoft*|\\(.*'
		
		for so_name in list(os_count_and_percentage.keys()):
			so_regex = re.sub('^\s+|\s+$','',re.sub(regex_rule,'',so_name))
			os_count_and_percentage.setdefault(so_regex, {'count':0,'percentage':0})
			os_count_and_percentage[so_regex]['count'] += os_count_and_percentage[so_name]['count']
			os_count_and_percentage[so_regex]['percentage'] += os_count_and_percentage[so_name]['percentage']
			os_count_and_percentage.pop(so_name)

	def _add_os_dates(self,os_count_and_percentage):
		"""
		Adds release and End of Life dates to an OS in the dict
		Args: 
			Dictionary with count and perentage of OSes		
		"""
		os_releases = self.yaml_parser.load_file(self.OS_RELEASES_FILEPATH)
		for os in list(os_count_and_percentage.keys()):
			os_count_and_percentage[os]['release'] = os_releases.get(os,{'release_date': 'N/A', 'end_date': 'N/A'})

	def _calculate_conformity_slice_count_and_percentage(self,computer_results,conformity_slices,num_managed_computers):
		"""
		Adds the count and percentage of computers with a total score in the 
		range of a conformity 'slice', as defined in report_options

		Args:
			computer_results: Dictonary with all modules' and a 'total' CheckResult
			conformity_slices: Dictionary of conformity slices as defined in report_options
			num_managed_comptuers: Number of all computers with agents in the environment
		"""
		#The total (sum of results for all modules in a computer) of all computers
		computer_results_totals = [ (lambda x: x['total']) (x) for x in computer_results.values()]
		
		for s in conformity_slices.values():			
			slice_filter = lambda x: s["range"][0] <= x.conformity_rate <= s["range"][1]
			#Number of computers within that range of score
			s["count"] = len( list( filter( slice_filter, computer_results_totals ) ) )
			s["percent"] = 100 * (s["count"] / num_managed_computers)

	#OVERRIDE from parent
	def _process_data(self):

		# self._truncate_dict_by_sort(self.report_data["agent_release"],'count',self.PIE_GRAPH_MAX_SLICES)
		self.report_data['agent_release'] = self._agent_release_ordered_list(self.report_data['agent_release'])




		#Operating Systems
		self._beautify_os_names(self.report_data["agent_operating_system"])
		
		self.report_data["all_operating_system"] = self.report_data["agent_operating_system"]

		self._truncate_dict_by_sort(self.report_data["agent_operating_system"],'count',self.PIE_GRAPH_MAX_SLICES)
		self._add_os_dates(self.report_data["agent_operating_system"])

		#Agent Average Conformity
		self._calculate_conformity_slice_count_and_percentage(
			self.report_data["computer_results"],
			self.report_options["agent_average_conformity_slices"],
			self.report_data["num_managed_computers"]
		)

		issues_sorted = sorted(self.report_data['issues'], key=lambda i: i.criticity_score, reverse=True)
		self.report_data['top_ten_issues'] = issues_sorted[:10]

		# COMBAK Anderson, plz improve the code below
		
		# List with severity description and color based on index. 
		# Using a item's weight we can access it's color and description
		severity_css = []
		severity_types = []
		severity_css += ["severity_enhancement"] * 2
		severity_css += ["severity_low"] * 2
		severity_css += ["severity_medium"] * 2
		severity_css += ["severity_critical"] * 2
		severity_css += ["severity_vulnerability"] * 2

		severity_types += ["Warning"] * 2
		severity_types += ["Low"] * 2
		severity_types += ["Medium"] * 2
		severity_types += ["High"] * 2
		severity_types += ["Critical"] * 2
		self.report_options['dist_issues'] = {}
		self.report_options['env_issues'] = {}


		# COMBAK: Just works
		for env_issue in issues_sorted[:20]:
			type_name = severity_types[env_issue.item_weight-1]
			css_name = severity_css[env_issue.item_weight-1]
			self.report_options['dist_issues'].setdefault(type_name, {
				"issues": [],
				"css_style": css_name
			})
			self.report_options['dist_issues'][type_name]['issues'].append(env_issue)

		for env_issue in issues_sorted:
			type_name = severity_types[env_issue.item_weight-1]
			self.report_options['env_issues'].setdefault(type_name, {
				"issues": [],
			})
			self.report_options['env_issues'][type_name]['issues'].append(env_issue)
		#


		for i,computer in enumerate(self.report_data['least_conforming_computers']):
			weight = computer[1]['total'].curr_score//10
			weight = (weight + (weight * 2)) % len(severity_css) # Jump to the opposite severity
			css_name = severity_css[weight]
			self.report_data['least_conforming_computers'][i][1]['css_name'] = css_name

		# Fully compliant modules count
		self.report_data['top_ten_worst_policies'] = [(id, re.escape(dict['name']).replace('_','\\_')) for id, dict in self.report_data['top_ten_worst_policies']]


	def get_report(self):
		return {"options": self.report_options, "data": self.report_data}