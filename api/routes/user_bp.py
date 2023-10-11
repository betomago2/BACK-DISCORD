from flask import Blueprint

from ..controllers.users_controller import UserController

user_bp = Blueprint('user_bp', __name__) #users

user_bp.route('/login', methods=['POST'])(UserController.login)
user_bp.route('/profile', methods=['GET'])(UserController.show_profile)
# user_bp.route('/<string:username>', methods=['GET'])(UserController.get)
user_bp.route('/logout', methods=['GET'])(UserController.logout)
user_bp.route("/register", methods=['POST'])(UserController.register)
user_bp.route("/update", methods=['PUT'])(UserController.update)
user_bp.route('/server_user', methods=['GET'])(UserController.get_servers_user)

#endpoints normales
user_bp.route('/<int:id>', methods=["GET"])(UserController.getID)
user_bp.route('/', )(UserController.getAll)
user_bp.route('/registrar', )(UserController.registrar)
user_bp.route('/actualizar/<string:username>', methods=["PUT"])(UserController.actualizar)
user_bp.route('/eliminar/<string:username>', methods=["DELETE"])(UserController.eliminar)