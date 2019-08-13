from flask_login import UserMixin
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.common import Common


class User(UserMixin):
    pass


class UserDao(db.Model):
    __tablename__ = 'app_user'

    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    salt = db.Column(db.String(20), nullable=False)
    # status状态，0-停用，1-启用
    status = db.Column(db.Integer, nullable=False)
    # 错误登录次数
    errLoginNum = db.Column(db.Integer, nullable=True)
    # 最后一次错误登录时间
    errLoginTime = db.Column(db.DateTime, nullable=True)

    def __init__(self, user_id, user_name, user_password):
        self.id = user_id
        self.name = user_name
        self.salt = Common.genSalt(10)
        self.password = Common.encryptedPsw(user_password, self.salt)
        self.status = 1
        self.errLoginNum = 0

    def __str__(self):
        return "Users(id='%s')" % self.id

    def getAll(self):
        return self.query.all()

    def get_byId(self, id):
        return self.query.filter_by(id=id).first()

    def get_byName(self, name):
        return self.query.filter_by(name=name).all()

    def add(self, user):
        db.session.add(user)
        return session_commit()

    def update(self):
        return session_commit()

    def delete(self, id):
        # deleteRow = self.query.filter_by(id=id).delete()
        return session_commit()


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason
