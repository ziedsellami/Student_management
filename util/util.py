from openerp.osv import osv
from openerp.osv import fields
import time

class util_country(osv.osv):
	""" Country """
	_name = "util.country"
	_description = "Country"
	_colums = {
		'flag': fields.binary('Flag'),
		'name': fields.char('Name', size=100, required=True)
	}
	_sql_constraints = [
		('name', 'unique(name)', 'The name of the country must de unique')
	]
util_country()

class util_town(osv.osv):
	""" Town of different country"""
	_name = "util.town"
	_description = "Town"
	_colums = {
		'name': fields.char('Name', size=100, required=True),
		'country': fields.many2one('country', 'Town')
	}
util_town()
