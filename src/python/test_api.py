"""Demo test."""

import pytest
import requests

def test_api(baseurl):
    """Demo test for hitting the Warchest api and validates content and HTTP Status Code
    Args:
        baseurl (str): The baseurl for the service
    """

    rsp = requests.get(f"{baseurl}/api/ping")
    obj = rsp.json()

    assert obj['message'] == "pong"
    assert rsp.status_code == 200


@pytest.mark.flakey
def test_api_failure(baseurl):
    """ Demo test that produces failure
    Args:
        baseurl (str): The baseurl for the service
    """

    rsp = requests.get(f"{baseurl}/api/coin")
    assert rsp.status_code == 200
