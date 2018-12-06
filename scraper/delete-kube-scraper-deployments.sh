#!/bin/bash

while IFS='' read -r line || [[ -n $line ]]; do
	name=${line//./-}
	name="$(echo -e "${name}" | tr -d '[:space:]')"
	kubectl delete deployment "scraper-$name"
done < "$1"
