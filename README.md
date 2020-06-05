# DEEP SECURITY HEALTH CHECK

Automated Deep Security Health Check Verification



## QUICKSTART
1. Run the `install_docker_image.sh`, it will build the docker image and create the configuration files
2. Edit the `/etc/DSHC/api_config.yml` file, place your DSM hostname and a API Access Key with VIEW-ONLY access to Computers, Policies, Scheduled Tasks, Anti-Malware Configurations and Stateful Configurations
3. Run the `dshc` alias to run a container.
4. The reports can be found in `/etc/DSHC/reports`

## PREREQUESITES
- Docker
- PyInstaller to generate executables for the extractor tool
- The complete set of prerequesites and dependencies can be found in the `Dockerfile`. We __advise against__ running the tool without docker.

  1. python 3.7+ and the python requirements
  2. php7.0-cli 
  3. php7.0-xml 
  4. php-font-lib 
  5. php7.0-mbstring
  6. php7.0-gd 
  7. composer
  8. PyInstaller


## DOCKER IMAGE INSTALLATION

### USE THE SCRIPT
- Run the `install_docker_image.sh` script. It will:
  - automatically __build a docker image, create configuration files and dirs at `/etc/DSHC/`
  - make a `dshc` alias to run a container and mount the correct directories


### DO IT MANUALLY
- Inside the directory `docker build -t dshc:latest .` (or any other tag)
- You will need to create or choose FOUR directories for the container's volumes:
  - one to store the assymetric keys.
  - one to store configuration files. 
    - Create a `api_config.yml` file on your chosen configuration directory (see the file's contents below in CONFIGURATION)
    - Copy/move __all others files__ included in the repository's own `config` directory
  - (optional) one to store data packs from the extractor tool
  - one to recieve the reports from the container

[Please follow the docker post-install guide to configure permissions.]( https://docs.docker.com/install/linux/linux-postinstall/ )

## CONFIGURATION
The configuration files for the program are placed in the tool's `config` directory.
- `api_config.yml` __Required__ to configure access to the DSM RESTful API. The following fields are expected
  - `host` The DSM API URL/IP Address. Include `https://` and the port (if non-standard)
  - `api-secret-key` The API Read-only access key
  - `api-version` Version in use by the API

EXAMPLE
```
api-configuration:                                                                 
  host: https://10.0.0.1:4119/api                        
  api-secret-key: myscretkey
  api-version: 'v1' #Example 'v1'       
```
- `report_details.yml` To configure details used in non-critical parts of the report (__DETAILS PENDING__)


## USAGE
```
dshc [-h] [-l --licenses LICENSES [LICENSES ...]]
            [-m --modules MODULES [MODULES ...]] [--standard STANDARD] [-d --debug]
            [-s --stress] [-r --remote PACKAGE]

```

### OPTIONAL ARGUMENTS:

* ```-h, --help```
  * show the help message and exit
* ```--licenses LICENSES [LICENSES ...], -l LICENSES [LICENSES ...]```
  * Space separated list of modules (grouped by license) to be checked

* ```--modules MODULES [MODULES ...], -m MODULES [MODULES ...]```
  * Space separated list of modules to be checked

* ```--standard STANDARD, -c STANDARD```
  * Conformity Standard to be used

* ```--debug, -d```
  * Debug messages will be written in debug.log

* ```--stress STRESS, -s STRESS```
  * Stress test - Choose number (dummy) of computers to
      run test

* ```--remote REMOTE, -r PACKAGE_NAME```
  * See EXTRACTOR AND REMOTE MODE below 

#### VALID LICENSES INPUT
- `mp`  Malware Protection - Anti-Malware, Web Reputation
- `ss`  System Security - Integrity Monitoring, Log Inspection, Application Control)
- `ns`  Network Security - Firewall, Intrusion Prevention
- `all` All modules

#### VALID MODULES INPUT
- `am`  Anti-Malware
- `wr`  Web Reputation
- `im`  Integrity Monitoring
- `li`  Log Inspection
- `ac`  Application Control
- `fw`  Firewall
- `ip`  Intrusion Prevention

If no modules or licenses are explicitly declared, all modules will be checked by default

## EXAMPLES
* `dshc -l mp ss -m ip`
  * Checks all Malware Protection and System Security modules and Intrusion Prevention module
* `dshc -r my_pack.dat`
  * Loads the my_pack.dat placed in the /data_packs directory



### EXTRACTOR AND REMOTE MODE

Intended to be used in cases where a customer is not able or willing to open a direct network connection to the DSM's API, the Standalone `extractor.py` tool can be run by the customer from inside the network.

The `extractor.py`  accesses the API and generates an encrypted data package containing the Deep Security's environment information. The data packages can then be unencrypted and used through the `-r` or `--remote` mode of the main  `dshc` program.

#### KEY GENERATION AND USAGE

For the extractor to encrypt and for dshc to decrypt the data packages, __it is required__ a 8192-bit RSA public-private key pair. A pair of public and private keys can be generated using the `generate_keys.py`. 

For further protection the private key will be protected with a password that as prompted by the key generation script.

__DO NOT SHARE YOUR PRIVATE KEY__

#### BUILDING THE EXTRACTOR TOOL EXECUTABLE

The `build_extractor_zip` can be used to create a zip with an executable of the extractor tool and of it's required files 

Detailed Instructions for the `extractor` can be found in the `EXTRACTOR_README.md` file.

#### LOADING THE DATA PACKAGES IN THE MAIN PROGRAM

Using  loads a data package generated by the extractor, decrpyts it and run checks. 

If running the docker version, place the data package in the `data_packs` directory and pass the __name__ of the package. The corresponding private key is expected to be in the `keys` directory with the name `PRIVATE_key.pem`. You will be prompted to enter the key's password.

__WARNING:__ the extractor module is not secure against erroneous or maliciously constructed data. __Never__ unpack data received from an untrusted or unauthenticated source.


### IMPACT ON ON-PREMISE INFRASTRUCTURE
The data used by the program (or extractor standalone) is fetched in the Deep Security Database via the RESTful API. There is an __increase of resource usage__ (proportional to the amount of data being queried), mainly in the __Database__ but also on the __Manager__.
As such, __caution should be taken for On-Premise deployments__ to avoid possible impacts on a customer's business.

Although the impact should be minimal for most deployments, consider the following before proceeding:
* Is the Database used exclusively for Deep Security?
  * If not, what other services could be affected?
* How many Agents are in the environment?
* Is Deep Security undergoing updates?

##### EXPERIMENTAL RESULTS
A test extracting data for 995 Agents and a lesser number of configurations and policies during a "stress" (DS _Rules and Patterns_ Update) period on a on a RDS-T2 (2 Intel CPUs up to 3.0 GHz, 8GB RAM, running PostegreSQL 9.6), resulted in Increases the following:
* DATABASE
  * +1% of CPU
  * +2e-4 seconds of Read Latency
  * +4 Database Connections
* MANAGER
  * +3% of RAM
  * +1% of CPU

## UTILITIES
In the `utils` directory are general utilities
* `gen_config` Script generates an empty api config YAML file in the `config` directory.
* `profiler` Shell script is used to perform a bulk of Stress tests on the dshc script. The results are stored as `performance_profile` in the same directory.

## CODE DOCUMENTATION
Detailed documentation on the code, project architecture can be found on the `docs` directory. __This is a To-Do.__

## AUTHORS
Deep Security Health Check was originally Developed by

* Anderson Leite [@aandersonl](https://github.com/AandersonL)
* Angelo Rodem <Angelo_Rodem@trendmicro.com>
* João Guimarães <Joao_Guimaraes@trendmicro.com>


