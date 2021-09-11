from src.presentation.types.http import TRequest, TResponse
from src.presentation.interfaces.controller import IController


class AddUserController(IController):
    def handle(self, request: TRequest) -> TResponse:
        print('Sua request: ', request)
        return {
            'status_code': 201,
            'body':{
                'message': 'created'
            }
        }