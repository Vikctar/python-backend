from datetime import datetime
from enum import Enum

from app import db


class AddressType(Enum):
    PICKUP_POINT = 'pickup_point'
    DROP_OFF_POINT = 'drop_off_point'


class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, nullable=False)
    vehicle_id = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(50))
    cargo_tonnage = db.Column(db.Float)
    address_type = db.Column(db.Enum(AddressType))
    done_by_user_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)

    def insert(self):
        db.session.add(self)
        db.session.commit()
