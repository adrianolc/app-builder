FROM python:3.8.2-alpine 

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN python3 -m venv .venv
RUN .venv/bin/pip3 install --upgrade pip
RUN .venv/bin/pip3 install -r requirements.txt

COPY api api
COPY git git
COPY build_android build_android
COPY .env .flaskenv ./
COPY settings.py boot.sh ./

RUN chmod a+x boot.sh

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]