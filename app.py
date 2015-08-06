from flask import Flask, render_template, request, flash, url_for, redirect, make_response, session


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

def admin_only(func):
    def wrapper(*args, **kwargs):
        current_session = session.get("user", 0)
        if current_session == 0:
            return func(*args, **kwargs)
        else:
            return func(*args, **kwargs)
    return wrapper

@app.route("/form-creator")
@admin_only
def form_creator():
    return render_template("form_creator.html", openvariable="{{", closevariable="}}")

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

