# Delivery-Fee-Calculator

This API developed with FastAPI calculates the delivery fee based on the following set of rules: 

 * If the cart value is less than 10€, a small order surcharge is added to the delivery price. The surcharge is the difference between the cart value and 10€. 
 * A delivery fee for the first 1000 meters (=1km) is 2€. If the delivery distance is longer than that, 1€ is added for every additional 500 meters that the courier     needs to travel before reaching the destination. Even if the distance would be shorter than 500 meters, the minimum fee is always 1€.
 * If the number of items is five or more, an additional 50 cent surcharge is added for each item above and including the fifth item. An extra "bulk" fee applies for more than 12 items of 1,20€
 * The delivery fee can never be more than 15€, including possible surcharges.
 * The delivery is free (0€) when the cart value is equal or more than 100€.
 * During the Friday rush (3 - 7 PM UTC), the delivery fee (the total fee including possible surcharges) will be multiplied by 1.2x. 
 
 The test automation has been implemented with pytest
 
 Instructions for using the API: 
 
 * Run "pip intsall -r requirements.txt"
 * To use the API, the following command can be used: "uvicorn main.app:app --reload"
 * Once, the application startup is complete, navigating to "http://127.0.0.1:8000/docs" will launch the interactive API documentation (swagger UI) 
 * In here, to interact with API, the "Post" method can be used to input the request payload in JSON and it will return a desired response payload, also in JSON
 * The test_.py file in the "main" folder have been used to test the API. It has 11 unique test cases, as per the requirements. To run the test automation,  navigate to "/main" and run the command "pytest test_.py -v"

