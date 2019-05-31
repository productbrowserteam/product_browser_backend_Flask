from flask_restful import Resource, reqparse
from Models.CategoryModel import CategoryModel


class PBlist(Resource):

    def get(self):
        pblist = CategoryModel.query.all()
        catlist = []
        for category in pblist:
            catlist.append({"id": category.id, "name": category.name, "url": category.url, "parent": category.parentCategory})
        return {"list": catlist}

