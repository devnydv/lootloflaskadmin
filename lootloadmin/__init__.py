from flask import Flask


app = Flask(__name__)
app.secret_key ="doNotTryToSuck"


from lootloadmin import routes
from lootloadmin.store import store