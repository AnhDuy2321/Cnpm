from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/t")
def test():
    return "Welcome to saleapp!"
if __name__ == "__main__":
    app.run(debug=True)