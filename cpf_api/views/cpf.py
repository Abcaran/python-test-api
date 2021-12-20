from flask_restful import Resource

from cpf_api.services.cpf import CPFService


class CPFView(Resource):

    def get(self, cpf):
        response = CPFService(cpf=cpf).validate_cpf()
        return {
            'CPF': cpf,
            'status': response.get('status'),
        }, response.get('http_status')
