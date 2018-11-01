#!/bin/bash

while IFS='' read -r line || [[ -n $line ]]; do
	name=${line//./-}
	kubectl delete deployment "scraper-$name"
done < "$1"
