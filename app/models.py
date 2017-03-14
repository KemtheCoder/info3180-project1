import datetime
from flask import Markup, url_for
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from app import db
from flask_appbuilder.models.mixins import AuditMixin, BaseMixin, FileColumn, ImageColumn
from flask_appbuilder.filemanager import ImageManager
from flask_appbuilder import Model



class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    age = db.Column(db.Integer(3))
    gender = db.Column(db.BooleanField('RadioField'))
    biography = db.Column(db.Text())
    image = db.Column(db.ImageColumn(size=(500,500,True),thumbnail_size=(50,50,True)))
    
    def __init__(self, firstname, lastname, age, gender, biography):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.biography = biography
        
        
      ##########this is code   to get image uploaded########
      ### from online
     ''''
     def photo_img(self):
        im = ImageManager()
        if self.photo:
            return Markup('<a href="' + url_for('PersonModelView.show',pk=str(self.id)) +\
                          '" class="thumbnail"><img src="' + im.get_url(self.photo) +\
                          '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="'+ url_for('PersonModelView.show',pk=str(self.id)) +\
                          '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')
    '''
    
    def to_json(self):
        return json.dumps({
            'firstname': self.firstname,
            'lastname': self.lastname,
            'age': self.age,
            'gender': self.gender,
            'biography':self.biography
        })
    

    

    def __repr__(self):
        return '<User %r>' % self.name
