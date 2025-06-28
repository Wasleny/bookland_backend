export PYTHONPATH := $(PWD)

# .PHONY: test test-cov lint format typecheck run

.PHONY: test test-cov lint format typecheck run migrate downgrade history

test:
	pytest -v

# test-cov:
# 	pytest --cov=bookland --cov-report=term-missing -v

test-cov:
	coverage run -m pytest
	coverage report -m
	coverage html

lint:
	black bookland tests --check

format:
	black bookland tests

typecheck:
	mypy bookland --explicit-package-bases

migrate:
	python migrate.py migrate

downgrade:
	python migrate.py downgrade

history:
	python migrate.py history

run:
	uvicorn bookland.interfaces.api.main:app --reload --host 0.0.0.0 --port 8000
	