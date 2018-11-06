run:
	cd src; \
	python eso-cap-builder-gui.py &

test:
	cd src; \
	python -m unittest -v test_capjournal