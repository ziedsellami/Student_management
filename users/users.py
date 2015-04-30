from openerp.osv import osv
from openerp.osv import fields
import time


class users_person(osv.osv):
	""" Parent class of all users """
	_name = "users.person"
	_description = "Parent class of all users"
	_colums = {
		'picture': fields.binary('Logo'),
		'first_name': fields.char('First Name', size=100, required=True),
		'last_name': fields.char('Last Name', size=100, required=True),
		'adress': fields.text('Adress'),
		'email': fields.char('Email Adress', size=100, required=True),
		'phone' : fields.integer('Phone Number'),
		
	}
	_sql_constraints = [
		('name', 'unique(name)', 'The name of the establishment must de unique')
	]
users_person()