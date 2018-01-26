import argparse
import datetime
import requests


class CoralClient(object):
    API_ENDPOINT = "http://127.0.0.1:5000/api/v2/"

    @staticmethod
    def date_validator(date_):
        try:
            resp_ = datetime.datetime.strptime(date_, "%Y-%m-%d")
            return resp_.strftime("%Y-%m-%d")
        except ValueError:
            err_msg = "Not a valid date : {date}".format(date=date_)
            raise argparse.ArgumentTypeError(err_msg)

    def search_hotel(self, pax_=2, check_in="2017-01-01",
                     check_out="2017-01-04", hotel_code="10a45b",
                     currency_code="USD"):
        uri_temp = self.API_ENDPOINT + "search/?pax={px}&checkin={c_in}" \
                                          "&checkout={c_out}&hotel_code=" \
                                          "{hcode}&currency={cur}"
        request_url = uri_temp.format(
            px=pax_, c_in=check_in, c_out=check_out, hcode=hotel_code,
            cur=currency_code
        )
        response = requests.get(request_url)
        return response.text

    def check_availability(self, hotel_code="10a45b",
                           search_code="n123ıkasdas_asdj??"):
        uri_temp = self.API_ENDPOINT + \
                      "hotel-availability/?search_code={scode}" \
                      "&hotel_code={hcode}"
        request_url = uri_temp.format(
            scode=search_code, hcode=hotel_code
        )
        response = requests.get(request_url)
        return response.text

    def make_provision(self, product_code="8klmsad89x"):
        request_url = self.API_ENDPOINT + "provision/{p_code}".format(
            p_code=product_code
        )
        response = requests.get(request_url)
        return response.text

    def make_booking(self, product_code):
        request_url = self.API_ENDPOINT + "book/{p_code}".format(
            p_code=product_code
        )
        response = requests.get(request_url)
        return response.text

    def check_booking_status(self, booking_code):
        request_url = self.API_ENDPOINT + "bookings/{b_code}".format(
            b_code=booking_code
        )
        response = requests.get(request_url)
        return response.text

    def cancel_booking(self, booking_code):
        request_url = self.API_ENDPOINT + "cancel/{b_code}".format(
            b_code=booking_code
        )
        response = requests.get(request_url)
        return response.text


def main():
    cli_base = CoralClient()
    parser = argparse.ArgumentParser()
    parser.add_argument("action",
                        help="""
                            can be one of following; search, availability,
                            provision, book, cancel, bookings
                            """,
                        type=str)
    parser.add_argument("--pax", help="Adult count", type=int)
    parser.add_argument("--checkin", help="Check-in date,format = YYYY-MM-DD",
                        type=cli_base.date_validator)
    parser.add_argument("--hotelcode", help="Unique code for hotel", type=str)
    parser.add_argument("--checkout", help="Checkout date,format = YYYY-MM-DD",
                        type=cli_base.date_validator)
    parser.add_argument("--currency", help="Price currency code", type=str)
    parser.add_argument("--searchcode",
                        help="Search code for availability check.", type=str)
    parser.add_argument("--productcode",
                        help="Product code for provision step.", type=str)
    parser.add_argument("--bookingcode",
                        help="""
                            Booking code for checking and cancellation
                            """, type=str)
    arguments = parser.parse_args()
    if arguments.action == "search":
        result_data = cli_base.search_hotel(
            pax_=arguments.pax,
            check_in=arguments.checkin,
            check_out=arguments.checkout,
            hotel_code=arguments.hotelcode,
            currency_code=arguments.currency
        )
        print(result_data)
    elif arguments.action == "availability":
        result_data = cli_base.check_availability(
            hotel_code=arguments.hotelcode,
            search_code=arguments.searchcode
        )
        print(result_data)
    elif arguments.action == "provision":
        result_data = cli_base.make_provision(
            product_code=arguments.productcode
        )
        print(result_data)
    elif arguments.action == "book":
        result_data = cli_base.make_booking(
            product_code=arguments.productcode
        )
        print(result_data)
    elif arguments.action == "cancel":
        result_data = cli_base.cancel_booking(
            booking_code=arguments.bookingcode
        )
        print(result_data)
    elif arguments.action == "bookings":
        result_data = cli_base.check_booking_status(
            booking_code=arguments.bookingcode
        )
        print(result_data)


if __name__ == "__main__":
    main()
