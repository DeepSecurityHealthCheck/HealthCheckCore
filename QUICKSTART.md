On this quickstart guide, we'll deploy the application in docker

# PREREQUESITES
- Docker 
- (For the complete list, check the Readme and the dockerfile)

1. Run the `install_docker_image.sh`, it will build the docker image and create the configuration files
2. Edit the `/etc/DSHC/api_config.yml` file, place your DSM hostname and a API Access Key with VIEW-ONLY access to Computers, Policies, Scheduled Tasks, Anti-Malware Configurations and Stateful Configurations
3. Run the `dshc` alias to run a container.
4. The reports can be found in `/etc/DSHC/reports`
