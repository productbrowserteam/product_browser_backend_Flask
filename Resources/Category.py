from flask_restful import Resource, reqparse
from Models.CategoryModel import CategoryModel


class Category(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="name required")
    parser.add_argument("url", type=str, required=True, help="name required")
    parser.add_argument("parentCategory", type=str, required=False)

    def post(self):
        request_data = Category.parser.parse_args()
        if CategoryModel.find_by_name(request_data["name"]):
            return{"message": "Page already exists in database"},400
        category = CategoryModel(request_data["name"],request_data["url"],request_data["parentCategory"])
        try:
            category.save_to_db()
        except:
            return {"message": "An error occured"}, 500
        return {"message": "page added"}

    def delete(self):
        request_data = Category.parser.parse_args()
        cat = CategoryModel.find_by_name(request_data["name"])
        if cat:
            cat.delete_from_db()
            return {"message": "category deleted"}
        return {"message" "category {} doesn't exist".format(request_data["name"])}


class CategoryModify(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("newname", type=str, required=True, help="newname required")
    parser.add_argument("name", type=str, required=True, help="name required")
    parser.add_argument("url", type=str, required=True, help="name required")
    parser.add_argument("parentCategory", type=str, required=False)

    def post(self):
        request_data = CategoryModify.parser.parse_args()

        try:
            cat = CategoryModel.find_by_name(request_data["name"])
            cat.name = request_data["newname"]
            cat.url = request_data["url"]
            cat.parentCategory = request_data["parentCategory"]
            cat.modify_to_db()
        except:
            return {"message": "category doesn't exist"}
        return {"message": "category changed"}

