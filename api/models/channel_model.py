from ..database import DatabaseConnection
from .server_model import Server

class Channel:
    """Clase que representa un canal."""
    
    _keys = ('channel_id', 'name', 'description', 'server_id')

    def __init__(self, **kwargs):
        self.channel_id = kwargs.get('channel_id')
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.server_id = kwargs.get('server_id')

    # def serialize(self):
    #     return {
    #         'channel_id': self.channel_id,
    #         'name': self.name,
    #         'description': self.description,
    #         'server_id': Server.get_servers(Server(server_id=self.server_id)).serialize() if self.server_id else None
    #     }

    def serialize(self):
         return {
             'channel_id': self.channel_id,
             'name': self.name,
             'description': self.description,
             'server_id': self.server_id
         }

    @classmethod
    def create(cls, channel):
        query = "INSERT INTO discord.channels (name, description, server_id) VALUES (%s, %s, %s)"
        params = (channel.name, channel.description, channel.server_id)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def delete(cls, channel):
        query = "DELETE FROM discord.channels WHERE channel_id = %s"
        params = (channel.channel_id,)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get(cls, channel=None):
        print("VINO POR GET - CHANNEL MODEL")
        try:
            if channel and channel.channel_id:
                print("GET 1")
                query = "SELECT channel_id, name, description, server_id FROM discord.channels WHERE channel_id = %s"
                params = (channel.channel_id,)
                result = DatabaseConnection.fetch_one(query, params)
                DatabaseConnection.close_connection()
                return cls(**dict(zip(cls._keys, result))) if result else None
        
            elif channel and channel.server_id:
                print("GET 2")
                query = "SELECT channel_id, name, description, server_id FROM discord.channels WHERE server_id = %s"
                params = (channel.server_id,)
                results = DatabaseConnection.fetch_all(query, params=params)
                channels = []
                if results is not None:
                    for result in results:
                        print("CHANNEL: ", result)
                        channels.append(Channel(
                         channel_id=result[0],
                            name=result[1],
                            description=result[2],
                            server_id=result[3]
                        ))
                DatabaseConnection.close_connection()
                return channels
        
            else:
                query = "SELECT channel_id, name, description, server_id FROM discord.channels"
                results = DatabaseConnection.fetch_all(query)
                DatabaseConnection.close_connection()
                return [cls(**dict(zip(cls._keys, row))) for row in results]
        except Exception as e:
            raise Exception(e)