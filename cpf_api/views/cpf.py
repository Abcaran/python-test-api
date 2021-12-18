from flask import jsonify
from flask_restful import Resource

from cpf_api.services.cpf import CPFService


class CPFView(Resource):

    def get(self, cpf):
        return CPFService(cpf=cpf).validate_cpf()
