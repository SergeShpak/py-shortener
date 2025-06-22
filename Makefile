.PHONY: sync
sync:
	uv sync --all-packages

.PHONY: lint
lint:
	uv run ruff check --fix