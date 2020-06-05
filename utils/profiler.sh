#/bin/sh
# To be run INSIDE the utils/ directory



if pwd | grep utils;then
    cd ..
fi

FILEPATH_RAW="utils/performance_profile_raw.log"
FILEPATH_FILTERED="utils/performance_profile.log"

rm -f $FILEPATH_RAW $FILEPATH_FILTERED

NUM_COMPUTERS=(100 500 1000 5000 10000 50000)

for i in "${NUM_COMPUTERS[@]}";
do
    printf "Processing for $i computers\n"
    { /usr/bin/time -v python3 ./dshc.py -s $i >>$FILEPATH_RAW ;} &>> $FILEPATH_RAW
done

cat $FILEPATH_RAW | egrep "python|CPU|Maximum resident|time" > $FILEPATH_FILTERED


if pwd | grep utils;then
    cd utils
fi
