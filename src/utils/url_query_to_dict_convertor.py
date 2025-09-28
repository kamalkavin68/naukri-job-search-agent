from urllib.parse import parse_qs, unquote

def url_query_to_dict(query: str):
    query_dict = {k: v[0] if len(v) == 1 else v for k, v in parse_qs(query).items()}
    return query_dict
