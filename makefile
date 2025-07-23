build:
	mkdir -p dist
	cp -r images dist
	cp -r src/static dist
	pip install -r requirements.txt
	python generator.py