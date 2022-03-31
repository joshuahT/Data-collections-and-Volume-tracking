import requests


def create_url():
    return f"https://public-api.solscan.io/account/transactions"


def get_params():
    query_params = {
        "account": "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K",
        "limit": 10,
    }
    return query_params


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, params=params)
    print(f"status code: {response.status_code}")
    if response.status_code != 200:
        raise Exception("Request error")
    return response.json()


def count(data):
    count = 0
    for i in range(len(data)):
        count = count + 1
    return count


def txHashList(response):
    txHash = []
    for i in range(len(response)):
        txHash.append(response[i]["txHash"])
    return txHash
