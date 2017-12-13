# ----------------------------------------
# TOP LEVEL TARGETS
# ----------------------------------------
all: build test 
test: metatest pytests
build: biolinkmodel/datamodel.py biolinkmodel/schema.py gen-golr-views ontology/biolink.ttl json-schema/biolink-model.json java gv

# ----------------------------------------
# BUILD/COMPILATION
# ----------------------------------------

gen-golr-views:
	./bin/gen-golr-views.py -d golr-views biolink-model.yaml


biolinkmodel/datamodel.py: biolink-model.yaml
	./bin/gen-py-classes.py $< > $@

ontology/biolink.ttl: biolink-model.yaml
	./bin/gen-rdf.py -o $@ $< 

ontology/%.json: ontology/%.ttl
	owltools $< -o -f json $@

ontology/%.obo: ontology/%.ttl
	owltools $< -o -f obo --no-check $@

ontology/%.omn: ontology/%.ttl
	owltools $< -o -f omn --prefix '' http://bioentity.io/vocab/ --prefix def http://purl.obolibrary.org/obo/IAO_0000115 $@

ontology/%.tree: ontology/%.json
	ogr --showdefs -t tree -r $< % > $@

ontology/%.png: ontology/%.json
	ogr-tree -t png -o $@ -c subClassOf subPropertyOf -r $< % 

gv: biolink-model.yaml 
	./bin/gen-graphviz.py -d graphviz $<

graphviz/%.png: biolink-model.yaml 
	./bin/gen-graphviz.py  -c $* $< -o graphviz/$*

graphql/biolink-model.graphql: biolink-model.yaml 
	./bin/gen-graphql.py $< > $@

#biolinkmodel/schema.py: biolink-model.yaml
#	./bin/gen-mm-schema.py $< > $@

# ----------------------------------------
# JSONSCHEMA
# ----------------------------------------
json-schema/%.json: %.yaml
	bin/gen-json-schema.py $< > $@.tmp && mv $@.tmp $@

JSONSCHEMA2POJO = $(HOME)/src/jsonschema2pojo/bin/jsonschema2pojo
java: json-schema/biolink-model.json
	$(JSONSCHEMA2POJO) --source $< -T JSONSCHEMA -t java-gen

# ----------------------------------------
# TESTS
# ----------------------------------------

pytests:
	pytest -s tests/*py

metatest: test-gen-meta test-gen-biolink-model

test-gen-%: test-pygen-% test-mmgen-%
	echo done

test-pygen-%: %.yaml
	./bin/gen-py-classes.py $< > $@ && python $@
test-mmgen-%: %.yaml
	./bin/gen-mm-schema.py $<

# ----------------------------------------
# METAMODEL
# ----------------------------------------

metamodel/jsonschema/metamodel.json: meta.yaml
	bin/gen-json-schema.py $< > $@

MM = metamodel/metamodel.py
#MMS = metamodel/metaschema.py
regen-mm:
	./bin/gen-py-classes.py meta.yaml  > $(MM)-tmp.py && python $(MM)-tmp.py && cp $(MM) $(MM)-PREV && mv $(MM)-tmp.py $(MM)
#regen-mms:
#	./bin/gen-mm-schema.py meta.yaml  > $(MM)-tmp.py && python $(MM)-tmp.py && cp $(MM) $(MM)-PREV && mv $(MM)-tmp.py $(MM)

# ----------------------------------------
# UTILS
# ----------------------------------------

dir-%:
	mkdir -p $@
