from unittest import mock

from src.presentation.controllers.add_user import AddUserController


def mock_return_value():
    return 401

def mock_return_value2():
    return 200

def test_add_user_success(print_fixture):
    mock_path = 'src.presentation.controllers.add_user.AddUserController.sum'
    mock2_path = 'src.presentation.controllers.add_user.AddUserController.sum2'
    with mock.patch(mock_path) as mck:
        with mock.patch(mock2_path) as mck2:
            mck.side_effect = mock_return_value
            mck2.side_effect = mock_return_value2
            sut = AddUserController()
            request = {
                'body':{
                    'name': 'valid_name',
                    'age': 0,
                    'weight': 10
                }
            }
            response = sut.handle(request)
            assert response == {
                'status_code': 401,
                'body':{
                    'message': 200
                }
            }