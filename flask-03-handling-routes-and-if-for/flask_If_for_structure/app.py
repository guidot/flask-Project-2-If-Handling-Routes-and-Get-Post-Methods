from flask import Flask, render_template

# Create an object named app
app = Flask(__name__)


@app.route("/")
def head():
    """head() shows the message "first" in index.html
    and assigns it to the route of ('/')
    """
    first = "Test conditions"
    return render_template("index.html", message=first)
    # return render_template("index.html")


@app.route("/list")
def header():
    """header() prints elements of  a list
    one by one in index.html
    and assigns it to the route of ('/')
    """
    all_names = ["Anja", "Bob", "Charlotte", "Devil", "Erika", "Fabiano"]
    # numbers = range(1, 11)
    return render_template("body.html", names=all_names)


# run this app in debug mode on your local box
if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=8081)
