On this quickstart guide, we'll deploy the application in docker

## PREREQUESITES
- [Docker](https://docs.docker.com/get-docker/)
- PyInstaller to generate executables for the extractor tool
- The complete set of prerequesites and dependencies can be found in the `Dockerfile`. We __advise against__ running the tool without docker.

  1. Docker
  2. python 3.7+ and the python requirements
  3. PyInstaller


1. Run the `install_docker_image.sh`, it will build the docker image and create the configuration files
2. [Create an API key on your Deep Security](https://automation.deepsecurity.trendmicro.com/article/dsaas/create-and-manage-api-keys?platform=dsaas) and [assign it to a role](https://help.deepsecurity.trendmicro.com/user-roles.html?Highlight=roles) the following permissions:
    * VIEW Access to COMPUTERS
    * VIEW Access to POLICIES
    * VIEW Access to MALWARE SCAN CONFIGURATIONS
    * VIEW Access to FIREWALL STATEFULL CONFIGURATIONS
    * VIEW Access to TASKS
2. Edit the `/etc/DSHC/api_config.yml` file, place your DSM hostname and a API Access Key. Leave the "api_version" as is

EXAMPLE
```                                                          
  host: https://app.deepsecurity.trendmicro.com/api                        
  api-secret-key: myscretkey
  api-version: 'v1' #Example 'v1'       
```
3. Run the `dshc` alias to run the container. Follow the on-screen prompts as they appear to fill in the report details.
4. When the generation is done the report can be found in `/etc/DSHC/reports` as a .zip file. The zip will contain 
    * The Executive report
    * The technical report (the password will be inside the executive report)
    * A copy of the BPG
