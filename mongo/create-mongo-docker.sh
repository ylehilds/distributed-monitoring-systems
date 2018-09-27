sudo mkdir /mongodata
docker run -d -p 27017:30001 --name mongo-docker -v /mongodata:/data mongo
