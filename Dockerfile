FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y python3.12-venv

COPY requirements.txt requirements.txt
COPY README.md README.md

# CMD [ "python3 -m venv ktt-env" ]
# RUN python3 pip3 install -r requirements.txt