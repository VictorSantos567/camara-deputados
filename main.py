from flask import Flask,render_template
import dao
import control
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", titulo="teste")

@app.route("/partidos")
def show_tables():
    dao.get_all_partys_current()
    df = control.transform_partys_dict_to_dataframe()
    html = df.to_html(classes='data')
    title = df.columns.values
    date = control.current_date()
    return render_template('partidos.html', tables=[html], titles=[title], date = date)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
