SHELL := /bin/bash
PROJECT_NAME = dsalgo-scala

DOCKER_IMG := $(PROJECT_NAME):latest
MOUNT_SRC := -v $(PWD)/src:/dsalgo/src

# Source https://gist.github.com/coryodaniel/5fb5503953ca799cd51adc6764324780
help: ## Print this beautiful help
	@grep -E '^[a-zA-Z_0-9-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## Clean the image
	docker rmi $(DOCKER_IMG) --force
	docker volume rm $(PROJECT_NAME) --force

build: ## Build sbt image with deps
	docker build -t $(DOCKER_IMG) .

shell: ## Opens a shell to interact inside the container
	@docker run --rm -it $(MOUNT_SRC) $(DOCKER_IMG) bash

console: ## Opens sbt console
	@docker run --rm -it $(MOUNT_SRC) $(DOCKER_IMG) sbt console

check: ## Run unit tests
	@docker run --rm -it $(MOUNT_SRC) $(DOCKER_IMG) sbt test
