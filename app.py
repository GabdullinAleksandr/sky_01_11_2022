from flask import Flask, render_template, request

app = Flask(__name__)

users = ['mike', 'mishel', 'adel', 'keks', 'kamila']


@app.route('/users/')
def user():
    term = request.args.get('term')
    return render_template(
        'index.html',
        users=users,
        search=term,
    )


if __name__ == '__main__':
    app.run(debug=True)
