#!/bin/bash

# Build the Docker image
docker build -t leap-years-test .

# Run the Docker container
docker run --rm leap-years-test