STATIC_SEARCH_RESP = r"""
{
  "count": 1,
  "code": "20170120_5_3_1_224_9fa211e8a14f44e5ae684bf4ee4b59f2_",
  "next_page_code": null,
  "max_wait": "1.0",
  "response_time": "0.96",
  "results": [
    {
      "hotel_code": "{hotel_code}",
      "checkout": "{checkout_date}",
      "checkin": "{checkin_date}",
      "destination_code": "206e4",
      "products": [
        {
          "code": "10e6cc_56305817968661_0_3_2_2_0_1_2406044196_0_3-0-0",
          "offer": false,
          "pay_at_hotel": false,
          "price": "357.21",
          "currency": "{currency_code}",
          "rooms": [
            {
              "pax": {
                "children_ages": [],
                "adult_quantity": "{pax_count}"
              },
              "room_category": "Standard",
              "room_description": "Triple Room",
              "nightly_prices": {
                "2017-01-20": "71.44",
                "2017-01-21": "71.44",
                "2017-01-22": "71.44",
                "2017-01-23": "71.44",
                "2017-01-24": "71.44"
              },
              "room_type": "TB"
            }
          ],
          "nonrefundable": null,
          "supports_cancellation": true,
          "hotel_currency": null,
          "hotel_price": null,
          "meal_type": "RO",
          "minimum_selling_price": null,
          "view": false
        }
      ]
    }
  ]
}
"""

STATIC_AVAIL_RESP = r"""
{
  "code": "{search_code}",
  "count": 1,
  "results": [
    {
      "code": "135f3a_55186709030717_1_2_2_2_0_1_438178821_23_0-1-0.",
      "destination_code": "206ec",
      "hotel_code": "{hotel_code}",
      "additional_info": "",
      "checkin": "2017-01-20",
      "checkout": "2017-01-25",
      "price": "212.38",
      "currency": "EUR",
      "pay_at_hotel": false,
      "hotel_price": null,
      "hotel_currency": null,
      "meal_type": "RO",
      "nonrefundable": true,
      "view": false,
      "rooms": [
        {
          "pax": {
            "children_ages": [],
            "adult_quantity": 1
          },
          "room_category": "Shared Facility",
          "room_description": "TWIN WITH SHARED BATHROOM",
          "nightly_prices": {
            "2017-01-20": "42.47",
            "2017-01-21": "42.47",
            "2017-01-22": "42.47",
            "2017-01-23": "42.47",
            "2017-01-24": "42.47"
          },
          "room_type": "SB"
        }
      ],
      "supports_cancellation": true,
      "minimum_selling_price": null,
      "offer": false,
      "policies": [
        {
          "ratio": "1.00",
          "days_remaining": 44
        }
      ]
    }
  ]
}
"""

STATIC_PROVISION_RESP = r"""
{
  "code": "PL77K57A2CLA",
  "destination_code": "206ec",
  "offer": false,
  "price": "212.38",
  "currency": "EUR",
  "rooms": [
    {
      "pax": {
        "children_ages": [],
        "adult_quantity": 1
      },
      "room_category": "Shared Facility",
      "room_description": "TWIN WITH SHARED BATHROOM",
      "nightly_prices": {
        "2017-01-20": "42.47",
        "2017-01-21": "42.47",
        "2017-01-22": "42.47",
        "2017-01-23": "42.47",
        "2017-01-24": "42.47"
      },
      "room_type": "SB"
    }
  ],
  "nonrefundable": false,
  "additional_info": "Check-in hour 15:00 – 02:00. No alcohol is served.",
  "supports_cancellation": true,
  "hotel_code": "135f3a",
  "hotel_currency": null,
  "hotel_price": null,
  "checkin": "2017-01-20",
  "meal_type": "RO",
  "policies": [
    {
      "ratio": "1.00",
      "days_remaining": 44
    }
  ],
  "view": false,
  "checkout": "2017-01-25",
  "minimum_selling_price": null,
  "pay_at_hotel": false
}
"""

STATIC_BOOKING_RESP = r"""
{
  "code": "B3CJBKKDU43F",
  "created_at": "2016-12-09 07:03:03.367699+00:00",
  "checkin": "2017-01-20",
  "checkout": "2017-01-25",
  "hotel_code": "135f3a",
  "destination_code": "206ec",
  "client_nationality": "gb",
  "pay_at_hotel": false,
  "currency": "EUR",
  "mealtype_code": "RO",
  "nonrefundable": false,
  "view": false,
  "policies": [
    {
      "days_remaining": 44,
      "ratio": "1.00"
    }
  ],
  "price": "212.38",
  "rooms": [
    {
      "pax": {
        "children_ages": "",
        "adult_quantity": 1
      },
      "room_category": "Shared Facility",
      "room_description": "TWIN WITH SHARED BATHROOM",
      "nightly_prices": {
        "2017-01-20": "42.47",
        "2017-01-21": "42.47",
        "2017-01-22": "42.47",
        "2017-01-23": "42.47",
        "2017-01-24": "42.47"
      },
      "room_type": "SB"
    }
  ],
  "status": "succeeded",
  "confirmation_numbers": [
    {
      "confirmation_number": "164-3015081",
      "names": [
        "John Doe"
      ],
      "rooms": [
        {
          "room_description": "TWIN WITH SHARED BATHROOM",
          "room_type": "TWN"
        }
      ]
    }
  ],
  "hotel_payment_info": [
    {
      "hotel_currency": null,
      "hotel_price": null
    }
  ],
  "minimum_selling_price": null,
  "special_request": null
}
"""

STATIC_CANCEL_BOOKING_RESP = r"""
{
  "currency": "EUR",
  "charge_amount": "212.38",
  "code": "B3CJBKKDU43F"
}
"""

STATIC_CHECK_BOOKING_RESP = r"""
{
  "code": "{booking_code}",
  "created_at": "2016-12-09T07:03:03.367Z",
  "checkin": "2017-01-20",
  "checkout": "2017-01-25",
  "hotel_code": "135f3a",
  "destination_code": "206ec",
  "client_nationality": "gb",
  "pay_at_hotel": false,
  "currency": "EUR",
  "mealtype_code": "RO",
  "nonrefundable": false,
  "view": false,
  "policies": [
    {
      "days_remaining": 44,
      "ratio": "1.00"
    }
  ],
  "price": "212.38",
  "rooms": [
    {
      "pax": {
        "children_ages": "",
        "adult_quantity": 1
      },
      "room_category": "Shared Facility",
      "room_description": "TWIN WITH SHARED BATHROOM",
      "nightly_prices": {
        "2017-01-20": "42.47",
        "2017-01-21": "42.47",
        "2017-01-22": "42.47",
        "2017-01-23": "42.47",
        "2017-01-24": "42.47"
      },
      "room_type": "SB"
    }
  ],
  "status": "cancelled",
  "confirmation_numbers": [
    {
      "confirmation_number": "164-3015081",
      "names": [
        "John Doe"
      ],
      "rooms": [
        {
          "room_description": "TWIN WITH SHARED BATHROOM",
          "room_type": "TWN"
        }
      ]
    }
  ],
  "hotel_payment_info": [
    {
      "hotel_currency": null,
      "hotel_price": null
    }
  ],
  "minimum_selling_price": null,
  "special_request": null
}
"""
