import json

import flask
import spacy
from flask import jsonify
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/process-doc', methods=['POST'])
def parse_request():
    data = request.get_data()
    return initialize_nlp_process(data)


def initialize_nlp_process(data):
    nouns_json = []
    verbs_json = []
    entity_json = []

    nlp = spacy.load("en_core_web_lg")
    doc = process_data(data, nlp)
    all_stopwords = nlp.Defaults.stop_words
    all_stopwords.remove("the")

    for noun in doc.noun_chunks:
        nounWords = noun.text.split()
        for nw in nounWords:
            for word in all_stopwords:
                if nw == word:
                    nounWords.remove(nw)
                    print("removed stop words:" + nw)
        text = ' '.join(nounWords)
        if len(text) > 0:
            nouns_json.append(text.lower())
    for token in doc:
        if token.pos_ == "VERB":
            verbs_json.append(token.lemma_.lower())
    for entity in doc.ents:
        entity_json.append(entity.text.lower())
    return jsonify({"NounPhrases": nouns_json, "Verbs": verbs_json, "Entities": entity_json})


def process_data(data, nlp):
    request_json = json.loads(data)
    text = request_json['document']
    return nlp(text)

app.run(port='5000')



