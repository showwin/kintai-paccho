.PHONY: fmt
fmt:
	poetry run black . && poetry run isort .

.PHONY: fmt-check
fmt-check:
	poetry run black . --check && poetry run isort . --check

.PHONY: test
test:
	poetry run python -m unittest discover
