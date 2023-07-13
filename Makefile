#
# Copyright (c) 2022, 2023 by Delphix. All rights reserved.
#
.PHONY: compose-up compose-down compose-clean

VERSION := 8.0.0
ROOT_DIR := $(shell pwd)
HSC_COMMON_CONTAINER_IMAGES := delphix-hyperscale-masking
VENV_UNLOAD := $(ROOT_DIR)/unload-service/.venv
VENV_LOAD := $(ROOT_DIR)/load-service/.venv

define make_unload
	-@echo "Creating Unload Service env"
	@cd unload-service && make env && make docker-image
	-@echo "Creation of Unload Service env complete"
endef

define make_load
	-@echo "Creating Load Service env"
	@cd load-service && make env && make docker-image
	-@echo "Creation of Load Service env complete"
endef

define clean
	@cd unload-service && make docker-rm && make clean_env
	@cd load-service && make docker-rm && make clean_env
endef

$(VENV_UNLOAD):
	-$(call make_unload)

$(VENV_LOAD):
	-$(call make_load)

compose-up: $(VENV_UNLOAD) $(VENV_LOAD)
	@# Help: Start all containers services inside mongo
	-@docker load -i $(HSC_COMMON_CONTAINER_IMAGES)-$(VERSION)/masking-service.tar
	-@docker load -i $(HSC_COMMON_CONTAINER_IMAGES)-$(VERSION)/controller-service.tar
	-@docker load -i $(HSC_COMMON_CONTAINER_IMAGES)-$(VERSION)/proxy.tar
	-@export VERSION=$(VERSION); docker-compose up -d;
	-@docker-compose ps

compose-down:
	@# Help: Stop all containers services inside mongo
	-@docker-compose down

compose-clean: compose-down
	@# Help: Cleans env and image created by the compose-up command
	$(call clean)


# A hidden target
.hidden:
help:
	@printf "%-20s %s\n" "Target" "Description"
	@printf "%-20s %s\n" "------" "-----------"
	@make -pqR : 2>/dev/null \
        | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' \
        | sort \
        | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' \
        | xargs -I _ sh -c 'printf "%-20s " _; make _ -nB | (grep -i "^# Help:" || echo "") | tail -1 | sed "s/^# Help: //g"'