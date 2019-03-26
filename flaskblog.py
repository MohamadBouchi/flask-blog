from flask import Flask, render_template, url_for

app = Flask(__name__)


posts = [
    {
        'author': 'author1',
        'title': 'post1',
        'content': 'content1',
        'date_posted': 'april 20, 2019'
    },
    {
        'author': 'author2',
        'title': 'post2',
        'content': 'content2',
        'date_posted': 'april 22, 2019'
    },
    {
        'author': 'author3',
        'title': 'post3',
        'content': 'content2',
        'date_posted': 'april 22, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='about')


if __name__ == '__main__':
    app.run(debug=True)

video 3
