# run_eval_in_host.sh
#!/bin/bash

# Build the docker container
docker build -t 286 .

# Run the docker container and remove the container once it exits.
docker run -it --rm 286

# Remove the Docker image
docker rmi 286