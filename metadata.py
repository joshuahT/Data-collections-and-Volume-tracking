import requests


def metadata_url():
    return f"https://public-api.solscan.io/token/meta"


def metadata_params(token):
    query_params = {"tokenAddress": "4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R"}
    return query_params
