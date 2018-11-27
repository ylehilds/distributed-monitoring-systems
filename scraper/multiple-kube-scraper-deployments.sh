#!/bin/bash

while IFS='' read -r line || [[ -n $line ]]; do
	name=${line//./-}
  name="$(echo -e "${name}" | tr -d '[:space:]')"
	kubectl run "scraper-$name" --image=gryffindor:scraper --image-pull-policy=Never --env="IP=$line" --env="DATABASEIP=$2:$3"
done < "$1"
