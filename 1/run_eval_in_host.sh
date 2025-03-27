#!/bin/bash

docker build -t quadratic .

docker run --rm quadratic
