from flask import Flask, render_template, url_for

app = Flask(__name__)
student_details = {
                        "Naeemah": 25,
                        "godwin": 26,
                        "Thapelo": 47,
                        "Karabo": 23
                    }

# ADD A ROUTE DECORATOR


@app.route("/<name>")
@app.route("/home/<name>")
def home(name):
    return render_template("home.html", name="Amanda")


@app.route("/times/<int:number>")
def times(number):
    return render_template("numbers.html", number=number, student_details=student_details)


if __name__ == "__main__":
    app.debug = True
    app.run()