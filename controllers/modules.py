from tornado.web import RequestHandler, Application, removeslash
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import parse_command_line
from tornado.gen import coroutine

# other libraries
import json
import os
from motor import MotorClient

# env
try:
    from controllers import env

    db_uname = env.db
    db_pswd = env.pswd
except:
    db_uname = os.environ['db_name']
    db_pswd = os.environ['db_pswd']

db = MotorClient("mongodb://{0}:{1}@ds147225.mlab.com:47225/kalburr-server".format(db_uname, db_pswd))["kalburr-server"]
