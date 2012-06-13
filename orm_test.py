import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

print(sqlalchemy.__version__)

#engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
engine = sqlalchemy.create_engine('sqlite:///test', echo=True)
engine.execute("select 1").scalar()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

#    def __repr__(self):
#        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)
        
Base.metadata.create_all(engine)

ed_user = User('ed', 'Ed Jones', 'edspassword')
u1 = User(name='ed', fullname='Ed Jones', password='foobar')

Session = sessionmaker(bind=engine)
# Session = sessionmaker()
# Session.configure(bind=engine)
session = Session()
print(ed_user.id)
#session.add(ed_user)
#session.commit()


our_user = session.query(User).filter_by(name='ed').first()
print(our_user.id, our_user.fullname, our_user.password);
print(ed_user is our_user)
print(ed_user.id)