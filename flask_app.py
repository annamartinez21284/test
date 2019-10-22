from flask import Flask, render_template

# Configure application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.form.get("button")
        return render_template("test.html")
    return render_template("index.html")
