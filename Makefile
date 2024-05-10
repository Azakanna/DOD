DOCKER_RUN=docker run \
				-it \
				--rm \
				-p 8000:8000 \
				--name authorization \
				authorization

build:
	docker build \
		--tag authorization \
		.

up: build
	${DOCKER_RUN}