# models/events.py

from pydantic import BaseModel, Field, root_validator, constr
from typing import Optional
from datetime import datetime

class EventCreate(BaseModel):
    name: constr(min_length=1)
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime
    location: Optional[str] = None

    @root_validator
    def check_times(cls, values):
        start, end = values.get('start_time'), values.get('end_time')
        if end <= start:
            raise ValueError('end_time must be after start_time')
        return values

class EventUpdate(BaseModel):
    name: Optional[constr(min_length=1)]
    description: Optional[str]
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    location: Optional[str]

    @root_validator
    def check_times(cls, values):
        start, end = values.get('start_time'), values.get('end_time')
        if start and end and end <= start:
            raise ValueError('end_time must be after start_time')
        return values