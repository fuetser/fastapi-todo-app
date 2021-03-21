import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String, unique=True)
    password = sa.Column(sa.String)


class TODO(Base):
    __tablename__ = "todos"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)
    description = sa.Column(sa.String, nullable=True)
    owner_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    user = relationship('User', backref='todos')
