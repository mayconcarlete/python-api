from dataclasses import dataclass

@dataclass
class TRequest:
    header: dict
    params: dict
    body: dict

@dataclass
class TResponse:
    status_code: int
    body: any