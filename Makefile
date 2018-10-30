run:
	cd src; \
	python eso-cap-builder.py --pdf 24.pdf --pages pages.txt

test:
	cd test; \
	python tests.py
