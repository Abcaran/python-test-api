from flask import jsonify
from flask_restful import Resource


class CPFResource(Resource):

    def get(self):
        return jsonify({'hello world': 'teste'})
