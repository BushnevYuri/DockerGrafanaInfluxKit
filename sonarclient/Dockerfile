FROM python:3

ENV HTTPS_PROXY "http://172.25.1.1:3128"

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY sonar-client.py ./

RUN pip3 install --no-cache-dir -r requirements.txt


CMD [ "python3", "./sonar-client.py" ]
