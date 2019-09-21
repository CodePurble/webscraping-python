#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route("/books")
def book_handler():
    return "book"

@app.route("/bruh")
def bruh_handler():
    return "BRUH"

app.run()