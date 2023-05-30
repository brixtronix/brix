from flask_app.__innit__ import app
from flask_app.controllers.routes import Parcel

if __name__=="__main__":
    app.run(debug=True)