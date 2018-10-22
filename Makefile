run:
	marketplace

develop: install-deps
	pip install -e .

deps:
	pip install -U pip pip-tools
	pip-compile

install-deps:
	pip install -r requirements.txt

zip:
	python setup.py sdist --format=zip

.PHONY: develop deps install-deps run test
