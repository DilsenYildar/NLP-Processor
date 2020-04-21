import flask
import spacy
import json
from flask import jsonify
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST'])
def parse_request():
    data = request.get_data()
    return initialize_nlp_process(data)


def initialize_nlp_process(data):
    nouns_json = []
    verbs_json = []
    entity_json = []

    doc = process_data(data)
    for noun in doc.noun_chunks:
        nouns_json.append(noun.text)
    for token in doc:
        if token.pos_ == "VERB":
            verbs_json.append(token.lemma_)
    for entity in doc.ents:
        entity_json.append(entity.text)
    return jsonify({"NounPhrases": nouns_json, "Verbs": verbs_json, "Entities": entity_json})


def process_data(data):
    nlp = spacy.load("en_core_web_lg")
    request_json = json.loads(data)
    text = request_json['document']
    return nlp(text)

app.run(port='5000')



