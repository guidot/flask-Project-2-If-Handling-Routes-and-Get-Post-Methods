from flask import Flask, redirect, url_for, render_template

# Create an object named app
app = Flask(__name__)


@app.route("/")
def home():
    """returns a string
    'This is home page for no path, <h1> Welcome Home</h1>'
    and assigns the root route ('/')
    """
    return "This is home page for no path, <h1> Welcome Home</h1>"


@app.route("/about")
def about():
    """returns a formatted string
    '<h1>This is my about page </h1>'
    and assigns it to the static route of ('about')
    """
    return "<h1>This is my about page </h1>"


@app.route("/error")
def error():
    """returns a formatted string
    '<h1>Either you encountered an error or you are not authorized.</h1>'
    and assign to the static route of ('error')
    """
    return "<h1>Either you encountered an error or you are not authorized</h1>"


@app.route("/admin")
def admin():
    """redirects the request to the error path
    and assigns it to the route of ('/admin')
    """
    return redirect(url_for("error"))


@app.route("/<name>")
def greet(name):
    """Create a function named greet which return formatted inline html string
    and assign to the dynamic route of ('/<name>')
    """
    greet_format = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Greeting Page</title>
</head>
<body>
    <h1>Hello, { name }!<h1>
    <h1>Welcome to my Greeting Page</h1>
</body>
</html>
    """
    return greet_format


@app.route("/greet-admin")
def greet_admin():
    """redirect the request to the hello path with param of 'Master Admin!!!!'
    and assigns it to the route of ('/greet-admin')
    """
    return redirect(url_for("greet", name="Master Admin!!!!"))


"""Rewrite a function named greet which uses template file named `greet.html`
under `templates` folder and assign to the dynamic route of ('/<name>').

Please find a template html file named `greet.html` which takes `name`
as parameter under `templates` folder
"""

# @app.route('/<name>')
# def greet(name):
#     return render_template('greet.html', name=name)


@app.route("/list10")
def list10():
    """Create a function named list10 which creates a list counting
    from 1 to 10 within `list10.html` and assign to the route of ('/list10').

    Please find a template html file named `list10.html` which shows
    a list counting from 1 to 10 under `templates` folder
    """
    return render_template("list10.html")


@app.route("/evens")
def evens():
    """show the even numbers from 1 to 10 within `evens.html`
    and assign to the route of ('/evens').
    Please find a template html file named `evens.html` which shows
    a list of even numbers from 1 to 10 under `templates` folder
    """
    return render_template("evens.html")


# Run the Flask application which listens on any network interfaces on port 8081.
if __name__ == "__main__":
    app.run(debug=True)
# app.run(host='0.0.0.0', port=8081)
