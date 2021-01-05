from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story 

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def ask_questions():
    """Generate and show form to ask words"""
    prompts = story.prompts