import sqlalchemy as db
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey
meta = MetaData()


# create engine
engine = db.create_engine(
    "postgresql://postgres:Caustic69@localhost:5432/SM", echo=True)

# create tables
customers = Table(
    'customers', meta,
    Column('customerId', Integer, primary_key=True),
    Column('firstName', String, nullable=False),
    Column('lastName', String, nullable=False),
    Column('phoneNo', Integer, nullable=False),
    Column('email', String),
    Column('notes', String),
)

products = Table(
    'products', meta,
    Column('productId', Integer, primary_key=True),
    Column('productName', String, nullable=False),
    Column('productDesc', String, nullable=False),
    Column('userId', Integer, ForeignKey('users.userId'), nullable=False),
    Column('productImg', String),
    Column('productVid', String),

)

users = Table(
    'users', meta,
    Column('userId', Integer, primary_key=True),
    Column('firstName', String, nullable=False),
    Column('secondName', String, nullable=False),
    Column('email', String, nullable=False),
    Column('password', String, nullable=False),
)

roles = Table(
    'roles', meta,
    Column('roleId', Integer, primary_key=True),
    Column('roleName', String, unique=True)
)

# Create all defined table objects
meta.create_all(engine)

'''
#insert records to the table
user1 = users.insert().values(userId=1, firstName='Victor', secondName='Micheni',
                            email='victormichenim@gmail.com', password='caustic')
user2 = users.insert().values(userId=2, firstName='James', secondName='Gichuki',
                            email='jamesnyokabi@gmail.com', password='jamo')

engine.execute(user1)
engine.execute(user2)
'''
