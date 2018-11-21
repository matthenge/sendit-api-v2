from flask import Blueprint
from flask_restful import Api, Resource
from app.api.v2.views.user_views import UserRegistration

version2 = Blueprint('v2', __name__, url_prefix='/api/v2')

api = Api(version2)

api.add_resource(UserRegistration, '/auth/signup', strict_slashes=False)
