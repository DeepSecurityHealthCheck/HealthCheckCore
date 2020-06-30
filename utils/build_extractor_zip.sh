#!/bin/bash


#Move the SSH keys (that were generated in the ubuntu user) to root
cp /home/ubuntu/.ssh/* ~/.ssh/ && \

#Add the bitbucket SSH fingerprint to do a git clone with no prompt
#ssh-keyscan  -H bitbucket.org >> .ssh/known_hosts
echo "|1|WA/b82K1Jx9SrX5NPH9gBUcgjgQ=|7ePmnw/2RTyIkkTWC/z/6gCu3J8= ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAubiN81eDcafrgMeLzaFPsw2kNvEcqTKl/VqLat/MaB33pZy0y3rJZtnqwR2qOOvbwKZYKiEO1O6VqNEBxKvJJelCq0dTXWT5pbO2gDXC6h6QDXCaHo6pOHGPUy+YBaGQRGuSusMEASYiWunYN0vCAI8QaXnWMXNMdFP3jHAJH0eDsoiGnLPBlBp4TNm6rYI74nMzgz3B9IikW4WVK+dc8KZJZWYjAuORU3jc1c/NPskD2ASinf8v3xnfXeukU0sJ5N6m5E8VLjObPEO+mN2t/FZTMZLiFqPWc/ALSqnMnnhwrNi2rbfg/rd/IpL8Le3pSBne8+seeFVBoGqzHM9yXw==" >> ~/.ssh/known_hosts && \

cd ~
git clone git@bitbucket.org:tmbrazil/dsbpg.git -q && \
cd dsbpg && \
git checkout deploy
git pull
#install SDK
pip3 install --upgrade -r requirements.txt
pip3 install ./vendor/SDK/ --ignore-installed && \

mkdir keys && \
aws s3 cp s3://dshc-public/PUBLIC_key.pem ./keys && \
EXTRACTOR_VERSION=$(grep "EXTRACTOR_VERSION =" < lib/constants.py | cut -d " " -f 3 | tr -d \") && \
ZIP_NAME=extractor$EXTRACTOR_VERSION-linux.zip && \
pyinstaller -F extractor.py --hidden-import=pkg_resources.py2_warn -p /usr/local/lib/python3.5/dist-packages/deepsecurity/ -p /usr/local/lib/python3.5/dist-packages/colorama/ -p /usr/local/lib/python3.5/dist-packages/requests/ && \
python3.5 utils/gen_config.py && \
zip $ZIP_NAME -j dist/extractor docs/EXTRACTOR_README.md && \
zip $ZIP_NAME extractor config/api_config.yml keys/PUBLIC_key.pem && \
aws s3 cp $ZIP_NAME s3://dshc-public/extractors/ && \
#Clean
poweroff
