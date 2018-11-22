from flask import Blueprint
from flask_restful import Api, Resource
from app.api.v2.views.user_views import UserRegistration, UserLogin
from app.api.v2.views.parcel_views import OrderCreation

version2 = Blueprint('v2', __name__, url_prefix='/api/v2')

api = Api(version2)

api.add_resource(UserRegistration, '/auth/signup', strict_slashes=False)
api.add_resource(UserLogin, '/fetch', strict_slashes=False)
api.add_resource(OrderCreation, '/parcels', strict_slashes=False)
