run:
	docker run --rm -it --env-file .env -p 8080:8080 filtro-githubapp

build:
	docker build -t filtro-githubapp .

test:
	curl http://localhost:8080/docs

shell:
	docker exec -it $(docker ps -qf ancestor=filtro-githubapp) /bin/bash