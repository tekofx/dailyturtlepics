FROM python:3.10-slim-buster
WORKDIR /bot/


COPY requirements.txt /tmp/
COPY src /bot/src

ENV TZ="Europe/Madrid"
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* \
        && python -m pip install --upgrade pip \
        && pip3 install -r /tmp/requirements.txt --no-cache-dir && pip3 install python-dotenv --no-cache-dir \
        && rm /tmp/requirements.txt 

CMD [ "python3","-u","/bot/src/main.py" ]