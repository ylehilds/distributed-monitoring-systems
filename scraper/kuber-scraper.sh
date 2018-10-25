kubectl run scraper-1 --image=gryffindor:scraper --env="IP=192.168.35.1" --env="DATABASEIP=$1" --image-pull-policy=Never
