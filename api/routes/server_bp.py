from flask import Blueprint
from ..controllers.server_controller import ServerController

server_bp = Blueprint('server_bp',__name__)

server_bp.route('/', methods = ['POST'])(ServerController.create_server)
server_bp.route('/', methods = ['GET'])(ServerController.get_servers)
server_bp.route('/serversuser', methods = ['GET'])(ServerController.get_servers_user)