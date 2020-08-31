FROM alvrme/alpine-android:android-30

WORKDIR /usr/src/build_android

COPY . ./

RUN apk --update add py3-pip && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

RUN pip3 install -r requirements.txt
