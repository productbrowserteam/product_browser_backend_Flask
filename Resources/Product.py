from flask_restful import Resource, reqparse
from Models.ProductModel import ProductModel
from Models.CategoryModel import CategoryModel


class Product(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="name required")
    parser.add_argument("url", type=str, required=False)
    parser.add_argument("description", type=str, required=False)
    parser.add_argument("subcategory", type=str, required=True, help="subcategory required")
    parser.add_argument("cid", type=str, required=False)

    def get(self):
        products = ProductModel.query.all()
        if ProductModel.query.first():
            result = []
            for product in products:
                productdata = {"id": product.id,"name" : product.name, "description": product.description, "subcategory": product.subcategory}
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