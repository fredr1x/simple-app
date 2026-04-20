from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def form():
    return """
    <h2>User Form</h2>
    <form method="POST" action="/submit">
        <input name="firstname" placeholder="First name" required />
        <br><br>
        <input name="lastname" placeholder="Last name" required />
        <br><br>
        <button type="submit">Submit</button>
    </form>
    """

@app.route("/submit", methods=["POST"])
def submit():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")

    payload = {
        "firstname": firstname,
        "lastname": lastname
    }

    return f"""
    <h2>Submitted Data</h2>
    <pre>{payload}</pre>
    <a href="/">Go back</a>
    """
