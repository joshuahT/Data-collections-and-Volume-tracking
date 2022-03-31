from data import program_url, get_URLparams, connect_to_endpoint, txHashList
from signature import signature_url, get_SignatureParams


def main():
    url = program_url()
    params = get_URLparams()
    json_response = connect_to_endpoint(url, params)
    # data = symboldata(json_response)
    # print(json_response)
    # counts = count(json_response)
    # print(counts)
    signature = txHashList(json_response)
    print(signature)
    urls = signature_url()
    paramss = get_SignatureParams()
    json_responses = connect_to_endpoint(urls, paramss)
    # for i in json_response["tokenBalanes"]
    print(json_responses["tokenBalanes"][0]["token"]["tokenAddress"])


if __name__ == "__main__":
    main()
