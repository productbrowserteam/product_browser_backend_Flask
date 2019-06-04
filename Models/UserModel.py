from db import db


class UserModel(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String)
    password = db.Column(db.String)


    def __init__(self, login, password):
        self.login = login
        self.password = password

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
    def find_by_name(cls, login):
        return cls.query.filter_by(login=login).first()