FROM python:3.8.2-alpine 

WORKDIR /usr/src/app

COPY . ./

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 "api:create_app()" --log-file=-
