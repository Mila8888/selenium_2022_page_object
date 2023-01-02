test-up: ## tests up
	docker pull selenoid/chrome:108.0
	docker-compose -p opencart -f docker-compose.yml up --build --abort-on-container-exit
	docker-compose -p opencart -f docker-compose.yml down

allure-report:
	docker cp opencart_tests_1:/app/allure_report . \
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
