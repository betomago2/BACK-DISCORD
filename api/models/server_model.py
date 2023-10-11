from ..database import DatabaseConnection

class Server:
    """Clase que representa un servidor."""

    def __init__(self, **kwargs):
        self.server_id = kwargs.get('server_id')
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.admin_user = kwargs.get('admin_user')

    def __str__(self):
        return f"Server: {self.name}"
    
    def serialize(self):
        return {
            "server_id": self.server_id,
            "name": self.name,
            "description": self.description, 
            "admin_user": self.admin_user,
        }

    @classmethod
    def create_server(cls, server):
        """Crea un servidor."""
        try:
            sql = """INSERT INTO discord.servers (name, description, admin_user) VALUES (%(name)s, %(description)s, %(admin_user)s);"""
            params = server.__dict__
            DatabaseConnection.execute_query(sql, params=params)

            return {"message": "Servidor Registrado con exito!"}, 201
        except Exception as e:
            raise Exception(e)

    @classmethod
    def create_us(cls, user_admin):
        """Crea registro que relaciona un servidor con un usuario."""
        try:
            sql = """INSERT INTO discord.server_user (server_id, user_id) SELECT MAX(servers.server_id), %s FROM discord.servers;"""
            params = user_admin,
            DatabaseConnection.execute_query(sql, params=params)  
        except Exception as e:
            raise Exception(e)

    @classmethod
    def delete_server(cls, server):
        query = "DELETE FROM discord.servers WHERE server_id = %s"
        params = (server.server_id,)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get_servers(self, user=None):
        """Funcion que retorna todos los servidores o los servidores de un usuario en especidifco en formato JSON"""
        try:
            # Get servidores de un usuario
            if user and user.username:
                print(f"GET SERVERS BY USER {user.username}")
                query="""
                SELECT
                    servers.server_id, servers.name, servers.description, servers.admin_user
                FROM
                    discord.servers
                JOIN
                    discord.server_user
                ON
                    server_user.server_id = servers.server_id 
                JOIN
                    discord.users
                ON
                    users.user_id = server_user.user_id
                WHERE
                    users.username = %(username)s;"""
                params = user.__dict__
                results = DatabaseConnection.fetch_all(query, params=params)
                DatabaseConnection.close_connection()
                servers = []
                if results is not None:
                    for result in results:
                        servers.append(Server(
                            server_id=result[0],
                            name=result[1],
                            description=result[2],
                            admin_user=result[3]
                        ))
                return servers
            # Get servidores
            else:
                print("GET SERVERS")
                query = "SELECT server_id, name, description, admin_user FROM discord.servers"
                results = DatabaseConnection.fetch_all(query)
                DatabaseConnection.close_connection()
                servers = []
                if results is not None:
                    for result in results:
                        servers.append(Server(
                            server_id=result[0],
                            name=result[1],
                            description=result[2],
                            admin_user=result[3]
                        ))
                return servers
        except Exception as e:
            raise Exception(e)

    # @classmethod
    # def get_server_user(cls, user = None):
    #     """Funcion que retorna los servidores de un usuario de la base de datos."""
    #     try:
    #         if user and user.user_id:   
                
    #             params = user.__dict__
    #             results = DatabaseConnection.fetch_all(query, params=params)
    #             servers = []
    #             if results is not None:
    #                 for result in results:
    #                     servers.append(Server(
    #                         server_id=result[0],
    #                         name=result[1],
    #                         description=result[2],
    #                         admin_user=result[3]
    #                     ))
    #             DatabaseConnection.close_connection()
    #             return servers
    #     except Exception as e:
    #         raise Exception(e)