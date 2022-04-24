from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


# Main

@app.route('/')
def index():
    return render_template("index.html")

# Errors

@app.errorhandler(404)
def handle_404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def handle_500(e):
    return render_template('500.html'), 500


if __name__=="__main__":
	app.run(debug=True)
