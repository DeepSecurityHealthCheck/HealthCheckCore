On this quickstart guide, we'll deploy the application in docker in your locla machine.

## PREREQUESITES
- [Docker](https://docs.docker.com/get-docker/)
  - The complete set of prerequesites and dependencies can be found in the `Dockerfile`. We __advise against__ running the tool without docker.
- Python 3.7+ and the python requirements
- PyInstaller to generate executables for the extractor tool

1. Run `pip3 install -r requirements.txt` to install all python dependencies
2. Run the `install_docker_image.sh`, it will build the docker image and create the configuration files
3. Run `dshc -g` to generate a key pair. Follow the on-screen prompt and **Securely store** the password. The keys will be stored under `/etc/DSHC/keys`
  1. Run `mv /etc/DSHC/keys/PUBLIC_KEY.pem /keys/`. If the `keys/` directory doesn't exist, create it. The extractor will use the public key.
4. [Create an API key on your Deep Security](https://automation.deepsecurity.trendmicro.com/article/dsaas/create-and-manage-api-keys?platform=dsaas) and [assign it to a role](https://help.deepsecurity.trendmicro.com/user-roles.html?Highlight=roles) the following permissions:
    * VIEW Access to COMPUTERS
    * VIEW Access to POLICIES
    * VIEW Access to MALWARE SCAN CONFIGURATIONS
    * VIEW Access to FIREWALL STATEFULL CONFIGURATIONS
    * VIEW Access to TASKS
5. Edit the `config/api_config.yml` file, place your DSM hostname and a API Access Key. Leave the "api_version" as is
EXAMPLE
```                                                          
  host: https://app.deepsecurity.trendmicro.com/api                        
  api-secret-key: myscretkey
  api-version: 'v1' #Example 'v1'       
```
6. Run `python3 extractor.py --notsend` and follow the on-screen prompts. If extraction is sucessful a data_pack will be created in this directory.

7. Run `dshc -d -r DATA_PACK_NAME.dat` alias to run the container. Follow the on-screen prompts as they appear.
4. When the generation is done the report can be found in `/etc/DSHC/reports` as a .zip file. The zip will contain 
    * The Executive report
    * The technical report (the password will be inside the executive report)
    * A copy of the BPG