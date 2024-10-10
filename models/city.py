#!/usr/bin/python3
"""City Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class City(BaseModel, Base):
    """The city class, contains state ID and name."""

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    if models.storage_type == "db":
        places = relationship("Place", backref="cities", cascade="delete")
    else:
        places = []  # FIXME: handle logic

    def __init__(self, *args, **kwargs):
        """Init method."""
        filtered_kwargs = {k: v for k, v in kwargs.items()
                           if hasattr(self, k) or k == "id"}
        super().__init__(*args, **filtered_kwargs)
        self.name = kwargs.get("name", None)
        self.state_id = kwargs.get("state_id", None)
