#!/bin/bash

docker build -t mean_columns .

docker run --rm mean_columns