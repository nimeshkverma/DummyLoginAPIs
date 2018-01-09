from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics


def param_check(data, params):
    all_params_present = True
    message = {}
    for param, param_type in params.iteritems():
        if not (param in data.keys() and type(data[param]) == param_type):
            all_params_present = False
            message[param] = 'This Field is required'

    return all_params_present, message


class Login(APIView):

    def post(self, request):
        params = {
            'username': str,
            'password': str,
            'source': str,
            'source_version': int,
        }
        all_params_present, message = param_check(request.data, params)
        if all_params_present:
            response = {
                "meta": "",
                "data": {
                    "customer_id": 11,
                    "session_token": "upwards_11_uIXGGbHaTPuaaVNpAsdwFDvrahQMGfAn"
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                "meta": "",
                "data": message
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):

    def get(self, request, customer_id):
        data = {
            "customer_id": customer_id,
            "session_token": request.META.get("HTTP_SESSION_TOKEN")
        }
        params = {
            "customer_id": int,
            "session_token": str
        }
        all_params_present, message = param_check(data, params)
        if all_params_present:
            response = {
                "meta": "",
                "data": {}
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        else:
            response = {
                "meta": "",
                "data": message
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)


class NoticeBoard(APIView):

    def get(self, request, customer_id):
        data = {
            "customer_id": customer_id,
            "session_token": request.META.get("HTTP_SESSION_TOKEN")
        }
        params = {
            "customer_id": int,
            "session_token": str
        }
        all_params_present, message = param_check(data, params)
        if all_params_present:
            response = {
                "meta": "",
                "data": {
                    "notice_board": True,
                    "notice": {
                        "msg": [
                            "Please Call us when you reach the Customer's Doc Pick Up",
                            "Our Whatsapp Number: 9911616971",
                        ],
                        "title": "Upwards Notice Board"
                    }
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                "meta": "",
                "data": message
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)


class CustomerPickup(APIView):

    def get(self, request, customer_id):
        data = {
            "customer_id": customer_id,
            "session_token": request.META.get("HTTP_SESSION_TOKEN")
        }
        params = {
            "customer_id": int,
            "session_token": str
        }
        all_params_present, message = param_check(data, params)
        if all_params_present:
            response = {
                "meta": "",
                "data":  [
                    {
                        "customer_id": 1,
                        "customer_name": "Ram Kumar Yadav",
                        "customer_phone_no": [
                            "9911991199",
                            "099-000000"
                        ],
                        "customer_address": "Pranik Chambers",
                        "cheque_qty": 2,
                        "cheque_amt": [
                            15000,
                            60120
                        ],
                        "date_of_request": "2018-11-01",
                        "date_of_pickup": "2018-05-03",
                        "city": "Mumbai",
                        "pincode": "400090"
                    },
                    {
                        "customer_id": 2,
                        "customer_name": "Kiran Sharma",
                        "customer_phone_no": [
                            "1245210",
                            "2541002"
                        ],
                        "customer_address": "XYZ, Mumbai-91",
                        "cheque_qty": 2,
                        "cheque_amt": [
                            15009,
                            60111
                        ],
                        "date_of_request": "2018-05-21",
                        "date_of_pickup": "2018-05-03",
                        "city": "Mumbai",
                        "pincode": "400090"
                    },
                    {
                        "customer_id": 3,
                        "customer_name": "Viran Sharma",
                        "customer_phone_no": [
                            "1245210",
                            "2541002"
                        ],
                        "customer_address": "XYZ, Mumbai-91",
                        "cheque_qty": 2,
                        "cheque_amt": [
                            15007,
                            60128
                        ],
                        "date_of_request": "2018-05-21",
                        "date_of_pickup": "2018-05-03",
                        "city": "Pune",
                        "pincode": "400091"
                    },
                    {
                        "customer_id": 4,
                        "customer_name": "Kiran Sharma",
                        "customer_phone_no": [
                            "1245210",
                            "2541002"
                        ],
                        "customer_address": "XYZ, Mumbai-91",
                        "cheque_qty": 2,
                        "cheque_amt": [
                            15005,
                            60126
                        ],
                        "date_of_request": "2018-05-21",
                        "date_of_pickup": "2018-05-03",
                        "city": "Mumbai",
                        "pincode": "4000904"
                    },
                    {
                        "customer_id": 5,
                        "customer_name": "Miran Sharma",
                        "customer_phone_no": [
                            "1245210",
                            "2541002"
                        ],
                        "customer_address": "XYZ, Mumbai-91",
                        "cheque_qty": 2,
                        "cheque_amt": [
                            15003,
                            60124
                        ],
                        "date_of_request": "2018-05-21",
                        "date_of_pickup": "2018-05-03",
                        "city": "Pune",
                        "pincode": "400090"
                    },
                    {
                        "customer_id": 6,
                        "customer_name": "Kiran Sharma",
                        "customer_phone_no": [
                            "1245210",
                            "2541002"
                        ],
                        "customer_address": "XYZ, Mumbai-91",
                        "cheque_qty": 2,
                        "cheque_amt": [
                            15001,
                            60122
                        ],
                        "date_of_request": "2018-05-21",
                        "date_of_pickup": "2018-05-03",
                        "city": "Mumbai",
                        "pincode": "400090"
                    }
                ]
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                "meta": "",
                "data": message
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)


class DocumentUploaded(APIView):

    def get(self, request, customer_id):
        data = {
            "customer_id": customer_id,
            "session_token": request.META.get("HTTP_SESSION_TOKEN")
        }
        params = {
            "customer_id": int,
            "session_token": str
        }
        all_params_present, message = param_check(data, params)
        if all_params_present:
            response = {
                "meta": "",
                "data":  {
                    'customer_id': auth_data['customer_id'],
                    'documents_uploaded': {
                        1: False,
                        2: False,
                        3: False,
                        4: False,
                        5: False,
                        6: False,
                        7: False,
                        8: False,
                        9: False,
                        10: False,
                        11: False,
                        12: False,
                        13: False,
                        14: False,
                        15: False,
                    }
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                "meta": "",
                "data": message
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)


class DocumentType(APIView):

    def get(self, request):
        response = {
            "meta": "",
            "data": [
                {
                    "id": 1,
                    "name": "aadhaar_front",
                    "usage": "KYC purpose"
                },
                {
                    "id": 2,
                    "name": "profile_pic",
                    "usage": "KYC purpose"
                },
                {
                    "id": 3,
                    "name": "pan",
                    "usage": "KYC purpose"
                },
                {
                    "id": 4,
                    "name": "salary_slips",
                    "usage": "Eligibility Purpose"
                },
                {
                    "id": 5,
                    "name": "address_proof",
                    "usage": "KYC purpose"
                },
                {
                    "id": 6,
                    "name": "unsigned_loan_agreement",
                    "usage": "KYC purpose"
                },
                {
                    "id": 7,
                    "name": "signed_loan_agreement",
                    "usage": "KYC purpose"
                },
                {
                    "id": 8,
                    "name": "signature",
                    "usage": "KYC purpose"
                },
                {
                    "id": 9,
                    "name": "current_month_income_proof",
                    "usage": "Eligibility Purpose"
                },
                {
                    "id": 10,
                    "name": "bank_statement",
                    "usage": "Eligibility Purpose"
                },
                {
                    "id": 11,
                    "name": "aadhaar_back",
                    "usage": "KYC purpose"
                },
                {
                    "id": 12,
                    "name": "last_month_income_proof",
                    "usage": "Eligibility Purpose"
                },
                {
                    "id": 13,
                    "name": "second_last_month_income_proof",
                    "usage": "Eligibility Purpose"
                },
                {
                    "id": 14,
                    "name": "company_id",
                    "usage": "KYC purpose"
                }
            ]
        }
        return Response(response, status=status.HTTP_200_OK)
