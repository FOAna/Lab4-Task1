from jinja2 import Environment, FileSystemLoader
from webob import Request
import os

assets =[
    'app.js',
    'react.js',
    'leaflet.js',
    'D3.js',
    'moment.js',
    'math.js',
    'main.css',
    'bootstrap.css',
    'normalize.css',
    ]
javascript = []
css = []

def app(environ, start_response):
    status = '200 OK'
    response_headers = ('Content-Type', 'text/HTML')
    start_response(status, [response_headers])

    for item in assets:
        (name, extension) = os.path.splitext(item)
        if extension == '.css':
            css.append(item)
        elif extension == '.js':
            javascript.append(item)

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('index.html')
    print(template.render(styles=css, scripts=javascript))

req2 = Request.blank('index.html')
print(req2.get_response(app))
