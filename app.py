from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


repositories = [
    {'user': 'GeoscienceAustralia', 'repo': 'fc', 'coveralls': True},
    {'user': 'GeoscienceAustralia', 'repo': 'wofs'},
    {'user': 'GeoscienceAustralia', 'repo': 'digitalearthau', 'codecov': True},
    {'user': 'GeoscienceAustralia', 'repo': 'dea-orchestration', 'codecov': True},
    {'user': 'opendatacube', 'repo': 'datacube-core', 'rtd_name': 'datacube-core', 'codecov': True},
    {'user': 'opendatacube', 'repo': 'datacube-ows'},
    {'user': 'opendatacube', 'repo': 'datacube-stats', 'codecov': True},
    {'user': 'GeoscienceAustralia', 'repo': 'wagl'},
    {'user': 'GeoscienceAustralia', 'repo': 'eo-datasets', 'coveralls': True},
    {'user': 'GeoscienceAustralia', 'repo': 'COG-Conversion'},
    {'user': 'opendatacube', 'repo': 'datacube-charts'},
    {'user': 'GeoscienceAustralia', 'repo': 'dea-config'},
]


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', repos=repositories)


if __name__ == '__main__':
    app.run()
