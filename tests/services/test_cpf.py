import unittest

from cpf_api.services.cpf import CPFService

ALLOWED_CPF_FORMATTED = '201.988.471-83'
ALLOWED_CPF_UNFORMATTED = '20198847183'
BLACKLISTED_CPF_FORMATTED = '150.188.156-55'
BLACKLISTED_CPF_UNFORMATTED = '15018815655'


class CPFServiceTestCase(unittest.TestCase):

    # def test_validate_no_cpf(self):
    #     cpf_service = CPFService.validate_cpf(cpf=None)
    #
    #     pass

    def test_validate_cpf_allowed_formatted(self):
        cpf_service = CPFService.validate_cpf(cpf=ALLOWED_CPF_FORMATTED)
        self.assertEqual(cpf_service.status, "FREE")

    # def test_validate_cpf_allowed_unformatted(self):
    #     cpf_service = CPFService.validate_cpf(cpf=ALLOWED_CPF_UNFORMATTED)
    #     pass
    #
    # def test_validate_cpf_blacklisted_formatted(self):
    #     cpf_service = CPFService.validate_cpf(cpf=BLACKLISTED_CPF_FORMATTED)
    #
    # def test_validate_cpf_blacklisted_unformatted(self):
    #     cpf_service = CPFService.validate_cpf(cpf=BLACKLISTED_CPF_UNFORMATTED)


