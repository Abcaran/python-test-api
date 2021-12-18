from flask import Flask
from flask_restful import Api

from cpf_api.views.cpf import CPFView

app = Flask(__name__)
api = Api(app)
api.add_resource(CPFView, '/<string:cpf>/')

if __name__ == '__main__':
    app.run(debug=True)
