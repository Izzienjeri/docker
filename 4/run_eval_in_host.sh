#!/bin/bash

docker build -t reconstructor .

docker run --rm reconstructor