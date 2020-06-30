import sys
import yaml
import os
from prompt_toolkit import prompt


DEFAULT_YAML ='''
conformity_standard: "Deep Security Best Practices Guide"
partner_name: 'Partner'
partner_contacts:
    "Equipe Defalt":
        title: 'Equipe Técnica Default'
        email: ''
        phone: ''
trend_contacts:
    'Jane Smith':
        title: 'Sales Engineer'
        email: 'jsmith@trend com'
        phone: '333-222-987'
'''.encode("UTF-8")


def prettify_string(s):
    return "".join(s.replace("_"," ").capitalize())


def dive_into(d, recur=False):
    new_dict = {}
    for key, value in d.items():
        if type(value) == dict:
            ctrl = ""
            new_dict[key] = {}
            while ctrl not in ['n', 'no', 'NO', 'N']:
                # if recur:
                new_key = prompt("{}\n Name: ".format(prettify_string(key)))
                if new_key == "":
                    break

                base_key = list(value.keys())[0]
                new_dict[key][new_key] = dive_into(value[base_key], recur=True)
                if recur:
                    break

                ctrl = prompt("New entry? in {} [y/n]".format(key))

            continue

        new_value = prompt("{} [Default:{}]: ".format(key, value)) or value
        new_dict[key] = new_value

    return new_dict


if __name__ == '__main__':
    try:
        report_details = yaml.safe_load(DEFAULT_YAML)
    except Exception as e:
        print("Error on trying read yaml file {}".format("d"))
        print(e)
        sys.exit(1)

    # Ok, enough checks

    new_cfg = dive_into(report_details)
    cfg_folder = "./config/report_details.yml"

    with open(cfg_folder, "w") as cfg:
        cfg.write(yaml.dump(new_cfg))

    print("New config saved on {}".format(cfg_folder))
