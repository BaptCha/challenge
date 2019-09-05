NAME = posos-challenge_1
PWD = $(shell pwd)
UID = $(shell id -u)
GID = $(shell id -g)

.PHONY: build_train
build_train:
	docker build -f trainer.Dockerfile --tag $(NAME)_trainer\
			--build-arg uid=$(UID)\
			--build-arg gid=$(GID)\
			.

.PHONY: run_train
run_train:
	docker run --name "training_container" $(NAME)_trainer

.PHONY: export_clf
export_clf:
	docker cp training_container:/home/appuser/text_clf.joblib.z Model/

.PHONY: train
train: build_train run_train export_clf
	

.PHONY: build_api
build_api:
	docker build -f api.Dockerfile --tag $(NAME)_api\
			--build-arg uid=$(UID)\
			--build-arg gid=$(GID)\
			.

.PHONY: run_api
run_api:
	docker run -p 4002:8888 --name "api_container" $(NAME)_api

.PHONY: api
api: build_api run_api