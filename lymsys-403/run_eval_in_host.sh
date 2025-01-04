# run_eval_in_host.sh
#!/bin/bash
docker build -t 403 .
docker run -it --rm 403