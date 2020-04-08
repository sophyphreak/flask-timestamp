from flask_restful import Resource
import arrow


class TimestampNow(Resource):
    def get(self):
        unix = arrow.utcnow().timestamp
        utc = arrow.utcnow().format("ddd, DD MMM YYYY HH:mm:ss ZZZ")
        return {"unix": unix, "utc": utc}


class TimestampSpecific(Resource):
    def get(self, date_string):
        try:
            input_time = arrow.get(date_string)
            unix = input_time.timestamp
            utc = input_time.format("ddd, DD MMM YYYY HH:mm:ss ZZZ")
            return {"unix": unix, "utc": utc}
        except:
            pass
        try:
            unix = int(date_string)
            input_time = arrow.get(unix)
            utc = input_time.format("ddd, DD MMM YYYY HH:mm:ss ZZZ")
            return {"unix": unix, "utc": utc}
        except:
            return {"error": "Invalid Date"}
