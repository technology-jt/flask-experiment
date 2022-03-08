from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'JT',
        'title': 'Post One',
        'content': 'first post content!',
        'date_posted': '3/7/2022'
    },
    {
        'author': 'Toby',
        'title': 'Post Two',
        'content': 'second post content!',
        'date_posted': '3/7/2022'
    }
]


@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
