#!/bin/bash
docker stop "monitoring-docker"
docker rm -f "monitoring-docker"
docker rmi -f "gryffindor:monitoring"

