from flask import render_template, Blueprint

from managers.dataset_manager import get_dataset

markup_bp = Blueprint('markup_bp', __name__)

@markup_bp.route("/document/<id>")
def document(id):
    dataset_loader = get_dataset()
    corpus = dataset_loader.get_by_doc_id(id)
    return render_template("document.html", corpus=corpus)

@markup_bp.route("/")
def index():
    dataset_loader = get_dataset()
    whole_corpus = dataset_loader.get_all_corpus()
    print(whole_corpus)
    return render_template("index.html", whole_corpus=whole_corpus)