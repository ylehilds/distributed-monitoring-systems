#!/bin/bash

docker run -d --name monitoring-docker -e HOST_IP=`hostname -I | awk '{print $1}'` gryffindor:monitoring
