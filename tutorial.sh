#!/bin/bash

IMAGE_NAME=openai_tutorial
DOCKER_PATH=./tutorial_env/Dockerfile


build() {
	export $(cat .env | xargs)
	docker build \
	--build-arg OPENAI_API_KEY=$OPENAI_API_KEY \
	-t ${IMAGE_NAME} -f ${DOCKER_PATH} .
}

start() {

	# Check if container exists
	EXISTING_CONTAINER=$(docker ps -a -q --filter "name=${IMAGE_NAME}")

	if [ ! -z "$EXISTING_CONTAINER" ]; then
		# Remove existing container
		docker rm -f ${EXISTING_CONTAINER}
	fi

	# -i:interactive, -t:tty, --rm:remove container if exit --name:container name

	docker run --rm -it --name ${IMAGE_NAME} \
						-v ${PWD}/contents:/contents \
						${IMAGE_NAME} sh -c "bash"
}

if [[ "$1" == "build" ]]; then
	build
elif [[ "$1" == "start" ]]; then
	start
else
	echo "Invalid option. Use 'build' or 'start'"
fi