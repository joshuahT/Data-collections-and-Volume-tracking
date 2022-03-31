from data import create_url, get_params, connect_to_endpoint, txHashList


def main():
    url = create_url()
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    # data = symboldata(json_response)
    # print(json_response)
    # counts = count(json_response)
    # print(counts)
    tx = txHashList(json_response)
    print(tx)


if __name__ == "__main__":
    main()
