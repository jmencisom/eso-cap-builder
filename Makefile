run:
	cd src; \
	python eso-cap-builder-gui.py &

test:
	python -m unittest discover