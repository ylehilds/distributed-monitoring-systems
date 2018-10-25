#!/bin/bash

while IFS='' read -r line || [[ -n $line ]]; do
	docker run -d -v /scraperlog:/scraperlog --name "scraper-docker-$line" -e "IP=$line" -e "DATABASEIP=$2" gryffindor:scraper
done < "$1"
