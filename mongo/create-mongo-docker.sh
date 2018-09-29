sudo mkdir /mongodata
docker run -d -p 30001:27017 --name mongo-docker -v /mongodata:/data mongo
