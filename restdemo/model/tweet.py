from restdemo import db
from sqlalchemy import ForeignKey
from datetime import datetime
from restdemo.model.base import Base

class Tweet(Base):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    body = db.Column(db.String(140))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
 
    def __repr__(self):
        return "user_id ={}, tweet ={}".format(
            self.user_id,
            self.body
        )
    # # TODO 抽象化 CRUD db 操作=>移到base.py
    # def add(self):
    #     db.session.add(self)
    #     db.session.commit()

        
    def as_dict(self):
        """子類重寫父類"""
        t = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        t['created_at'] = t['created_at'].isoformat()
        return t