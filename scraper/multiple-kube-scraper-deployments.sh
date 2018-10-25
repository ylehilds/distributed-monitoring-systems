#!/bin/bash

while IFS='' read -r line || [[ -n $line ]]; do
	name=${line//./-}
	kubectl run "scraper-$name" --image=gryffindor:scraper --image-pull-policy=Never --env="IP=$line" --env="DATABASEIP=$2"
done < "$1"
