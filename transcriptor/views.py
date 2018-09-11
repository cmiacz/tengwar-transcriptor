#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import request, render_template, jsonify

from . import app
from .model import TextTranscriptor, TengwarTableGenerator
from .languages import get_available_languages
from .languages import detector


text_transcriptor = TextTranscriptor()
table_genarator = TengwarTableGenerator()


@app.route('/')
@app.route('/index')
def root():
    return render_template("index.html", languages=get_available_languages())


@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)


@app.route('/transcribe', methods=['POST'])
def transcribe():
    text = request.form.get("sourceText", "")
    lang = request.form.get("language") or detector.detect_language(text)
    return jsonify({"language": lang, "text": text_transcriptor.transcribe(text, lang)})


@app.route('/table', methods=['POST'])
def table():
    lang = request.form.get("language")
    return render_template("table.html", tengwar_table=table_genarator.generate(lang))
