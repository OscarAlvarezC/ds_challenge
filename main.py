from flask import Flask, request
from flask import jsonify
from src.models.models import db
from src.api.evaluations import configure_evaluation_routes
from config import config
from src.common.utils import HTTPStatus

def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    # configure routes
    configure_evaluation_routes(app)
    return app

enviroment = config['development']
app = create_app(enviroment)

@app.route('/api/v1/test', methods=['GET'])
def test():
    response = {'message': 'hello from api v1!'}
    return jsonify(response), HTTPStatus.OK 
    # by default every response is status 200 = OK

if __name__ == '__main__':
    app.run(debug=True)