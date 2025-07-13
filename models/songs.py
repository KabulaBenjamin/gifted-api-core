# models/songs.py

from pydantic import BaseModel, Field, constr
from typing import Optional

class SongCreate(BaseModel):
    title: constr(min_length=1)
    artist: Optional[constr(min_length=1)] = None
    album: Optional[constr(min_length=1)] = None
    duration_seconds: Optional[int] = Field(None, gt=0)

class SongUpdate(BaseModel):
    title: Optional[constr(min_length=1)]
    artist: Optional[constr(min_length=1)]
    album: Optional[constr(min_length=1)]
    duration_seconds: Optional[int] = Field(None, gt=0)