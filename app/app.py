from flask import Flask
from flask_admin import Admin
#from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)
# импорт нужен для миграций
from models import *

admin = Admin(app)
#admin.add_view(ModelView(Post, db.session))
