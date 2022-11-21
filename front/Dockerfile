FROM node:18

WORKDIR /tapRides

COPY package.json ./
RUN npm install

COPY . .

CMD ["npm", "start"]