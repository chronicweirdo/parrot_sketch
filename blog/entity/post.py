'''
Created on Jun 19, 2012

@author: silviu
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Date
import sqlalchemy

Base = declarative_base()

class Post(Base):
    '''
    classdocs
    '''
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    date = Column(Date)

    def __init__(self, text, date):
        '''
        Constructor
        '''
        self.text = text
        self.date = date

engine = sqlalchemy.create_engine('sqlite:///blog', echo=True)        
Base.metadata.create_all(engine)

def getSession():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
        
def save(post):
    session = getSession()
    session.add(post)
    session.commit()
    
def loadAll():
    session = getSession()
    return session.query(Post)

def loadFirst():
    session = getSession()
    return session.query(Post).first()