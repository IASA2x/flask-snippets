from flask import Flask, render_template, request, flash, url_for, redirect, make_response

app = Flask(__name__)

def create_response(text):
    resp = make_response(redirect(url_for("form")))
    resp.set_cookie("value", text)
    return resp


def executor(*data):
    def wrapper(*functions):
        for func in functions:
            yield func(*data)
    return wrapper


@app.route("/form", methods=['GET'])
def form():
    return render_template("form.html", cookies=request.cookies)


@app.route("/form", methods=['POST'])
def form_process():
    bar = executor(request.form.get("subject", "Oops"))
    resp, _ = bar(create_response, flash)
    return resp


if __name__ == '__main__':
    app.config.from_pyfile("config.py")
    app.run()

