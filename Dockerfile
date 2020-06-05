# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Copy the current directory contentshinto the container at /app
COPY . /dshc

# Set the working directory to /app

WORKDIR /dshc

RUN apt-get update && \
    apt-get install -y \
    gcc zip php-cli php-xml php-imagick php-pear php-dom php-opcache php-font-lib php-mbstring php-gd composer curl && \
    apt-get install -y curl && curl --silent --location https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install nodejs -y &&\
    apt-get clean


# Setting enviroment Docker to work with data_packs
ENV ENV=DOCKER
ENV DSHC_EXECUTED_URL=$(DSHC_EXECUTED_URL)
ENV DSHC_CRASH_URL=$(DSHC_CRASH_URL)
# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade pip && \
    pip3 install --trusted-host pypi.python.org -r requirements.txt && \
    pip3 install ./vendor/SDK/ && \
    cd ./report_templates/HTML_en && composer install && cd ../.. && \
    cd ./report_templates/HTML_jp && composer install && cd ../.. && \
    cd ./report_templates/tech_report/ds_bpg_client/ && npm i && cd ../../../ &&\
    chmod +x dshc.py

# Run app.py when the container launches
ENTRYPOINT ["python3", "dshc.py"]
