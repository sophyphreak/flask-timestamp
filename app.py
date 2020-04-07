from flask import Flask
from flask_restful import Resource, Api
import arrow

app = Flask(__name__)
api = Api(app)

class TimestampNow(Resource):
    def get(self):
        now = arrow.utcnow()
        unix = now.timestamp
        utc = now.format('ddd, DD MMM YYYY HH:mm:ss ZZZ')
        return {"unix": unix, "utc": utc}

class TimestampSpecific(Resource):
    def get(self, date_string):
        try:
            input_time = arrow.get(date_string)
            unix = input_time.timestamp
            utc = input_time.format('ddd, DD MMM YYYY HH:mm:ss ZZZ')
            return {"unix": unix, "utc": utc}
        except:
            pass
        unix = int(date_string)
        input_time = arrow.get(unix)
        utc = input_time.format('ddd, DD MMM YYYY HH:mm:ss ZZZ')
        return {"unix": unix, "utc": utc}


api.add_resource(TimestampNow, '/api/timestamp')
api.add_resource(TimestampSpecific, '/api/timestamp/<date_string>')

if __name__ == '__main__':
    app.run(debug=True)