#!/bin/bash
# run_eval_in_host.sh

# Build the docker container
docker build -t 987 .

if [ $? -eq 0 ]; then
    echo "Docker image built successfully."
else
    echo "Docker image build failed."
    exit 1
fi

# Run the docker container and remove the container once it exits.
docker run -it --rm 987

# Remove the Docker image
docker rmi 987


