from db import db


class ProductModel(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    description = db.Column(db.String)
    subcategory = db.Column(db.String)
    subcategoryUrl = db.Column(db.String)


    def __init__(self, name, url, description, subcategory, subcategoryUrl):
        self.name = name
        self.url = url
        self.description = description
        self.subcategory = subcategory
        self.subcategoryUrl = subcategoryUrl

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def modify_to_db(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_subcategory(cls, subcat):
        return cls.query.filter_by(subcategory=subcat)