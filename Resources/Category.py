from flask_restful import Resource, reqparse
from Models.CategoryModel import CategoryModel
import json


class Category(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="name required")
    parser.add_argument("url", type=str, required=True, help="name required")
    parser.add_argument("parentCategory", type=str, required=False)


    def get(self):
        cat = CategoryModel.query.all()
        catlist = []
        for category in cat:
            catlist.append({"id": category.id, "name": category.name, "url": category.url, "parent": category.parentCategory})
        return {"list": catlist}


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


    def get(self):

        def getData(data, itter, parent=""):
            category = "cat" + str(itter)
            for n in data[category]:
                cat = CategoryModel(n["name"], n["url"], parent)
                cat.save_to_db()
                try:
                    getData(n, itter + 1, n["name"])
                except:
                    pass

        with open("Cat.txt", "br") as json_file:
            data = json.load(json_file)
            getData(data, 0)
        return {"message": "categories imported"}

class CategoryJson(Resource):

    def get(self):
        result = {"header": "Categories"}
        def categoryhelper(parent, series):
            data = []
            cat = CategoryModel.find_by_parentCategory(parent)
            if CategoryModel.find_by_parentCategoryFirst(parent):
                for c in cat:
                    category = {"name": c.name, "url": c.url,}
                    try:
                        catkey = "cat{}".format(series)
                        categories = categoryhelper(c.name, series+1)
                        if categories != None:
                            category[catkey] = categories
                    except:
                        pass
                    data.append(category)
                return data

        result["cat0"] = categoryhelper("", 1)
        return result