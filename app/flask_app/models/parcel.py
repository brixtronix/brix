from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Parcel:
    db="brixtronix"
    def __init__(self,data):
        self.id = data['id']
        self.parcel = data['parcel']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = data['user_id']
        self.poster=None


    @classmethod
    def save_parcel(cls,data):
        query="INSERT INTO parcels (parcel,user_id,created_at,updated_at) VALUES(%(parcel)s,%(user_id)s,NOW(),NOW());"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all_parcels(cls):
        query="SELECT * FROM parcels JOIN users ON parcels.user_id=users.id;"
        results=connectToMySQL(cls.db).query_db(query)
        all_parcels=[]
        for row in results:
            posting_user=User({
                "id": row['id'],
                "name": row['name'],
                "email": row['email'],
                "password": row['password'],
                "local": row['local'],
                "phone": row['phone'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            })
            new_parcel=Parcel({
                "id": row['id'],
                "parcel": row['parcel'],
                "user_id": row['user_id'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            })
            new_parcel.poster=posting_user
            all_parcels.append(new_parcel)
        return all_parcels
    
    @classmethod
    def delete_parcel(cls,data):
        query="DELETE FROM parcels WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @staticmethod
    def validate_parcel(parcels):
        is_valid=True
        if parcels["parcel"]<=0:
            flash("Can't be blank")
            is_valid=False
        return is_valid