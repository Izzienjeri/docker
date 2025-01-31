#!/bin/bash

docker build -t extraction .

docker run --rm extraction