import datetime
import webapp2_extras.appengine.auth.models

from lib.google.appengine.ext import db
from lib.google.appengine.ext.db import polymodel
from webapp2_extras import security

#Clase padre para crear usuarios y pacientes
class Persona(polymodel.PolyModel):
	nombre = db.StringProperty(required=True)
	apPaterno = db.StringProperty(required=True)
	apMaterno = db.StringProperty()
	email = db.EmailProperty()
    pic = db.BlobProperty()

class Paciente(Persona):
	direccion = db.PostalAddressProperty()
	telefono = db.PhoneNumberProperty()
	comentarioPaciente = db.TextProperty()

class perfil(Persona)
    firma = db.StringProperty()

class Citas(db.Model):
    paciente =  db.ReferenceProperty('Paciente')
    fechaCita= db.DateProperty()
    primerCita = db.BooleanProperty()
    comentario = db.TextProperty()

class notas(db.Model):
    perfilAsociado = db.ReferenceProperty('perfil')
    nota = db.DateProperty()