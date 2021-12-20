import os
import re

from utils import get_project_root

BLACKLIST_PATH = os.path.join(get_project_root(), 'blacklist.txt')


class CPFService:
    cpf = None

    def __init__(self, cpf):
        self.cpf = self.only_numbers(cpf)

    def only_numbers(self, text):
        return re.sub("[^0-9]", "", text)

    def validate_cpf(self):
        if not self.cpf:
            raise ValueError("No CPF")

        with open(BLACKLIST_PATH) as file:
            content = file.read()
            lines = content.splitlines()
            for line in lines:
                if self.only_numbers(line) == self.cpf:
                    return {'status': 'BLOCK', 'http_status': 404}
            return {'status': 'FREE', 'http_status': 302}
