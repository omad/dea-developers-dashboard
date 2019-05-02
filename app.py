from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


repositories = [
    {'user': 'GeoscienceAustralia', 'repo': 'fc', 'branch': 'master', 'coveralls': True},
    {'user': 'GeoscienceAustralia', 'branch': 'master', 'repo': 'wofs'},
    {'user': 'GeoscienceAustralia', 'repo': 'digitalearthau', 'branch': 'develop', 'codecov': True},
    {'user': 'GeoscienceAustralia', 'repo': 'dea-orchestration', 'branch': 'master', 'codecov': True},
    {'user': 'opendatacube', 'repo': 'datacube-core', 'branch': 'develop', 'rtd_name': 'datacube-core', 'codecov': True},
    {'user': 'opendatacube', 'repo': 'datacube-ows', 'branch': 'master'},
    {'user': 'opendatacube', 'repo': 'datacube-stats', 'branch': 'master', 'codecov': True},
    {'user': 'GeoscienceAustralia', 'repo': 'wagl', 'branch': 'develop'},
    {'user': 'GeoscienceAustralia', 'repo': 'eo-datasets', 'branch': 'develop', 'coveralls': True},
    {'user': 'GeoscienceAustralia', 'repo': 'COG-Conversion', 'branch': 'master'},
    {'user': 'opendatacube', 'repo': 'datacube-charts'},
    {'user': 'GeoscienceAustralia', 'repo': 'dea-config'},
]


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', repos=repositories)


if __name__ == '__main__':
    app.run()
