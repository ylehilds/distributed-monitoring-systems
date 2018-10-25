docker run -d -v /scraperlog:/scraperlog --name scraper-docker -e "IP=192.168.35.5" -e "DATABASEIP=$1" gryffindor:scraper
