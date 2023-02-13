import math
import datetime
import calendar

class Delivery_Fee_Calculator:
    def __init__(self, cart_value, delivery_distance, number_of_items, time):
        self.cart_value = cart_value/100  #converting cents to euros
        self.delivery_distance = delivery_distance
        self.number_of_items = number_of_items
        self.time = time

    #Method to calculate surcharge based on cart value
    def cart_value_surcharge(self):
        surcharge_cart = (10 - self.cart_value) if self.cart_value < 10 else 0
        return surcharge_cart

    #Method to calculate surcharge based on delivery distance
    def delivery_distance_surcharge(self):
        base_fee = 2
        if self.delivery_distance <= 1000:
            return base_fee   
        else:
            distance_exceed = self.delivery_distance - 1000
            surcharge_distance = (distance_exceed/500 + base_fee) if (distance_exceed % 500) == 0 else (math.floor(distance_exceed/500) + base_fee + 1) #adding a delivery fee of 1 euro for every additional distance per 500 metre, travelled beyond base fee for 1000 m 
            return surcharge_distance

    #Method to calculate surcharge based on number of items
    def number_of_items_surcharge(self):
        if self.number_of_items <= 4:
            return 0
        elif  4 < self.number_of_items < 13:
            return (self.number_of_items - 4) * 0.5    #multiplying the exceeding number of items beyond 4 with 0,5 euros (50 cents) if number of items in cart, is greater than 4 but not more than 12
        else:
            return ((self.number_of_items - 4) * 0.5) + 1.2 #adding an additional surcharge of 1,2 euros (120 cents) if number of items is more than 12

    #Method to calculate surcharge based on time of week
    def time_surcharge(self):
        day_of_week = datetime.datetime.strptime(self.time, '%Y-%m-%dT%H:%M:%SZ').weekday() #getting the index for the day of week from the input date time
        hour = datetime.datetime.strptime(self.time, '%Y-%m-%dT%H:%M:%SZ').time().hour
        minute = datetime.datetime.strptime(self.time, '%Y-%m-%dT%H:%M:%SZ').time().minute
        second = datetime.datetime.strptime(self.time, '%Y-%m-%dT%H:%M:%SZ').time().second
        if calendar.day_name[day_of_week] == 'Friday' and hour in range(15,20) and (hour + minute + second) <= 19:   #Checking if day of week is a "Friday"  and  "the time of day is between 3 p.m (13 hrs) and 7 p.m (19 hrs)"  and  "doesn't exceed 7 p.m by a second"
            return 1.2  #multiplier if time falls within rush hour
        else:
            return 1

    #Master method to calculate total surcharge  (called in app.py)   
    def total_surcharge(self):
        surcharge_cart = self.cart_value_surcharge()
        surcharge_distance = self.delivery_distance_surcharge()
        surcharge_number_of_items = self.number_of_items_surcharge()
        surcharge_time = self.time_surcharge()

        if self.cart_value >= 100 :
            return {"delivery_fee" : 0}    #if cart value is greater than or equal to 100 euros no delivery charge is added
        else:
            return {"delivery_fee" : int(min(1500, (((surcharge_cart + surcharge_distance + surcharge_number_of_items) * surcharge_time)) * 100))}    #If total delivery charge is less than or equal to 1500 cents then that value is returned  otherwise a maximum of 1500 cents of surcharge is returned 

    





        



   


    