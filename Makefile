DATA_DIR = data
BUCKET = jrnold-data/acw_battle_data
REGION = us-west-2

build:
	python build.py $(DATA_DIR)

docs: html pdf

html:
	make -C docs html

pdf:
	make -C docs pdf


# Deploy data to S3
deploy:
	python ./bin/deploy.py $(DATA_DIR) $(BUCKET) $(REGION)
