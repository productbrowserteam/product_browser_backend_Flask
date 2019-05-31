import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from Resources import ProductBrowser, Category, Product


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Ilikepie'
api = Api(app)

from db import db
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()



api.add_resource(ProductBrowser.PBlist, '/pb')
api.add_resource(Category.Category, '/cat')
api.add_resource(Category.CategoryModify, '/cat/mod')
api.add_resource(Product.Product, "/product")


if __name__ == '__main__':
    app.run()