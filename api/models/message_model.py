from ..database import DatabaseConnection
from .users_model import User
from .exceptions import ServerError

class Message:
    """Clase que representa un mensaje."""
    
    def __init__(self, **kwargs):
        self.message_id = kwargs.get('message_id')
        self.message = kwargs.get('message')
        self.date_time = kwargs.get('date_time')
        self.user_id = kwargs.get('user_id')
        self.channel_id = kwargs.get('channel_id')
    
    def serialize(self):
        return {
            "message_id": self.message_id,
            "message": self.message,
            "date_time": self.date_time, 
            "user_id": self.user_id,
            "channel_id": self.channel_id
        }

    def serialize2(self):
        return {
            "message_id": self.message_id,
            "message": self.message,
            "date_time": self.date_time, 
            "user_id": User.get_id_user(User(user_id=self.user_id)).serialize() if self.user_id else None,
            "channel_id": self.channel_id
        }

    @classmethod
    def get_message(cls, message):
        query = """SELECT message_id, message, date_time, user_id, channel_id FROM discord.messages WHERE message_id = %(message_id)s"""
        params = message.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return Message(
                message_id = result[0],
                message = result[1],
                date_time = result[2],
                user_id = result[3],
                channel_id = result[4],
            )
        return None
    
    @classmethod
    def get_messages(cls, channel=None):
        try:
            if channel:
                query = """SELECT message_id, message, date_time, user_id, channel_id FROM discord.messages WHERE channel_id = %s"""
                params = (channel.channel_id,)
                results = DatabaseConnection.fetch_all(query, params=params)
                message_list = []
                for result in results:
                    message_list.append(Message(
                        message_id = result[0],
                        message = result[1],
                        date_time = result[2],
                        user_id = result[3],
                        channel_id = result[4]
                    ))
            return message_list
        except Exception as e:
            raise Exception(e)

    @classmethod
    def create_message(cls, message):
        query = """INSERT INTO discord.messages (message_id, message, user_id, channel_id)
        VALUES (%s, %s, %s, %s)"""
        params = message.message_id, message.message, message.user_id, message.channel_id
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update_message(cls, message):
        pass

    @classmethod
    def delete_message(cls, message):
        query = """DELETE FROM discord.messages WHERE message_id = %s"""
        params = message.message_id,
        cursor = DatabaseConnection.execute_query(query, params=params)

        if cursor.rowcount == 0:
            raise ServerError("No se pudo eliminar al mensaje")
        else:
            return {"message": "Mensaje eliminado con exito"}