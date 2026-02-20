pip install coverage
coverage run -m pytest # or: coverage run -m unittest discover -s tests
coverage xml -o coverage.xml
