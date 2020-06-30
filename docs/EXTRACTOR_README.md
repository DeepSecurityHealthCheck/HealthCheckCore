Trend Micro Incorporated                                  March 18, 2020

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Trend Micro Extractor Tool for Deep Security Health Check
Version 1.8

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TERMS AND CONDITIONS: This tool was developed by Trend Micro, Inc.
This tool has received limited testing and is for your internal
use only. THIS TOOL IS PROVIDED "AS IS" WITHOUT WARRANTIES OF ANY
KIND. TREND MICRO MAKES NO WARRANTY ABOUT THE OPERATION OR
PERFORMANCE OF THIS TOOL NOR DOES IT WARRANT THAT THIS TOOL IS
ERROR FREE. TO THE FULLEST EXTENT PERMITTED BY LAW, TREND MICRO
DISCLAIMS ALL IMPLIED AND STATUTORY WARRANTIES, INCLUDING BUT NOT
LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY,
NONINFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE. THIS TOOL
IS SUBJECT TO CHANGE AND MODIFICATION, INCLUDING, WITHOUT
LIMITATION, CHANGES AND MODIFICATIONS WITH RESPECT TO PERFORMANCE
AND FUNCTIONALITY ANY TIME AT THE SOLE DISCRETION OF TREND MICRO.

# STANDALONE EXTRACTOR TOOL FOR DEEP SECURITY HEALTH CHECK

## ABOUT THIS TOOL
In order to create a Health Check report for you, we will need to collect some data from your Deep Security deployment. This tool will:
* Extract the required data (see details below) from the database by accessing the RESTful API
* ENCRYPT and SUBMIT the data using SSL to an ONLINE PLATFORM for report generation, whereupon the report will be downloaded. 
* In the case where an Internet connection is unavailable, the program will store the data in an encrypted data package .dat file for manual submission.

## PRE-REQUIREMENTS

This tool __REQUIRES__:
*	A Deep Security Manager on version 11.1 or greater (DSaaS will work as well)
  *	If your DSM is currently on an older release than stated above, please check the Download Center for externally available patches or contact Trend Micro to receive the latest Feature Release and consider to upgrade at your earliest convenience.
*	A Key for the RESTful API with the following permissions:
  * VIEW Access to COMPUTERS
  * VIEW Access to POLICIES
  * VIEW Access to MALWARE SCAN CONFIGURATIONS
  * VIEW Access to FIREWALL STATEFULL CONFIGURATIONS
  * VIEW Access to TASKS
* A 8192-bit RSA public key (it should be included in the extractor.zip file).

__OPTIONAL__
* An Internet connection for automatic data submission and report download


# HOW TO USE/RUN THE EXPORT TOOL

1.	Access the DS Management Console and go to Administration > User Management > API Keys and Create a new key, configure it's permissions to have the "VIEW" access as noted above. 
  *	__WE STRONGLY RECOMMEND__ that you set an expiration date for the API access Key.
2.	Extract the extractor.zip contents into a folder.
3.	Access the api_config.yml file inside the config directory. Edit the fields accordingly and tool can be run on any computer able to connect to the DSM's RESTful API.
  * `host:	https://<The DSM API URL/IP Address>:<DS PORT>/api`
    * Make sure to enter `https://` and the DSM Console port
    * e.g.: https://app.deepsecurity.trendmicro.com/api 
    * e.g.: https://10.0.0.1:4119/api 
  *	`api-secret-key` The API Read-only access key
  *	`api-version` Version in use by the API. If in doubt, leave it as ‘v1’ (including the quotes)
4.	After saving the configurations, run the executable file. And follow the on-screen prompts as they appear.
  * Enter exact name of the public key file included in the .zip (keys/PUBLIC_key.pem by default)
  * Enter the Language of the final report.
    * `en` for English
    * `jp` for Japanese
  * Enter which of the DS modules to check, separated by spaces:
    * `all` for All Modules
    * `am` for anti_malware
    * `wr` for web_reputation
    * `im` for integrity_monitoring
    * `li` for log_inspection
    * `ac` for application_control
    * `fw` for firewall
    * `ip` for intrusion_prevention
  * (*OPTIONAL*, press `Enter` to skip each prompt) Enter the following data
    * Customer / Partner company's name.
    * Customer / Partner contact information
    * Trend Micro employee contact information
5. If an internet connection __is available__ 
* the Extractor will submit the data to the online platform and download the report as soon as it becomes available. __This process might take several minutes to complete__ 
* If the download fails, run the extractor by passing `--get ` and the __GENERATION ID__ provided in both the terminal window and the file GENERATION_ID.txt file. 
  * E.g.: `./extractor --get  333333-d000-aaaa-000f-fffeee11222`


6. If an internet connection is __not available__
* The data will be saved in an __encrypted file__ in the same directory where the tool was executed. 
* You can send the package in another machine, or once internet connectivity is established, by passing `--send` and the name of the data package.
  * E.g.: `./extractor --send data_pack_11112222333333.dat` 

## SUPPORT
__IF ALL ELSE FAILS__ and either file (re)submission or report download attempts are failling after multiple attempts, Contact the maintainers __describing the issue__ , sending the __generation ID__ and, if available, the __.dat file__ to alloflardsbpg@trendmicro.com

## NOT UPLOADING THE DATA PACK
You can pass the `--notsend` option to skip the file upload attempt and save the data_pack locally. 

`./extractor --notsend`

## GENERATING AN UNENCRYPTED DATA PACK

Running the Extractor with the `-u` switch as below will generate an __UNENCRYPTED__ .json file containing __ALL DATA EXTRACTED BY THE TOOL__. 

 `./extractor -u`

Please notice, that:
  * The __RESPONSABILITY__ of __HANDLING UNENCRYPTED__ data __LIES SOLELY__ with the customer's, partner's and/or Trend Micro's __employee running the tool__.
  * All data shown comes as it is provided by the official Deep Security SDK and that __not all data extracted is necessarily used in the report generation__.
    * The unencrypted file, if generated, should be used __EXCLUSIVELY__ for the customer's review of the extracted data and __SHOULD BE SECURELY DISCARDED__ and __NOT TRANSMITTED__ after such review. 

# WHAT WILL BE EXPORTED
The export tool will extract the following details through the RESTful API and Official SDK:
* Deep Security Agent configurations for all computers and computer groups registered in the Manager
*	Policy configurations for all policies currently in-use by at least one computer
*	Configurations for all Anti-Malware (Manual, Scheduled and Real-Time) and Stateful Firewall Configurations
* All Scheduled tasks in the environment


# DATA RETENTION PERIOD
The data package you shared will be removed after 45 days as of report creation.


# IMPACT ON ON-PREMISE INFRASTRUCTURE
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


# AUTHORS AND MAINTAINERS
Contact the current maintainers: alloflardsbpg@trendmicro.com

*Deep Security Health Check was originally Developed by*
* Anderson Leite <Anderson_Leite@trendmicro.com>
* Angelo Rodem <Angelo_Rodem@trendmicro.com>
* João Guimarães <Joao_Guimaraes@trendmicro.com>
* Tatiana Bohrer <Tatiana_Bohrer@trendmicro.com>
