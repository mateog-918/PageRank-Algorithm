from flask import Flask, render_template, request, redirect, url_for
from data import strony, add_page, add_link, search_pages
from pagerank import compute_pagerank

app = Flask(__name__)

# Wczytaj dane testowe
add_page("Strona A", "To jest strona o kotach.")
add_page("Strona B", "To jest strona o psach.")
add_page("Strona C", "To jest strona o zwierzętach.")

@app.route("/")
def search():
    return render_template("search.html")

@app.route("/results")
def results():
    query = request.args.get("q", "")
    results = search_pages(query)
    return render_template("results.html", query=query, results=results)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/add_page", methods=["POST"])
def add_page_route():
    title = request.form["title"]
    text = request.form["text"]
    add_page(title, text)
    compute_pagerank()
    return redirect(url_for("search"))

@app.route("/link")
def link():
    return render_template("link.html", strony=strony)

@app.route("/add_link", methods=["POST"])
def add_link_route():
    src = request.form["source"]
    dst = request.form["destination"]
    add_link(src, dst)
    compute_pagerank()
    return redirect(url_for("search"))

@app.route("/recalculate")
def recalculate():
    compute_pagerank()
    return redirect(url_for("search"))

@app.route("/page/<title>")
def page(title):
    if title in strony:
        data = strony[title]
        return render_template("page.html", title=title, text=data["text"], links=data["links_to"])
    return "Strona nie istnieje", 404

if __name__ == "__main__":
    app.run(debug=True)
