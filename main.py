from flask import Flask,render_template

app = Flask(__name__)


@app.route("/partidos")
def index():
    return render_template("index.html", titulo="Teste")

if __name__ == '__main__':
    app.run(debug=True)
