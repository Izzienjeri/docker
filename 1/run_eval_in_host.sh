# run_eval_in_host.sh 
#!/bin/bash

#Build the docker container
docker build -t task_1087 .

# Run the docker container and remove the container once it exits.
docker run --rm task_1087

# Remove the Docker image
docker rmi task_1087
