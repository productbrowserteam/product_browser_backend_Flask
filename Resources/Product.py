from flask_restful import Resource, reqparse
from Models.ProductModel import ProductModel
from Models.CategoryModel import CategoryModel
import json


class Product(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="name required")
    parser.add_argument("url", type=str, required=False)
    parser.add_argument("description", type=str, required=False)
    parser.add_argument("subcategory", type=str, required=True, help="subcategory required")
    parser.add_argument("subcategoryUrl", type=str, required=True, help="subcategoryUrl required")
    parser.add_argument("cid", type=str, required=False)

    def get(self):
        products = ProductModel.query.all()
        if ProductModel.query.first():
            result = []
            for product in products:
                productdata = {"id": product.id,"name" : product.name, "description": product.description, "subcategory": {"name": product.subcategory, "url": product.subcategoryUrl}}
                result.append(productdata)
            return {"products": result}
        return {"message": "no products "}

    def post(self):
        request_data = Product.parser.parse_args()

        if ProductModel.find_by_name(request_data["name"]):
            return {"message": "product {} alredy exists in database".format(request_data["name"])}
        if CategoryModel.find_by_name(request_data["subcategory"]):
            product = ProductModel(request_data["name"], request_data["url"], request_data["description"], request_data["subcategory"], request_data["cid"])
            try:
                product.save_to_db()
            except:
                return {"message": "An error occured"}, 500
            return {"message": "product added"}
        return {"message": "category {} doesn't exist".format(request_data["subcategory"])}

    def delete(self):
        request_data = Product.parser.parse_args()
        product = ProductModel.find_by_name(request_data["name"])
        if product:
            product.delete_from_db()
            return {"message": "product {} deleted from database".format(request_data["name"])}
        return {"message": "error {} doesn't exist".format(request_data["name"])}


class Products(Resource):

    def get(self):
        with open("Prod.txt", "br") as json_file:
            data = json.load(json_file)
            for p in data["products"]:
                prod = ProductModel(p["name"], p["url"], p["description"], p["subcategory"][0]["name"], p["subcategory"][0]["url"])
                prod.save_to_db()
        return {"message": "product imported"}


class ProductsJson(Resource):

    def get(self):
        products = ProductModel.query.all()
        if ProductModel.query.first():
            result = []
            for product in products:
                productdata = { "name": product.name, "description": product.description,
                               "subcategory": [{"name": product.subcategory, "url": product.subcategoryUrl}]}
                result.append(productdata)
            return {"products": result}
        return {"message": "no products "}


class ProductModify(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="name required")
    parser.add_argument("url", type=str, required=False)
    parser.add_argument("description", type=str, required=False)
    parser.add_argument("subcategory", type=str, required=False, help="subcategory required")
    parser.add_argument("subcategoryUrl", type=str, required=False, help="subcategoryUrl required")
    parser.add_argument("cid", type=str, required=False)

    def post(self):
        request_data = ProductModify.parser.parse_args()

        product = ProductModel.find_by_name(request_data["name"])
        if product:
            product.url = request_data["url"]
            product.description = request_data["description"]
            product.subcategory = request_data["subcategory"]
            product.subcategoryUrl = request_data["subcategoryUrl"]
            product.modify_to_db()
            return {"message": "product updated"}
        return {"message": "product doesn't exist"}
