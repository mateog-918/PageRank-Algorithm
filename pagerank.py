# pagerank.py
from data import strony, pr

def compute_pagerank(d=0.85, max_iter=100, tol=1e-6):
    N = len(strony)
    if N == 0:
        return
    local_pr = {node: 1/N for node in strony}
    for _ in range(max_iter):
        new_pr = {}
        for node in strony:
            inbound = [src for src in strony if node in strony[src]["links_to"]]
            new_pr[node] = (1 - d) / N + d * sum(local_pr[src] / len(strony[src]["links_to"]) for src in inbound if strony[src]["links_to"])
        if all(abs(new_pr[n] - local_pr[n]) < tol for n in strony):
            break
        local_pr = new_pr
    pr.clear()
    pr.update(local_pr)