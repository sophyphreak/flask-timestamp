from flask import Flask
from flask_restful import Api

from resources.timestamp import TimestampNow, TimestampSpecific

app = Flask(__name__)
api = Api(app)

api.add_resource(TimestampNow, '/api/timestamp/')
api.add_resource(TimestampSpecific, '/api/timestamp/<date_string>')

if __name__ == '__main__':
    app.run(port=5000)