# data.py
strony = {}

pr = {}  # PageRanky

def add_page(title, text):
    if title not in strony:
        strony[title] = {"text": text, "links_to": []}

def add_link(src, dst):
    if src in strony and dst in strony:
        if dst not in strony[src]["links_to"]:
            strony[src]["links_to"].append(dst)

def search_pages(query):
    results = []
    for title, data in strony.items():
        if query.lower() in data["text"].lower() or query.lower() in title.lower():
            results.append((title, pr.get(title, 0)))
    return sorted(results, key=lambda x: x[1], reverse=True)
