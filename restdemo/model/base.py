from restdemo import db

class Base(db.Model):

    __abstract__ = True # 不是 table  ，讓系統不會認為此事table
    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
