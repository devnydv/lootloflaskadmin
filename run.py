from lootloadmin import app
from lootloadmin.store import store

app.register_blueprint(store)
if __name__=="__main__":
    app.run(debug=True)