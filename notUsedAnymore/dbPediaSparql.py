from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
# sparql.setQuery("""
#     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#     SELECT ?label
#     WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }
# """)
# sparql.setQuery("select ?o { <http://dbpedia.org/resource/The_Beatles> rdf:type ?o}")
sparql.setQuery("SELECT DISTINCT ?p WHERE { "
                "OPTIONAL { <http://dbpedia.org/resource/IBM>  ?p  ?o } "
                "OPTIONAL {?s  ?p  <http://dbpedia.org/resource/IBM> } } "
                "ORDER BY ?p")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["p"]["value"])
