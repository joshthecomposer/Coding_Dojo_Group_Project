from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash,session
from flask_app.models import user

DB='et'

class Timer:
    def __init__(self, data ):
        self.id=data['id']
        self.name=data['name']
        self.excercise_time=data['excercise_time']
        self.rest_time=data['rest_time']
        self.sets=data['sets']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
        self.user=None
    @staticmethod
    def is_valid(data):
        valid=True
        flash_string='is required'
        if len(data['name'])<1:
            flash('name '+ flash_string,'timer')
            valid=False
        if len(data['excercise_time'])<1:
            flash('excercise_time '+flash_string,'timer')
            valid=False
        if len(data['rest_time'])<1:
            flash('rest_time '+flash_string,'timer')
            valid=False
        if len(data['sets'])<1:
            flash('sets '+flash_string,'timer')
            valid=False
        
        return valid
    @classmethod
    def save_timers(cls, data):
        if not Timer.is_valid(data):
            return False
        query='''INSERT INTO timers(name,excercise_time,rest_time,sets,user_id,updated_at,created_at)
        VALUES(%(name)s,%(excercise_time)s,%(rest_time)s,%(sets)s,%(user_id)s,NOW(),NOW())'''
        return connectToMySQL(DB).query_db(query,data)
    @classmethod
    def update_timer(cls,data):
        this_timer=cls.by_id(data['id'])
        if this_timer.user.id!=session['user_id']:
            return False
        if not Timer.is_valid(data):
            return False
        query='''UPDATE timers SET name=%(name)s,excercise_time=%(excercise_time)s,rest_time=%(rest_time)s,sets=%(sets)s
        where id=%(id)s'''
        return connectToMySQL(DB).query_db(query,data)
    @classmethod
    def by_id(cls, id):
        data={'id':id}
        query='SELECT * FROM timers JOIN users ON users.id=timers.user_id where timers.id=%(id)s'
        result=connectToMySQL(DB).query_db(query,data)
        timer=result[0]
        timer_obj=cls(timer)
        timer_obj.user=user.User({
                'id':timer['users.id'],
                'username':timer['username'],
                'email':timer['email'],
                'password':timer['password'],
                'updated_at':timer['users.updated_at'],
                'created_at':timer['users.created_at']

        })
  
        return timer_obj
    @classmethod
    def destroy(cls,id):
        this_timer=cls.by_id(id)
        if this_timer.user.id!=session['user_id']:
            return False
        data={'id':id}
        query='DELETE FROM timers where id=%(id)s'
        return connectToMySQL(DB).query_db(query,data)