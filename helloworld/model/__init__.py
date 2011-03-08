"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base

from helloworld.model import meta

_Base = declarative_base()

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    meta.Session.configure(bind=engine)
    meta.engine = engine


class Person(_Base):
    __tablename__ = "persons"

    id = sa.Column(sa.types.Integer, primary_key=True)
    name = sa.Column(sa.types.String(100))
    email = sa.Column(sa.types.String(100))