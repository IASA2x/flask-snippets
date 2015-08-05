from flask import Flask, render_template, request, flash, url_for, redirect

app = Flask(__name__)

@app.route("/form", methods=['GET'])
def form():
    return render_template("form.html")

@app.route("/form", methods=['POST'])
def form_process():
    flash(request.form.get("subject", "Oops"))
    return redirect(url_for("form"))

if __name__ == '__main__':
    app.config.from_pyfile("config.py")
    app.run()

