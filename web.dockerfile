FROM node:12-slim
WORKDIR /opt/todo
COPY web/package.json /opt/todo/package.json
COPY web/yarn.lock /opt/todo/yarn.lock
RUN yarn install
CMD ["yarn", "serve"]
