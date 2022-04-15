from fastapi.testclient import TestClient

from ..app import app

from mysk_utils.response import InternalCode

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.headers["X-Internal-Code"] == str(
        InternalCode.IC_GENERIC_SUCCESS.value
    )
    assert response.status_code == 200
    assert response.json() == {"status": True}


# def test_gql_health_check():
#     query = """
#     query test {
#         health
#     }
#     """

#     response = schema.execute_sync(query)
#     assert response.data == {"health": True}
#     assert response.errors == None
