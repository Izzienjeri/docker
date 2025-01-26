#!/bin/bash

docker build -t categorical_encoder_project .
docker run --rm categorical_encoder_project

