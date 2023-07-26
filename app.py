from flask import Flask
from routes import join_routes
from models import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1:3306/data'
db.init_app(app)
app.app_context().push()

migrate =Migrate(app,db)

db.create_all()

app.register_blueprint(join_routes)

if __name__ == '__main__':
    app.run(debug=True)