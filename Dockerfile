FROM python:3.8.2-alpine 

WORKDIR /app-builder

COPY requirements.txt ./

RUN python3 -m venv .venv
RUN .venv/bin/pip3 install -r requirements.txt

COPY api api
COPY .env .flaskenv ./
COPY settings.py boot.sh ./

RUN chmod a+x boot.sh

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]