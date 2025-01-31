# run_eval_in_host.sh
#!/bin/bash
docker build -t find_duplicates .
docker run --rm -it find_duplicates
