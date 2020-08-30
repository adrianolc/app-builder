FROM python:3.8.2-alpine 

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

RUN apk --update add git && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

COPY api api \
     git git \
     build_android build_android \
     settings.py ./ \
     .env .flaskenv ./ 

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 "api:create_app()" --timeout 600 --log-file=-
