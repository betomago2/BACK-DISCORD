from flask import Blueprint
from ..models.exceptions import UserNotFound, UsernameExists, BadRequest, NotFound

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(UserNotFound)
def handle_user_not_found(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(UsernameExists)
def handle_username_exists(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(BadRequest)
def handle_bad_request(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(NotFound)
def handle_not_found(error):
    return error.get_response(), error.status_code