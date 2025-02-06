#!/bin/bash
docker build -t code_eval .
docker run --rm code_eval
