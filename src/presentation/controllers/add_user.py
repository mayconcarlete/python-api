from src.presentation.types.http import TRequest, TResponse
from src.presentation.interfaces.controller import IController


class AddUserController(IController):
    def handle(self, request: TRequest) -> TResponse:
        print('Sua request: ', request)
        status_code = self.sum()
        print(status_code)
        return {
            'status_code': self.sum(),
            'body':{
                'message': self.sum2()
            }
        }

    def sum(self):
        return 300
    
    def sum2(self):
        return 300