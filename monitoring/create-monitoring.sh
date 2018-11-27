#!/bin/bash

docker run -d --restart always --name monitoring-docker -e HOST_IP=`hostname -I | awk '{print $1}'` -e USERNAME=`whoami` gryffindor:monitoring
