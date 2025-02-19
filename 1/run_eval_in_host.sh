#!/bin/bash
docker build -t 1182_golden .
docker run --rm 1182_golden
