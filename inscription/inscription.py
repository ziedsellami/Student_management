from openerp.osv import osv
from openerp.osv import fields
import time

class country(osv.osv):
	""" Country """
	_name = "country"
	_description = "Country"
	_colums = {
		'flag': fields.binary('Flag'),
		'name': fields.char('Name', size=100, required=True)
	}
	_sql_constraints = [
		('name', 'unique(name)', 'The name of the country must de unique')
	]
country()

class town(osv.osv):
	""" town """
	_name = "town"
	_description = "Town"
	_colums = {
		'name': fields.char('Name', size=100, required=True),
		'country': fields.many2one('country', 'Town')
	}
town()

class establishment(osv.osv):
	""" Scolar establishment """
	_name = "establishment"
	_description = "Scolar Establishment"
	_colums = {
		'logo': fields.binary('Logo'),
		'name': fields.char('Name', size=100, required=True),
		'description': fields.text('Description'),
		'adress': fields.text('Adress'),
		'town': fields.many2one('town', 'Town')
	}
	_sql_constraints = [
		('name', 'unique(name)', 'The name of the establishment must de unique')
	]
establishment()

class university(osv.osv):
	""" University """
	_name = "university"
	_description = "University"
	_colums = {
		'logo': fields.binary('Logo'),
		'abbreviation': fields.char('Abbreviation', size=10, required=True),
		'name': fields.char('Name', size=100, required=True),
		'description': fields.text('Description'),
		'website': fields.char('Website', size=100),
		'adress': fields.text('Adress'),
		'town': fields.many2one('town', 'Town'),
		'establishment': fields.many2one('establishment', 'Establishment')
	}
	_sql_constraints = [
		('name', 'unique(name)', 'The abbreviation of the university must de unique'),
		('name', 'unique(name)', 'The name of the university must de unique')
	]
university()

class degree(osv.osv):
	""" Degree """
	_name = "Degree"
	_description = "Degree"
	_colums = {
		'name': fields.char('Name', size=100, required=True),
		'description': fields.text('Description')
	}
degree()

class speciality(osv.osv):
	""" Degree """
	_name = "Degree"
	_description = "Degree"
	_colums = {
		'name': fields.char('Name', size=100, required=True),
		'description': fields.text('Description')
	}
degree()