FROM node:6.11.3-alpine

RUN apk --update add \
    git \
    nginx

RUN npm install -g bower
RUN npm install -g polymer-cli

COPY nginx.conf /etc/nginx/nginx.conf

WORKDIR /run/nginx

COPY ./views /usr/share/nginx/html/
WORKDIR /usr/share/nginx/html

RUN bower install --allow-root

CMD ["nginx", "-g", "daemon off;"]

