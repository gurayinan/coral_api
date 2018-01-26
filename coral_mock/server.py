import json
from flask import Flask, request
import coral_mock.static_responses as static_resp

flask_app = Flask(__name__)


@flask_app.route("/api/v2/search/", methods=["GET"])
def search_():
    # Retrieve static json sample and replace values from request params
    # for mocking purposes.
    resp_ = json.loads(static_resp.STATIC_SEARCH_RESP)
    resp_["results"][0]["hotel_code"] = request.args.get("hotel_code")
    resp_["results"][0]["checkout"] = request.args.get("checkout")
    resp_["results"][0]["checkin"] = request.args.get("checkin")
    resp_["results"][0]["products"][0]["currency"] = \
        request.args.get("currency")
    resp_["results"][0]["products"][0]["rooms"][0]["pax"]["adult_quantity"] =\
        request.args.get("pax")
    return json.dumps(resp_, indent=2)


@flask_app.route("/api/v2/hotel-availability/", methods=["GET"])
def check_availability_():
    json_resp = json.loads(static_resp.STATIC_AVAIL_RESP)
    json_resp["code"] = request.args.get("search_code")
    json_resp["results"][0]["hotel_code"] = request.args.get("hotel_code")
    return json.dumps(json_resp, indent=2)


@flask_app.route("/api/v2/provision/<product_code>", methods=["GET"])
def provision_(product_code):
    json_resp = json.loads(static_resp.STATIC_PROVISION_RESP)
    return json.dumps(json_resp, indent=2)


@flask_app.route("/api/v2/book/<product_code>", methods=["GET"])
def make_booking_(product_code):
    json_resp = json.loads(static_resp.STATIC_BOOKING_RESP)
    return json.dumps(json_resp, indent=2)


@flask_app.route("/api/v2/cancel/<booking_code>", methods=["GET"])
def cancel_booking_(booking_code):
    json_resp = json.loads(static_resp.STATIC_CANCEL_BOOKING_RESP)
    return json.dumps(json_resp, indent=2)


@flask_app.route("/api/v2/bookings/<booking_code>/", methods=["GET"])
def check_booking_(booking_code):
    json_resp = json.loads(static_resp.STATIC_CHECK_BOOKING_RESP)
    json_resp["code"] = booking_code
    return json.dumps(json_resp, indent=2)


if __name__ == "__main__":
    flask_app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
