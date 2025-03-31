# run_eval_in_host.sh
#!/bin/bash
docker build -t encryption .
docker run --rm -it encryption