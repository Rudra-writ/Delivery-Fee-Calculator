from fastapi import FastAPI, Request
from  main.fee_calculator import Delivery_Fee_Calculator
from pydantic import BaseModel

#Data validation of the input JSON data using pydantic
class Input_Data(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: str


app = FastAPI()

@app.post("/")
def delivery_fee(Input_Data: Input_Data):

    total_surcharge = Delivery_Fee_Calculator(Input_Data.cart_value, Input_Data.delivery_distance, Input_Data.number_of_items, Input_Data.time) #Creating an instance of the Delivery_Fee_Calculator class
    return total_surcharge.total_surcharge()

