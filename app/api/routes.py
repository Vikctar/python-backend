from apifairy import body, other_responses
from flask import jsonify, abort

from app.api import api
from app.models import Trip
from app.schemas import NewTripSchema

new_trip_schema = NewTripSchema()


@api.get('/demo')
def demo():
    return jsonify({'message': 'Success'})


@api.post('record-trip')
@body(new_trip_schema)
@other_responses({201: 'Created', 403: 'Forbidden'})
def record_trip(kwargs):
    print(kwargs)
    driver_id = kwargs.get('driver_id')
    vehicle_id = kwargs.get('vehicle_id')
    customer_id = kwargs.get('customer_id')
    address = kwargs.get('address')
    cargo_tonnage = kwargs.get('cargo_tonnage')
    done_by_user_id = kwargs.get('done_by_user_id')
    address_type = kwargs.get('address_type')
    try:
        trip = Trip(
            driver_id=driver_id,
            vehicle_id=vehicle_id,
            customer_id=customer_id,
            address=address,
            cargo_tonnage=cargo_tonnage,
            address_type=address_type,
            done_by_user_id=done_by_user_id
        )
        trip.insert()
        return jsonify({
            'description': 'Trip Recorded'
        }), 201
    except:
        abort(422)
