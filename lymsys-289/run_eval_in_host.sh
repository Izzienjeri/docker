#!/bin/bash

# Build the Docker image
# Running the Docker container and execute eval.py for testing
docker build -t fibonacci_sequence .
docker run --rm fibonacci_sequence