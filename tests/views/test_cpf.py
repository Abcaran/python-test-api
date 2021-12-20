import unittest

import main


class CPFViewTestCase(unittest.TestCase):

    def setUp(self):
        self.app = main.app
        self.response = self.app.get('/<string:cpf>/')

    def test_get_empty_params(self):
        pass

    def test_get_cpf_allowed(self):
        self.assertEqual(302, self.response.status_code)

    def test_get_cpf_blacklisted(self):
        pass
