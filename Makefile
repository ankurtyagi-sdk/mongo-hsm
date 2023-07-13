#
# Copyright (c) 2022, 2023 by Delphix. All rights reserved.
#
.PHONY: compose-up compose-down compose-clean

VERSION := 8.0.0
HSC_COMMON_CONTAINER_IMAGES := delphix-hyperscale-masking

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

unload-service/.venv:
	-$(call make_unload)

load-service/.venv:
	-$(call make_load)

compose-up: unload-service/.venv load-service/.venv
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
	@# Help: Cleans env and image created by the compose-up command'
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