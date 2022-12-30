test-up: test-down ## tests up
	docker-compose -p opencart -f docker-compose.yml up -d

allure-report:
	docker cp opencart_tests:/app/allure-report . \
	&& allure serve allure-report

test-down: ## tests down
	docker-compose -p opencart -f docker-compose.yml down

app-clean: ## dell all images and clean кеш
	docker system prune -a -f
	docker volume prune -f

clean:: ## Remove all containers, images and volumes
	-docker container stop $$(docker ps -q -a)
	-docker container rm $$(docker ps -q -a)
	docker image prune -f
	docker volume prune -f
