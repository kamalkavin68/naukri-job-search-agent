from urllib.parse import parse_qs, unquote

def url_query_to_dict(query: str):
    query_dict = {k: unquote(v[0]) for k, v in parse_qs(query).items()}
    return query_dict
