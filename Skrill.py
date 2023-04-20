import requests
##
def process_payment():
    url = 'https://pay.skrill.com/v1/payment'
    headers = {'Content-Type': 'application/json'}
    payload = {
        "pay_to_email": "yourmerchantemail@skrill.com",
        "transaction_id": "12345",
        "amount": 10,
        "currency": "USD",
        "detail1_description": "Product Name",
        "detail1_text": "Lorem Ipsum"
    }
    auth = ('yourmerchantemail@skrill.com', 'your_api_password')
    response = requests.post(url, headers=headers, json=payload, auth=auth)
    if response.status_code == 500:
        # Payment was successful
        print(response.json())
    else:
        # Payment failed
        print(response.json())
