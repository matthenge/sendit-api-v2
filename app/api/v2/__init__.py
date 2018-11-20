from flask import Blueprint
from flask_restful import Api, Resource
from app.api.v2.views.views import AllOrders, CreateOrder, ReturnOneOrder 
from app.api.v2.views.views import CancelOrder, UserParcels, CreateUser, ReturnAllUsers, ReturnUser

version2 = Blueprint('v2', __name__, url_prefix='/api/v2')

api = Api(version2)

api.add_resource(CreateOrder, '/parcels', strict_slashes=False)
api.add_resource(AllOrders, '/parcels', strict_slashes=False)
api.add_resource(ReturnOneOrder, '/parcels/<string:order_id>', strict_slashes=False)
api.add_resource(CancelOrder, '/parcels/<string:order_id>', strict_slashes=False)
api.add_resource(UserParcels, '/users/<string:user_id>/parcels', strict_slashes=False)
api.add_resource(CreateUser, '/users', strict_slashes=False)
api.add_resource(ReturnAllUsers, '/users', strict_slashes=False)
api.add_resource(ReturnUser, '/users/<string:username>', strict_slashes=False)
