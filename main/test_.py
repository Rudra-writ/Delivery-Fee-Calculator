from fastapi.testclient import TestClient
import pytest
from main.app import app

client = TestClient(app) 

#testing the API response using 11 different test cases
@pytest.mark.parametrize("cart_value, delivery_distance, number_of_items, time, result", 
[(790, 2335, 4, "2021-10-12T13:00:00Z", 710),  #result should be 710 cents(7.1 euros) since: 15 euros > ((10  - 7.9 ) (cart_surcharge) + 2 (delivery_base_surcharge) + 3 (additional_delivery_surcharge) + (0) (no_of_items_surcharge)) euros
(10000, 2335, 4, "2021-10-12T13:00:00Z",0),    #result should be 0 cents since: cart_value = 10000 cents(100 euros)
(910, 3501, 8, "2021-10-12T13:00:00Z",1090),   #result should be 1090 cents(10.9 euros) since: 15 euros > ((10  - 9.1 ) (cart_surcharge) + 2 (delivery_base_surcharge) + 5  (additional_delivery_surcharge) + (4 * 0.5) (no_of_items_surcharge)) euros
(910, 3501, 12, "2021-10-12T13:00:00Z",1290),  #result should be 1290 cents(12,9 euros) since: 15 euros > ((10  - 9.1 ) (cart_surcharge) + 2 (delivery_base_surcharge) + 5  (additional_delivery_surcharge) + (8 * 0.5) (no_of_items_surcharge)) euros
(300, 3501, 12, "2021-10-12T13:00:00Z",1500),  #result should be 1500 cents(15 euros)  since: 15 euros < ((10  - 3 ) (cart_surcharge) + 2 (delivery_base_surcharge) + 5  (additional_delivery_surcharge) + (8 * 0.5) (no_of_items_surcharge)) euros
(999, 1001, 5, "2021-10-12T13:00:00Z",351),    #result should be 351 cents(3,51 euros) since: 15 euros > ((10  - 9.99 ) (cart_surcharge) + 2 (delivery_base_surcharge) + 1 (additional_delivery_surcharge) + (1 * 0.5) (no_of_items_surcharge)) euros
(999, 1001, 5, "2023-01-20T13:00:00Z",351),    #result should be 351 cents(3,51 euros) since: 15 euros > ((10  - 9.99 ) (cart_surcharge) + 2 (delivery_base_surcharge) + 1 (additional_delivery_surcharge) + (1 * 0.5) (no_of_items_surcharge)) euros, although its a Friday but its not a rush hour (3-7 PM)
(999, 1001, 5, "2023-01-20T15:00:00Z",421),    #result should be 421 cents(4,21 euros) since: 15 euros > (((10  - 9.99 ) (cart_surcharge) + 2 (delivery_base_surcharge) + 1 (additional_delivery_surcharge) + (1 * 0.5) (no_of_items_surcharge)) * 1.2 euros (becuase its a  Friday rush hour(3-7 PM)))
(999, 1001, 5, "2023-01-20T19:00:00Z",421),    #result should be 421 cents(4,21 euros) since: 15 euros > (((10  - 9.99 ) (cart_surcharge) + 2 (delivery_base_surcharge) + 1 (additional_delivery_surcharge) + (1 * 0.5) (no_of_items_surcharge)) * 1.2 euros (becuase its a Friday rush hour(3-7 PM)))
(999, 1001, 5, "2023-01-20T19:02:00Z",351),    #result should be 351 cents(3,51 euros) since: 15 euros > (((10  - 9.99 ) (cart_surcharge) + 2 (delivery_base_surcharge) + 1 (additional_delivery_surcharge) + (1 * 0.5) (no_of_items_surcharge)) * 1 euro ( becuase its a Friday but 2 minutes passed 7 PM))
(999, 1001, 5, "2023-01-20T19:00:01Z",351),    #result should be 351 cents(3,51 euros) since: 15 euros > (((10  - 9.99 ) (cart_surcharge) + 2 (delivery_base_surcharge) + 1 (additional_delivery_surcharge) + (1 * 0.5) (no_of_items_surcharge)) * 1 euro ( becuase its a Friday but 1 second passed 7 PM))
],)

def test_total_surcharge(cart_value, delivery_distance, number_of_items, time, result):
    
    response = client.post("/", json={"cart_value": cart_value, "delivery_distance": delivery_distance, "number_of_items": number_of_items, "time": time })
    assert response.status_code == 200         #Checking if HTTP response is 200 to ensure the operation is successful
    assert response.json() == 	{"delivery_fee": result}  #Checking if response result(JSON) is same as the expected result


  