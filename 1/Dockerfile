FROM node:23-alpine

WORKDIR /usr/src/app

RUN apk update && apk add bash

COPY package*.json ./

RUN npm install

COPY . .

CMD ["/bin/bash", "run.sh"]