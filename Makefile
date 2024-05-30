.PHONY: package upload-test upload

package:
	python setup.py check
	python setup.py sdist bdist_wheel

upload-test:
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload:
	python -m twine upload dist/*