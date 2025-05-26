# app.py
from flask import Flask, render_template, request, redirect, url_for
from data import strony, add_page, add_link, search_pages
from pagerank import compute_pagerank

app = Flask(__name__)

# deafultowe strony bez linków
add_page("Strona A", "To jest przykładowa strona o kotach.")
add_page("Strona B", "To jest przykładowa strona o psach.")
add_page("Strona C", "To jest przykładowa strona o zwierzętach.")
add_page("Strona D", "To jest nowa strona bez linków.")

@app.route("/")
def index():
    query = request.args.get("q", "")
    if query:
        results = search_pages(query)
    else:
        results = []
    return render_template("index.html", query=query, results=results, strony=strony)

@app.route("/page/<title>")
def page(title):
    if title in strony:
        data = strony[title]
        return render_template("page.html", title=title, text=data["text"], links=data["links_to"])
    return "Strona nie istnieje", 404

@app.route("/add_page", methods=["POST"])
def add_page_route():
    title = request.form["title"]
    text = request.form["text"]
    add_page(title, text)
    return redirect(url_for("index"))

@app.route("/add_link", methods=["POST"])
def add_link_route():
    src = request.form["source"]
    dst = request.form["destination"]
    add_link(src, dst)
    return redirect(url_for("index"))

@app.route("/recalculate")
def recalculate():
    compute_pagerank()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)