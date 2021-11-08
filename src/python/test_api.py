"""Demo test."""

import requests

def test_api(baseurl):
    """Demo test for hitting the Warchest api

    Args:
        baseurl (str): The baseurl for the service
    """

    rsp = requests.get(f"{baseurl}/api/ping")

    print(rsp.content)