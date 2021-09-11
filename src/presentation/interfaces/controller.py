import abc

from src.presentation.types.http import TRequest, TResponse


class IController(abc.ABC):
    
    @abc.abstractmethod
    def handle(self, request: TRequest) -> TResponse:
        raise NotImplementedError