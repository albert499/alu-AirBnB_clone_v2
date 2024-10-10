#!/usr/bin/python3
"""Module for the Amenity model in HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class Amenity(BaseModel, Base):
    """
    attributes:
        name: (str) name of amenity
        place_amenity: (list) list of amenities associated with a place
    """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    if models.storage_type == "db":
        place_amenities = relationship("Place", secondary="place_amenity",
                back_populates="amenities")
    else:
        place_amenities = []  # FIXME: handle logic

    def __init__(self, *args, **kwargs):
        """Init method."""
        filtered_kwargs = {k: v for k, v in kwargs.items()
                           if hasattr(self, k) or k == "id"}
        super().__init__(*args, **filtered_kwargs)
        self.name = kwargs.get("name", None)
        self.place_id = kwargs.get("place_id", None)
