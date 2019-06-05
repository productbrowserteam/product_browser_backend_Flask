import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from Resources import  Category, Product


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



api.add_resource(Category.Category, '/category')
api.add_resource(Category.CategoryModify, '/category/modify')
api.add_resource(Product.Product, "/product")
api.add_resource(Product.Products, "/importproducts")
api.add_resource(Product.ProductsJson, "/product/json")
api.add_resource(Category.CategoryJson, "/category/json")



if __name__ == '__main__':
    app.run()