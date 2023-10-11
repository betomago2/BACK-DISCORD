from ..models.channel_model import Channel
from flask import request

from ..models.exceptions import NotFound, BadRequest

class ChannelController:
    """Clase de controlador de canales."""

    @classmethod
    def get(cls, server_id):
        print("VINO POR GET - CHANNEL CONTROLLER")
        channels = []
        # Get canales por servidor
        channel_obj = Channel(server_id=server_id)
        channels = Channel.get(channel_obj)
        print("Salio")
        print("CHANNELS RETORNADO: ", [channel.serialize() for channel in channels])
        return [channel.serialize() for channel in channels], 200

    @classmethod
    def get_by_id(cls, channel_id):
        if channel_id <= 0:
            raise BadRequest("El id de la tarea debe ser mayor a 0") 
        channel_obj = Channel(channel_id=channel_id)
        channel = Channel.get(channel_obj)
        if channel:
            return channel.serialize(), 200
        raise NotFound("Tarea no encontrada")

    @classmethod
    def create(cls):
        data = request.json
        channel_obj = Channel(
            name=data.get('name'),
            description=data.get('description'),
            server_id=data.get('server_id')
            )
        Channel.create(channel_obj)
        return {'message': 'Canal creado con éxito'}, 201

    @classmethod
    def delete(cls, channel_id):
        channel_obj = Channel(channel_id=channel_id)
        Channel.delete(channel_obj)
        return {'message': 'Canal eliminado con éxito'}, 200