from flask import Blueprint
from ..controllers.channel_controller import ChannelController

channel_bp = Blueprint('channel_bp', __name__)

channel_bp.route('/<int:server_id>', methods=['GET'])(ChannelController.get)
#channel_bp.route('/<int:channel_id>', methods=['GET'])(ChannelController.get_by_id)
channel_bp.route('/', methods=['POST'])(ChannelController.create)
channel_bp.route('/<int:channel_id>', methods=['DELETE'])(ChannelController.delete)