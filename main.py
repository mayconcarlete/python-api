from sanic import Sanic
from sanic.response import text, json, html
from routes import load_routes

app = Sanic('MySanicApp')
load_routes(app)

@app.route("/")
async def handler(request):
    return html('<!DOCTYPE html><html lang="en"><meta charset="UTF-8"><div>Hi 😎</div>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)
