#!/bin/bash

while IFS='' read -r line || [[ -n $line ]]; do
	docker run -d -v /scraperlog:/scraperlog --name "scraper-docker-$line" -e "IP=$line" gryffindor:scraper
done < "$1"
