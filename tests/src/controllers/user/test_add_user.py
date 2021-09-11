from src.presentation.controllers.add_user import AddUserController


def test_add_user_success():
    sut = AddUserController()
    request = {
        'body':{
            'name': 'valid_name',
            'age': 0,
            'weight': 10
        }
    }
    response = sut.handle(request)
    assert response['status_code'] == 201
    assert response['body'] == {
        'message': 'created'
    }