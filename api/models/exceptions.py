from flask import jsonify

class CustomException(Exception):

    def __init__(self, status_code, name = "Custom Error", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response


class UserNotFound(Exception):
    def __init__(self, status_code=404, name = "User Not Found/Exists", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response

class UsernameExists(Exception):
    def __init__(self, status_code, name = "User Exists", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = 404

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response
    
    def serialize(self):
        return {    "status_code" : self.status_code,
                    "name": self.name,
                    "description": self.description,
        }
    
class DataNotComplete:
    def __init__(self, status_code, name = "User Not Found/Exists", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = 400

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response

class ServerError(CustomException):

    def __init__(self, description = "Error en la base de datos"):
        super().__init__(500, "Server Error", description)
        self.description = description
        self.status_code = 500

class BadRequest(CustomException):

    def __init__(self, description = 'Solcitud inválida'):
        super().__init__(400, name = "Bad Request", description = description)
    
class NotFound(CustomException):

    def __init__(self, description = 'Recurso no encontrado'):
        super().__init__(404, name = "Not Found", description = description)