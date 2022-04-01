from data import program_url, get_URLparams, connect_to_endpoint, txHashList
from signature import signature_url, get_SignatureParams
from metadata import metadata_params, metadata_url


def main():
    programurl = program_url()
    programparams = get_URLparams()
    json_response = connect_to_endpoint(programurl, programparams)
    # data = symboldata(json_response)
    # print(json_response)
    # counts = count(json_response)
    # print(counts)
    signature = txHashList(json_response)
    print(signature)
    signatureurl = signature_url()
    signature_params = get_SignatureParams()
    json_responses = connect_to_endpoint(signatureurl, signature_params)
    # for i in json_response["tokenBalanes"]
    token_address = json_responses["tokenBalanes"][0]["token"]["tokenAddress"]
    metadataurl = metadata_url()
    metadataparams = metadata_params(token_address)

    json_response3 = connect_to_endpoint(metadataurl, metadataparams)

    print(json_response3)


if __name__ == "__main__":
    main()
