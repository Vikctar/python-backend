from app import ma


class EmptySchema(ma.Schema):
    pass


class NewTripSchema(ma.Schema):
    """Schema defining the attributes when creating a new trip."""
    driver_id = ma.Integer()
    vehicle_id = ma.Integer()
    customer_id = ma.Integer()
    address = ma.String()
    cargo_tonnage = ma.Float()
    address_type = ma.String()
    done_by_user_id = ma.Integer()


class TokenSchema(ma.Schema):
    """Schema defining the attributes of a token"""
    token = ma.String()
