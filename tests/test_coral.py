import unittest
import json
from cli_app.client import CoralClient


class CoralTests(unittest.TestCase):

    def setUp(self):
        self.client = CoralClient()
        self.test_values = {
            "hotel_code": "10545b",
            "check_in": "2017-04-22",
            "check_out": "2017-04-25",
            "currency": "USD",
            "pax_count": 4,
            "booking_code": "120jmsda34!sad.ss",
            "product_code": "1234ml90nsx",
            "search_code": "s21mol9978zs"
        }

    def test_search_hotel_code_match(self):
        sample_result = self.client.search_hotel(
            pax_=self.test_values.get('pax_count'),
            check_in=self.test_values.get('check_in'),
            check_out=self.test_values.get('check_out'),
            currency_code=self.test_values.get('currency'),
            hotel_code=self.test_values.get('hotel_code')
        )
        self.assertIn(member="hotel_code\": \"{hotel_code}".format(
            hotel_code=self.test_values.get('hotel_code')
        ), container=sample_result)

    def test_search_dates_match(self):
        sample_result = self.client.search_hotel(
            pax_=self.test_values.get('pax_count'),
            check_in=self.test_values.get('check_in'),
            check_out=self.test_values.get('check_out'),
            currency_code=self.test_values.get('currency'),
            hotel_code=self.test_values.get('hotel_code')
        )
        self.assertIn(member="checkin\": \"{check_in}".format(
            check_in=self.test_values.get('check_in')
        ), container=sample_result)
        self.assertIn(member="checkout\": \"{check_out}".format(
            check_out=self.test_values.get('check_out')
        ), container=sample_result)

    def test_check_search_code_matches(self):
        sample_result = self.client.check_availability(
            hotel_code=self.test_values.get('hotel_code'),
            search_code=self.test_values.get('search_code')
        )
        self.assertEqual(
            first=json.loads(sample_result)['code'],
            second=self.test_values.get('search_code')
        )

    def test_check_provision_response_type(self):
        sample_result = self.client.make_provision(
            product_code=self.test_values.get('product_code')
        )
        self.assertIsInstance(json.loads(sample_result), dict)
        self.assertIsInstance(sample_result, str)

    def test_cancel_response_has_charged_amount(self):
        sample_result = self.client.cancel_booking(
            booking_code=self.test_values.get('booking_code')
        )
        self.assertTrue('charge_amount' in json.loads(sample_result))

    def test_check_booking_code_matches(self):
        sample_result = self.client.check_booking_status(
            booking_code=self.test_values.get('booking_code')
        )
        self.assertEqual(
            first=json.loads(sample_result)['code'],
            second=self.test_values.get('booking_code')
        )

    def test_booking_response_has_status_field(self):
        sample_result = self.client.make_booking(
            product_code=self.test_values.get('product_code')
        )
        self.assertTrue('status' in json.loads(sample_result))

    def test_check_search_results_count_matches(self):
        sample_result = self.client.search_hotel(
            pax_=self.test_values.get('pax_count'),
            check_in=self.test_values.get('check_in'),
            check_out=self.test_values.get('check_out'),
            currency_code=self.test_values.get('currency'),
            hotel_code=self.test_values.get('hotel_code')
        )
        sample_dict = json.loads(sample_result)
        self.assertEqual(
            first=int(sample_dict['count']),
            second=len(sample_dict['results'])
        )
