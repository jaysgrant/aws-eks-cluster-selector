install:
	pipenv install --dev --skip-lock

cov:
	pipenv run pytest --cov=cluster_selector --cov-report=html tests/unit
	open "./htmlcov/index.html"