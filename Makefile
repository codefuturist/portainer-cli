build:
	uv build

install:
	uv sync

install-dev:
	uv sync --group dev

lint:
	uv run flake8 portainer_cli/

run:
	uv run portainer-cli
