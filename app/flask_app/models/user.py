from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "brixtronix"
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.email=data['email']
        self.password=data['password']
        self.local=data['local']
        self.phone=data['phone']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        print(results)
        return cls(results[0])
    
    @classmethod
    def get_by_email(cls, data):
        query="SELECT * FROM users WHERE email=%(email)s;"
        results=connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1 :
            return False
        return cls(results[0])
    
