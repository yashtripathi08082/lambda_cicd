from lambda_function import lambda_handler

def test_lambda():

    response = lambda_handler({}, {})

    assert response["statusCode"] == 200