FROM node:13-alpine
WORKDIR /app
COPY app/package.json package.json
RUN npm install
RUN npm install react-scripts@3.3.1 -g --silent