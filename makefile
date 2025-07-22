build:
	mkdir dist
	cp -r images dist/images
	cp -r src/static dist
	pip install -r requirements.txt
	python generator.py