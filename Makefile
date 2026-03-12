.PHONY: serve update test lint clear

serve:
	uv run mkdocs serve

update:
	uv run python scripts/update_dashboard.py

test:
	uv run pytest

lint:
	uv run ruff check .
	uv run mypy .

clear:
	uv run python scripts/clear_solutions.py
