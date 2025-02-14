from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///expensesDB.db'
app.config['SECRET_KEY'] = 'JLK689O3IU45olnojojouuo543o=5y9y9youjdsohhbafdnoglhoho'

db = SQLAlchemy(app)


from application import routes