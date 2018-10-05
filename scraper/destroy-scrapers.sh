#!/bin/bash

while IFS='' read -r line || [[ -n $line ]]; do
	docker stop "scraper-docker-$line"
	docker rm "scraper-docker-$line"
done < "$1"
