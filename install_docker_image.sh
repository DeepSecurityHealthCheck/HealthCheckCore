#!/bin/bash


CONTAINER_NAME="dshc"
CONTAINER_VERSION="1.8.5"

BASE_FOLDER=/etc/DSHC
KEYS_PATH=$BASE_FOLDER/keys
CONFIG_PATH=$BASE_FOLDER/config
REPORT_PATH=$BASE_FOLDER/reports
DATA_PACK=$BASE_FOLDER/data_packs


# Creating dirs for config and keys

if [ -d $CONFIG_PATH ] 
then
    echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ WARNING @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    echo "$CONFIG_PATH Already created, if you have no idea about what are you doing, please hit Ctrl+C now to stop or ENTER to continue"
    echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ WARNING @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    read
fi


# Removing and creating config folder
sudo rm -rf $BASE_FOLDER
sudo mkdir $BASE_FOLDER


# Creating sub dirs
sudo mkdir -p $KEYS_PATH
sudo mkdir -p $CONFIG_PATH
sudo mkdir -p $REPORT_PATH
sudo mkdir -p $DATA_PACK

sudo chown -R $(whoami):$(whoami) $BASE_FOLDER
sudo chmod +xwr -R $BASE_FOLDER

# Recreate API config file
python3 utils/gen_config.py
# Moving keys 
cp *.pem $KEYS_PATH -rf 2> /dev/null || cp ./keys/*.pem $KEYS_PATH -rf 2> /dev/null
# Moving configs
sudo cp config/* $CONFIG_PATH -rf


# Building image
docker container rm $(docker ps --filter=ancestor=$CONTAINER_NAME:$CONTAINER_VERSION -qa)
sudo docker rmi $CONTAINER_NAME:$CONTAINER_VERSION --force 2> /dev/null
sudo docker build --tag=$CONTAINER_NAME:$CONTAINER_VERSION .

RUN_SCRIPT="docker run -v $KEYS_PATH:/dshc/keys:rw -v $CONFIG_PATH:/dshc/config:ro -v $REPORT_PATH:/dshc/report_pdfs -v $DATA_PACK:/dshc/data_packs --rm -it $CONTAINER_NAME:$CONTAINER_VERSION"


sudo rm /usr/bin/dshc 2> /dev/null

echo "#!/bin/bash
    $RUN_SCRIPT" '$@' | sudo tee /usr/bin/dshc > /dev/null

sudo chmod +x /usr/bin/dshc
