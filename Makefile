ifeq ($(wildcard pyvenv),)
    PYTHON = python3
else
    PYTHON = pyvenv/bin/python
endif


all:

init:
	$(PYTHON) -m pip install -r requirements.txt

init-dev: init
	$(PYTHON) -m pip install -r requirements-dev.txt

venv:
	if [ ! -d 'pyvenv' ]; then python3 -m virtenv pyvenv; fi

lint: init-dev
	flake8 centreoncdiff
	flake8 tests

test: init-dev lint
	$(PYTHON) -m unittest discover -s tests

coverage: init-dev lint
	$(PYTHON) -m coverage run --source centreoncdiff -m unittest discover -s tests
	$(PYTHON) -m coverage report -m

build: init-dev
	$(PYTHON) -m build --sdist --wheel --outdir dist/

deploy-test: build
	$(PYTHON) -m twine upload dist/* --repository-url https://test.pypi.org/legacy/ -u __token__ -p $(REPO_PYPI_TEST_TOKEN)

deploy: build

clean:
	rm -rf pyvenv dist .pytest_cache .coverage
	find -name '*pyc*' -delete
	find -name '*__pycache__*' -delete
