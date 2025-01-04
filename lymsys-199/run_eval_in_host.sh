# run_eval_in_host.sh
#!/bin/bash
docker build -t python_program_199 .
docker run --rm -it python_program_199