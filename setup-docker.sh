# NOTE: Run with sudo

# remove old docker installments
apt-get remove docker docker-engine docker.io

# set up apt
apt-get update
apt-get install \
	apt-transport-https \
	ca-certificates \
	curl \
	software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository \
	"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
	$(lsb_release -cs) \
	stable"

# install docker
apt-get update
apt-get install docker-ce

# add user to docker sudo group
groupadd docker
usermod -aG docker $USER

# pull mongo dockerfile
docker pull mongo
