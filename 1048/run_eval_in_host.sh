# run_eval_in_host.sh
#!/bin/bash
docker build -t middle .
docker run --rm -it middle