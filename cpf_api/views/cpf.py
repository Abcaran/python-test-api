from flask import jsonify
from flask_restful import Resource


class CPFView(Resource):

    def get(self, cpf):
        return jsonify({'hello world': 'teste'})
