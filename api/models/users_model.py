from ..database import DatabaseConnection
from ..models.exceptions import UserNotFound, UsernameExists, DataNotComplete

class User:
    """Clase que representa un Usuario."""

    def __init__(self):
        """esta vacio"""

    def __init__(self,**kwargs):
        self.user_id = kwargs.get('user_id')
        self.email = kwargs.get('email')
        self.username = kwargs.get('username')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.password = kwargs.get('password')
        self.birthdate = kwargs.get('birthdate')
        self.avatar=kwargs.get("avatar")

    def serialize(self):
        return {
            "user_id": self.user_id,
            "email": self.email,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password,
            "birthdate": self.birthdate,
            "avatar": self.avatar
        }
    
    @classmethod
    def is_registered(cls, user):
        query = """SELECT user_id FROM discord.users 
        WHERE username = %(username)s and password = %(password)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False
    
    @classmethod
    def get(cls, user):
        print("GET - USERS MODEL", user.username)
        try:
            if user.exists(user.username):
                sql="""SELECT user_id, email, username, first_name, last_name, password, birthdate, avatar FROM discord.users
                WHERE users.username=%(username)s"""
                params = user.__dict__
                result = DatabaseConnection.fetch_one(sql, params=params)

                if result is not None:
                    return cls(
                        user_id = result[0],
                        email = result[1],
                        username = result[2],  
                        first_name = result[3],
                        last_name =result[4],
                        password = result[5],
                        birthdate = result[6],
                        avatar = result[7]
                    )
                DatabaseConnection.close_connection()
                return None
        except Exception as e:
            raise Exception(e)
            

    @classmethod
    def exists(self, username):
        print("EXISTS - USERS MODEL", username)
        try:
            sql="SELECT username FROM discord.users "
            results= DatabaseConnection.fetch_all(sql)

            existe=False
            for n in results:
                for x in n:
                    if x.lower()==username.lower():
                        existe=True  
            DatabaseConnection.close_connection()
            return existe
        except Exception as e:
            raise Exception(e)

    @classmethod
    def createUser(cls,user):
        if user.exists(user.username):
            return None
        else: 
            params= user.__dict__
            sql="""INSERT INTO discord.users(email,username,first_name,last_name,password,birthdate,avatar) 
                VALUES(%(email)s,%(username)s,%(first_name)s,%(last_name)s,%(password)s,%(birthdate)s,%(avatar)s)"""
            DatabaseConnection.execute_query(sql, params=params)
            return {"message":"User creado con exito!"},200

    @classmethod
    def updateUser(cls, user):
        # birthdate = %(birthdate)s,
        user=user.serialize()
        if user["birthdate"] is not None:
            query ="""
            UPDATE
                discord.users
            SET
                email = %(email)s,
                username = %(username)s,
                first_name = %(first_name)s,
                last_name = %(last_name)s,
                birthdate = %(birthdate)s,
                avatar = %(avatar)s
            WHERE
                user_id = %(user_id)s
            """
        else:
            query ="""
            UPDATE
                discord.users
            SET
                email = %(email)s,
                username = %(username)s,
                first_name = %(first_name)s,
                last_name = %(last_name)s,
                avatar = %(avatar)s
            WHERE
                user_id = %(user_id)s
            """
        
        params = user
        # print("cumple ",user.birthdate)
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def get_id_user(cls, user = None):
        """"Retorna el usuario con el ID pasado por parámetro. (Para chat.js)"""
        if user and user.user_id:
            query = "SELECT * FROM discord.users WHERE user_id = %s"
            params = (user.user_id,)
            result = DatabaseConnection.fetch_one(query, params)
            if result is not None:
                return cls(
                        user_id = result[0],
                        email = result[1],
                        username = result[2],  
                        first_name = result[3],
                        last_name =result[4],
                        password = result[5],
                        birthdate = result[6],
                        avatar = result[7]
                    )
            return None

    #metodos sencillos part2
    def getBy_id(self,user):
        sql="SELECT * FROM discord.users WHERE user_id= %s"
        params=user.user_id,
        results= DatabaseConnection.fetch_one(sql,params=params)
        print(results)
        if results is not None:
            return User(
                user_id=results[0],
                email=results[1],
                username=results[2],
                password=results[3],
                first_name=results[4],
                last_name=results[5],
                birthdate=results[6],
                avatar=results[7]
            ).serialize()
        else:
            raise UserNotFound("Usuario no encontrado")

    @classmethod
    def getAll(cls):
        sql="SELECT * FROM discord.users"
        results= DatabaseConnection.fetch_all(sql)
        users = []
        for x in results:
            user = User(user_id=x[0],
                        email =x[1],
                        username=x[2],
                        password=x[3],
                        first_name=x[4],
                        last_name=x[5],
                        birthdate=x[6],
                        avatar=x[7]).serialize()
            users.append(user)
        return users
    
    @classmethod
    def registrar(cls,user):
        if user.exists(user.username):
            raise UsernameExists("Este nombre de usuario ya existe")
        else: 
            params= user.__dict__
            if user.email!="" and user.password!="" and user.username!="":
                if user.birthdate=="":
                    sql="""INSERT INTO discord.users(email,username,first_name,last_name,password) 
                    VALUES(%(email)s,%(username)s,%(first_name)s,%(last_name)s,%(password)s)"""
                else:

                    sql="""INSERT INTO discord.users(email,username,first_name,last_name,password,birthdate) 
                    VALUES(%(email)s,%(username)s,%(first_name)s,%(last_name)s,%(password)s,%(birthdate)s)"""
                DatabaseConnection.execute_query(sql, params=params)
                return user.serialize()
            else:
                raise DataNotComplete(description="Faltan completar alguno de estos campos --> email/password/username")
    
    @classmethod       
    def actualizar(cls,user1,user):

        # print("->",type(user1))
        usuario= User.get(user1)
        # print("desde modelo..metodo actualizar-->",usuario)
        if usuario is not None:
            #actualizamos datos
            query="UPDATE discord.users SET "
            if user.email!=None:
                consulta=query + "email=%s WHERE username=%s"
                params= user.email, user1.username 
                DatabaseConnection.execute_query(consulta,params=params)
            if user.username!=None:
                consulta=query + "username=%s WHERE username=%s"
                params= user.username, user1.username 
                DatabaseConnection.execute_query(consulta,params=params)
            if user.first_name!=None:
                consulta=query + "first_name=%s WHERE username=%s"
                params= user.first_name, user1.username 
                DatabaseConnection.execute_query(consulta,params=params)
            if user.last_name!=None:
                consulta=query + "last_name=%s WHERE username=%s"
                params= user.last_name, user1.username 
                DatabaseConnection.execute_query(consulta,params=params)
            if user.password!=None:
                consulta=query + "password=%s WHERE username=%s"
                params= user.password, user1.username 
                DatabaseConnection.execute_query(consulta,params=params)    
            if user.birthdate!=None:
                consulta=query + "birthdate=%s WHERE username=%s"
                params= user.birthdate, user1.username 
                DatabaseConnection.execute_query(consulta,params=params)

            return {"message":f"Los datos del usuario {user1.username} fueron modificados con exito"},200
        else:
            raise UserNotFound(description="usuario no encontrado")
        
    
    @classmethod
    def eliminar(cls,username):
        #DELETE FROM table_name WHERE condition;
        if User.exists(username):
            query="DELETE FROM discord.users WHERE username=%s"
            DatabaseConnection.execute_query(query,params=(username,))
            return {"message":"Usuario eliminado"}
        else:
            raise UserNotFound(description="El usuario no encontrado")