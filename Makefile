.PHONY : test_unit test_system test_integration

define PRETTYPRINT_PYSCRIPT
import sys, os
if len(sys.argv) == 1:
	print("="*os.get_terminal_size().columns + "\n\n")
	exit()
else:
    text = " " + " ".join(sys.argv[1:]) + " "
full_width = os.get_terminal_size().columns
padwidth = int((full_width-len(text)-2)/2)
outstr = "\n" + "="*int(padwidth) + text + "="*int(padwidth)
while len(outstr) < full_width:
    outstr += "="
print(outstr)
endef
export PRETTYPRINT_PYSCRIPT

# SETUP
test_venv: test_venv/touchfile

test_venv/touchfile:
	test -d test_venv || virtualenv test_venv
	. test_venv/bin/activate; \
	pip install -e '.[dev]'
	touch test_venv/touchfile

# BUILD
build: test_venv
	@. test_venv/bin/activate; \
	python -c "$$PRETTYPRINT_PYSCRIPT" BUILDING DISTRIBUTIONS; \
	python -m build

# TEST
test: test_venv test_unit
	@. test_venv/bin/activate; \
	python -c "$$PRETTYPRINT_PYSCRIPT"

test_all: test_venv test test_system

test_unit: test_venv
	@. test_venv/bin/activate; \
	python -c "$$PRETTYPRINT_PYSCRIPT" RUNNING UNIT TESTS; \
	pytest --cov=src tests/test_unit*.py -x

test_integration: test_venv
	@. test_venv/bin/activate; \
	python -c "$$PRETTYPRINT_PYSCRIPT" RUNNING INTEGRATION TESTS; \
	pytest --cov=src tests/test_integration*.py -x

test_system: test_venv
	@. test_venv/bin/activate; \
	python -c "$$PRETTYPRINT_PYSCRIPT" RUNNING SYSTEM TESTS; \
	pytest tests/test_system*.py -x

# TEARDOWN
clean:
	rm -rf test_venv
	rm -f .coverage
	find . -name "*.pyc" -type f -delete
	find . -name "*__pycache__" -delete

# UTILITIES
release: test_venv
	@. test_venv/bin/activate; \
	git reset *; \
	semantic-release changelog; \
	git add CHANGELOG.md; \
	git commit -m "docs: update changelog."; \
	semantic-release version
