from flask import Flask, render_template, request
import functions

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def get_phons():
    sel_phons = []
    lang = None
    comm_feat = {}
    sel_phons = request.form.getlist("phon_check")
    phons_to_pass = ",".join(sel_phons)
    print(sel_phons)
    lang = pass
    comm_feat = functions.compare_phonemes(lang, phons_to_pass)
    return render_template("index.html", selected_phonemes = sel_phons, language = lang, common_features = comm_feat)



