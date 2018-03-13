from flask import Flask,render_template
from data import Articles

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def index():
	return render_template('home.html')

@app.route("/api")
def api():
	return render_template('api.html')

@app.route("/articles")
def articles():
	return render_template('articles.html')


if __name__ == "__main__":
    app.run(debug=True)
