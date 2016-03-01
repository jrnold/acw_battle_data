DATA_DIR = data

build:
	python build.py $(DATA_DIR)

docs: html pdf

html:
	make -C docs html

pdf:
	make -C docs pdf


# Deploy data to S3
deploy:
	./bin/deploy.sh
