from flask import Flask, render_template, request
import api
import backend

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/About/')
def about():
    return render_template('about.html')



@app.route('/search/', methods=["GET"])
def search():
    return render_template('search.html')

@app.route("/output/", methods=["GET", "POST"])
def get_phons():
    lang = request.form.get("languages")
    sel_phons = request.form.getlist("phon_check")
    comm_feat = (backend.compare_phonemes(lang, *sel_phons))[0]
    kitty = api.get_kitty()
    return render_template("output.html", selected_phonemes = sel_phons, language = lang, common_features = comm_feat, kitty = kitty)