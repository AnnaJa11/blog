from flask import render_template, Blueprint


routes_app = Blueprint('routes_app', __name__)



@routes_app.route("/")
def index():
   return render_template("base.html")
