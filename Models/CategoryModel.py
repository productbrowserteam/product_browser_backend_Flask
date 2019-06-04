from db import db

class CategoryModel(db.Model):

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    parentCategory = db.Column(db.String)
    url = db.Column(db.String)

    def __init__(self, name, url, parentCategory=""):
        self.name = name
        self.url = url
        self.parentCategory = parentCategory

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def modify_to_db(self):
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_url(cls, url):
        return cls.query.filter_by(url=url).first()

    @classmethod
    def find_by_parentCategory(cls, parentCategory):
        return cls.query.filter_by(parentCategory=parentCategory)

    @classmethod
    def find_by_parentCategoryFirst(cls, parentCategory):
        return cls.query.filter_by(parentCategory=parentCategory).first()

