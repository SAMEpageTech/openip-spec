.PHONY: test
test:
	python -m openip_validate validate --schema cre/cre.schema.json --examples cre/examples && \
	python -m openip_validate validate --schema dre/dre.schema.json --examples dre/examples