#!/bin/bash

docker run -it --name monitoring-docker -e HOST_IP=`hostname -I | awk '{print $1}'` gryffindor:monitoring
