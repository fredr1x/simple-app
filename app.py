import	os
from flask import Flask
app	= Flask(__name__)
@app.route("/")
def	home():
    return	"App	is	running"
@app.route("/db")
def	db():
    password = os.getenv("DB_PASSWORD")
    return	f"DB password is {password}"

if __name__=="__main__":
    app.run()
