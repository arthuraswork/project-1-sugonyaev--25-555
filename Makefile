st:
	poetry install
	poetry build
	poetry run project

install:
	poetry install

project:
	poetry run project

build:
	poetry build

version:
	poetry --version

publish:
	poetry publish --dry-run

package-install:
	poetry run pip install dist/*.whl

lint:
	poetry run ruff check .