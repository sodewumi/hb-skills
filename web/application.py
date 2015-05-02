from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/fill")
def render_form():
    return render_template("application-form.html")

@app.route("/response")
def write_response():
    last_name_py = request.args.get("last_name_form")
    first_name_py = request.args.get("first_name_form")
    salary_py = request.args.get("salary_form")
    position_py = request.args.get("applying")

    return render_template("response.html", first_name_response =first_name_py,
        last_name_response = last_name_py, salary_response = salary_py,  position_response = position_py)

if __name__ == "__main__":
    app.run(debug=True)