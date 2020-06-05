import os

"""
Brief:
    Script for generate missing config file to be filled
"""


BASIC_CONFIG = """host: https://<Your DSM Hostname or IP>:<DSM Port>/api #Your DSM hostname
api-secret-key: #Your API KEY
api-version: 'v1' #Default 'v1'
"""

CONFIG_PATH = "config/api_config.yml"

def gen_config():

    """
    Create a yaml file to hold the basic config for connection on the API
    """

    cfg_file = open(CONFIG_PATH, "w")
    cfg_file.write(BASIC_CONFIG)
    cfg_file.close()
    pass

if __name__ == '__main__':
    print("(Re)Creating API Config file !")
    gen_config()
    exit(0)

    #print("File already exists!")
