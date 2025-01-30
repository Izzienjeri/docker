#!/bin/bash

docker build -t eval_string .

docker run --rm eval_string