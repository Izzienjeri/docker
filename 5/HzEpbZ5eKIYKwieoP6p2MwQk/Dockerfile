# Use an official Node.js image as the base image
FROM node:18

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install project dependencies (Jest in this case)
RUN npm install

# Copy the rest of your application files to the container
COPY . .

# Run the unit tests using Jest
CMD ["/bin/bash", "run.sh"]
