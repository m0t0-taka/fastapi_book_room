import datetime
from pydantic import BaseModel, Field


class Booking(BaseModel):
    booking_id: int
    user_id: int
    room_id: int
    booked_num: int
    start_at: datetime.datetime
    end_at: datetime.datetime

    # dictでなくORMに対応したClassにする
    class Config:
        orm_mode = True


class User(BaseModel):
    user_id: int
    user_name: str = Field(max_length=12)

    class Config:
        orm_mode = True


class Room(BaseModel):
    room_id: int
    room_name: str = Field(max_length=12)
    capacity: int

    class Config:
        orm_mode = True
