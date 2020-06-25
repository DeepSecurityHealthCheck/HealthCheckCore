from colorama import init, Fore
import os
EXTRACTOR_VERSION = "1.8.4"
EXTRACTOR_WIZARD_HEADER = """
DSHC EXTRACTOR v{}
By Running this tool you state that:
{}* YOU READ the INSTRUCTIONS and,
* AGREED with the TERMS AND CONDITIONS in the EXTRACTOR_README FILE 
{} To generate an UNENCRYPTED datapack, run the tool with -u """.format(EXTRACTOR_VERSION,Fore.LIGHTRED_EX,Fore.LIGHTMAGENTA_EX)

EXTRACTOR_HELP_STRING = """
VALID LANGUAGES INPUT
en  English
jp  Japanese

VALID MODULES INPUT (SPACE SEPARATED)
am  (Anti-Malware)
wr  (Web Reputation)
im  (Integrity Monitoring)
li  (Log Inspection)
ac  (Application Control)
fw  (Firewall)
ip  (Intrusion Prevention)
all (All modules)
"""

VALID_MODULES = {
    "am" : "anti_malware",
    "wr" : "web_reputation",
    "im" : "integrity_monitoring",
    "li" : "log_inspection",
    "ac" : "application_control",
    "fw" : "firewall",
    "ip" : "intrusion_prevention"
}

VALID_LICENSES = {
    #MALWARE_PREVENTION
    "mp" : ["am","wr"],
    #SYSTEM_SECURITY
    "ss" : ["im","li","ac"],
    #NETWORK_SECURITY
    "ns" : ["fw", "ip"],
    #ALL    #Enterprise and DSaaS
    "all" : list(VALID_MODULES.keys())
}

VALID_LANGUAGES = {
    "en" : "English",
    "jp" : "Japanese"
}
DEFAULT_LANGUAGE = "en"

LANGUAGE_ENV_NAME = "DSHC_LANG"

HTML_BASE_PATH="./report_templates/HTML_{}/"
CONFORMITY_STANDARDS_BASE_PATH = "conformity_standards/"
CONFORMITY_STANDARDS_SUFFIX = "_config_{}"
MODULE_DESCRIPTIONS_FILEPATH = "report_templates/module_descriptions_{}/bpg_descriptions.yml"

def format_paths():
    global HTML_BASE_PATH, CONFORMITY_STANDARDS_SUFFIX, MODULE_DESCRIPTIONS_FILEPATH
    l = os.environ.get(LANGUAGE_ENV_NAME,DEFAULT_LANGUAGE)
    HTML_BASE_PATH = HTML_BASE_PATH.format(l)
    CONFORMITY_STANDARDS_SUFFIX = CONFORMITY_STANDARDS_SUFFIX.format(l)
    MODULE_DESCRIPTIONS_FILEPATH = MODULE_DESCRIPTIONS_FILEPATH.format(l)
