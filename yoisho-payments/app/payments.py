from bottle import Bottle, request
import json
from random import randint
from datetime import datetime

app = Bottle()

@app.get('/get_currency')
def get_currency():

	currency = request.query['currency']
        clist_buy={'USD':'389', 'SGD':'281'}
        clist_sell={'USD':'489', 'SGD':'381'}

        rcur={}

        rand1 = randint(100,200)
        rand2 = randint(100,200)

        try:
                rcur['buy'] = str(clist_buy[currency]) + "." + str(rand1)
        except:
                rcur['buy'] = -1

        try:
                rcur['sell'] = str(clist_sell[currency]) + "." + str(rand2)
        except:
                rcur['sell']=-1

        rcur['timestamp']=str(datetime.now())

	#return dict(data=rcur)
	return dict(rcur)



@app.get('/swagger')
def swagger():

	swagger = '''{   "swagger" : "2.0",   "host" : "",   "basePath" : "",   "schemes" : [ "http" ],   "paths" : {     "/get_currency" : {       "get" : {         "description" : "",         "operationId" : "get_currency",         "produces" : [ "application/json" ],         "parameters" : [ {           "description" : "The desired currency",           "required" : true,           "in" : "query",           "name" : "currency",           "type" : "string"         } ],         "responses" : {           "default" : {             "description" : "successful operation"           }         }       }     }   },   "info" : {     "title" : "Yoisho Currency Exchange",     "description" : "",     "version" : "1.0"   },   "x-axway" : {     "corsEnabled" : true,     "basePaths" : [ "" ],     "serviceType" : "rest",     "deprecated" : false,     "tags" : { }   } }'''

	return swagger

