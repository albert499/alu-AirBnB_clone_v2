#!/usr/bin/python3
"""This module defines a class User."""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
import models


class User(BaseModel, Base):
    """This class defines a user by various attributes."""

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    if models.storage_type == "db":
        places = relationship("Place", backref="user", cascade="delete")
        reviews = relationship("Review", backref="user", cascade="delete")
    else:
        places = []  # FIXME: handle logic
        reviews = []  # FIXME: handle logic

    def __init__(self, *args, **kwargs):
        """User init method."""
        filtered_kwargs = {k: v for k, v in kwargs.items()
                           if hasattr(self, k) or k == "id"}
        super().__init__(*args, **filtered_kwargs)
        self.email = kwargs.get("email", None)
        self.password = kwargs.get("password", None)
        self.first_name = kwargs.get("first_name", None)
        self.last_name = kwargs.get("last_name", None)
