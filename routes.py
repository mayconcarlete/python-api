from sanic.response import json


def status(request):
    return json({'error':'some error from other file with auto reload'}, status=401)

def status_params(request, arg1):
    return json({'acertou': arg1})


def load_routes(app):
    app.add_route(status, '/status', methods=['GET'])
    app.add_route(status_params, '/status/<arg1>', methods = ['GET'])
