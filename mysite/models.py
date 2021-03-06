import sqlite3
from flask import g
import os
dir_path = os.path.dirname(os.path.abspath('__init__.py'))
DATABASE = os.path.join(dir_path, 'mysite.db')
def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	db.row_factory = sqlite3.Row
	return db

def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

def query_db(query, args=(), one=False):
	cur = get_db().execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv
