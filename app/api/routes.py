from flask import jsonify

from app.api import api


@api.get('/demo')
def demo():
    return jsonify({'message': 'Success'})
