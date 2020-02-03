from flask import request
from flask_restful import Resource
from managers.Data import load_data_from_api,load_all_code_site_from_api, load_all_grandeur_hydro_from_api
class Codes(Resource):
    grandeur_hydro=request.args.get('grandeur_hydro', '')
