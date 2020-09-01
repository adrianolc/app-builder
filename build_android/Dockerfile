FROM androidsdk/android-29

WORKDIR /usr/src/build_android

COPY . ./

RUN apk --update add py3-pip && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

RUN pip3 install -r requirements.txt

EXPOSE 5001

CMD gunicorn --bind 0.0.0.0:5001 "api:create_app()" --timeout 1200 --log-file=-
