from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def awal():
    return render_template('menuawal.html')

@app.route("/biodata")
def biodata():
    return render_template('biodata.html')

if __name__ == "__main__":
    app.run()