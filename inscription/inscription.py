from openerp.osv import osv
from openerp.osv import fields
import time


class inscription_establishment(osv.osv):
	""" Scolar establishment """
	_name = "inscription.establishment"
	_description = "Scolar Establishment"
	_colums = {
		'logo': fields.binary('Logo'),
		'name': fields.char('Name', size=100, required=True),
		'description': fields.text('Description'),
		'adress': fields.text('Adress'),
		#'town': fields.many2one('town', 'Town')
	}
	_sql_constraints = [
		('name', 'unique(name)', 'The name of the establishment must de unique')
	]
inscription_establishment()

class inscription_university(osv.osv):
	""" University """
	_name = "inscription.university"
	_description = "University"
	_colums = {
		'logo': fields.binary('Logo'),
		'abbreviation': fields.char('Abbreviation', size=10, required=True),
		'name': fields.char('Name', size=100, required=True),
		'description': fields.text('Description'),
		'website': fields.char('Website', size=100),
		'adress': fields.text('Adress'),
		#'town': fields.many2one('town', 'Town'),
		#'establishment': fields.many2one('establishment', 'Establishment')
	}
	_sql_constraints = [
		('name', 'unique(name)', 'The abbreviation of the university must de unique'),
		('name', 'unique(name)', 'The name of the university must de unique')
	]
inscription_university()

class inscription_degree(osv.osv):
	""" Degree """
	_name = "inscription.degree"
	_description = "Degree"
	_colums = {
		'name': fields.char('Name', size=100, required=True),
		'description': fields.text('Description'),
		#'university': fields.many2one('university', 'University')
	}
inscription_degree()

class inscription_speciality(osv.osv):
	""" speciality """
	_name = "inscription.speciality"
	_description = "speciality"
	_colums = {
		'name': fields.char('Name', size=100, required=True),
		'description': fields.text('Description'),
		#'degree': fields.many2one('degree', 'Degree')
	}
inscription_speciality()

class inscription_reforme(osv.osv):
	""" reforme """
	_name = "inscription.reforme"
	_description = "reforme"
	_colums = {
		'name': fields.char('Name', size=100, required=True),
		'description': fields.text('Description'),
		'apply_date': fields.date('Apply Date')
		#'speciality': fields.many2one('speciality', 'Speciality'),
		'confirmation': fields.selection((('y','Confirmed') ,('n','Unconfirmed')), 'Status'),
		'application': fields.selection((('y','Applicated') ,('n','Not Applicated')), 'application')
	}
inscription_reforme()

class inscription_module(osv.osv):
	""" Module class """
	_name = "inscription.module"
	_description = "Module class"
	_colums = {
		'id': fields.char('Identifier', size=10, required=True),
		'designation': fields.char('Designation', size=100, required=True),
		'coefficient': fields.float('Coefficient', required=True),
		'hours_number': fields.integer('Hours Number'),
		'description': fields.text('Description')
	}
inscription_module()

class inscription_teaching_unit(osv.osv):
	""" teaching_unit """
	_name = "inscription.teaching_unit"
	_description = "teaching_unit"
	_colums = {
		'id': fields.char('Identifier', size=10, required=True),
		'designation': fields.char('Designation', size=100, required=True),
		'coefficient': fields.float('Coefficient', required=True),
		'hours_number': fields.integer('Hours Number'),
		'description': fields.text('Description')
	}
inscription_teaching_unit