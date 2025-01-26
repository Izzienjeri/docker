#!/bin/bash

# Build the Docker image
docker build -t jsdom-test .

# Run the Docker container to execute the tests
docker run --rm jsdom-test