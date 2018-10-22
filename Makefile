develop: install-deps
	pip install -e .

deps:
	pip-compile

install-deps:
	pip install -r requirements.txt

test:
	tox -v

.PHONY: develop deps install-deps test
