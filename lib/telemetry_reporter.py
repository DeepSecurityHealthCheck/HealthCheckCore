import requests
import hashlib
import pickle
import json
import os
from colorama import Fore


def hashes(data_pack):
    if data_pack is not None:
        m = hashlib.sha256()
        m.update(pickle.dumps(data_pack))
        hash = m.digest()

        m = hashlib.sha256()
        m.update(pickle.dumps(data_pack.get('customer_info', None)))
        client_id = m.digest()
    else:
        m = hashlib.sha256()
        m.update(pickle.dumps(b"a"*16))
        hash = m.digest()

        m = hashlib.sha256()
        m.update(pickle.dumps(b"b"*16))
        client_id = m.digest()

    return client_id, hash


def report_crash(message, data_pack=None):
    url = os.environ.get("DSHC_CRASH_URL","")
    client_id, phash = hashes(data_pack)

    post_fields = {
            "crash-message": str(message),
            "packet-hash": phash.hex(),
            "unique-anonymous-id": client_id.hex()
    }

    print(Fore.LIGHTYELLOW_EX + message)
    try:
        r = requests.post(url=url, data=json.dumps(post_fields))
        if r.status_code != 200:
            print("\n" + Fore.LIGHTYELLOW_EX + "Could not submit telemetry, please inform manually this crash to alloflardsbpg@trendmicro.com")
        else:
            print("\n" + Fore.LIGHTRED_EX + "Anonymous crash telemetry submitted, returned:: {} {}".format(str(r.status_code), str(r.reason)))
    except requests.exceptions.ConnectionError:
        print("\n" + Fore.LIGHTYELLOW_EX + "Could not submit telemetry, please inform manually this crash to alloflardsbpg@trendmicro.com")



def report_execution(telemetry_data, data_pack=None):
    url = os.environ.get("DSHC_EXECUTED_URL","")

    client_id, phash = hashes(data_pack)

    dict_dump = {
        "unique-anonymous-id" : client_id.hex(),
        "packet-hash" : phash.hex()
    }

    post_fields = {**telemetry_data, **dict_dump}

    try:
        r = requests.post(url=url, data=json.dumps(post_fields))
        if r.status_code != 200:
            print("\n" + Fore.LIGHTYELLOW_EX + "Could not submit telemetry, please inform manually this execution to alloflardsbpg@trendmicro.com")
            print(r.content)
        else:
            print("\n" + Fore.LIGHTGREEN_EX + "Anonymous run telemetry submitted, returned: {} {}".format(str(r.status_code), str(r.reason)))
    except requests.exceptions.ConnectionError:
        print("\n" + Fore.LIGHTYELLOW_EX + "Could not submit telemetry, please inform manually this execution to alloflardsbpg@trendmicro.com")
