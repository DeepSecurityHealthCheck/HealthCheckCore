import os
import subprocess
from tqdm import tqdm
import time
import getpass

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

dir_dp = "/etc/DSHC/data_packs"
directory = os.fsencode(dir_dp)
rd_dir = '/etc/DSHC/config/report_details.yml'

password = getpass.getpass("Insert the key's password: ").encode()

files = os.listdir(directory)
for file in tqdm(files, desc=">>> BACH PROCESSING PROGRESS"):
    filename = os.fsdecode(file)
    if filename.endswith(".dat") or filename.endswith(".DAT"):
        print("Current packet: " + filename)
        stream = open(rd_dir, 'r')
        details = load(stream, Loader=Loader)
        #path = os.path.join(dir_dp, filename)
        args = ['dshc', '-r', filename, '-k', 'PRIVATE_key.pem', '-p', password, '-o', filename+".zip"]
        details["customer_name"] = filename[:-4]
        stream.close()

        stream_save = open(rd_dir, 'w')
        output = dump(details, Dumper=Dumper)
        stream_save.write(output)
        stream_save.close()

        ret = subprocess.call(args)
        #print('\n' + ret.stderr.decode("utf-8"))
        #print(ret.stdout.decode("utf-8"))
    else:
        print("Invalid file: " + filename)

    time.sleep(0.3)