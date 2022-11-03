from flask import *

app = Flask(__name__)


@app.route('/users/<id>')
def users(id):
    return render_template(
        'show.html',
        name=id,
    )


if __name__ == '__main__':
    app.run(debug=True)
