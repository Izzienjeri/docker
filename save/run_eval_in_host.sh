# run_eval_in_host.sh
#!/bin/bash
docker build -t nasdaq_filtered .
docker run --rm -it nasdaq_filtered