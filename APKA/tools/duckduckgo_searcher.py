from duckduckgo_search import DDGS


# Connect to the Web and retreive Top 5 searches for Query
def web_search(query: str, max_results: int = 5) -> list:
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, region='wt-wt', safesearch="moderate", max_results=max_results):
            results.append(f"{r['title']}: {r['href']}")
    return results
