#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 13:34:32 2024

@author: didko
"""
import csv
import datetime
import aspose.pdf as ap
from datetime import date
import base64
import maskpass
class Vehicle:
    days_reserve = 0
    def __init__(self, brand, model, reg_plate, year, color, mileage, reserved):
        self.brand = brand
        self.model = model
        self.reg_plate = reg_plate
        self.year = year
        self.color = color
        self.mileage = mileage
        self.reserved = False

def setMileage(self, mileage):
    self.mileage = mileage
def VehicleHistory(self):
    filename = f"vehicle_{self.reg_plate}_info.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Brand','Model','Reg_number'])
        writer.writerow([self.brand,self.model,self.reg_plate])
    
class Car(Vehicle):
    price_per_day = 70
    def __init__(self, brand, model, reg_plate, year, color, mileage, reserved, car_type):
        super().__init__( brand, model, reg_plate, year, color, mileage, reserved)
        self.car_type = car_type
        VehicleHistory(self)
    def reserve(self, start_date, days_reserve):
        reserved = True
        print("Vehicle " + self.brand + " " + self.model + " " + self.reg_plate + " " + " is reserved for " + str(days_reserve) + ". Price is " + str(self.price_per_day*days_reserve))
    def getRentalFee(self, days_reserved):
         return self.price_per_day*days_reserved
class MotorBike(Vehicle):
    price_per_day = 90
    def __init__(self, brand, model, reg_plate, year, color, mileage, reserved, cc):
        super().__init__(brand,model,reg_plate,year,color,mileage,reserved)
        self.cc = cc
        VehicleHistory(self)
        
    def reserve(self, start_date, days_reserve):
        reserved = True
        print("Vehicle " + self.brand + " " + self.model + " " + self.reg_plate + " is reserved for " + str(days_reserve) + ". Price is " + str(self.price_per_day*days_reserve))
    def getRentalFee(self, days_reserve):
        return self.price_per_day*days_reserve
class RentalPerson:
    def __init__(self,firstName, family, nationality, identification_number, card_id, email, phone_number):
        self.firstName = firstName
        self.family = family
        self.nationality = nationality
        self.identification_number = identification_number
        self.card_id = card_id
        self.email = email
        self.phone_number = phone_number
    def toString(self):
        print("Renter " + self.firstName + " " + self.family +" from " + self.nationality + 
              " with id: " + self.identification_number +
              ", cardId: " + self.card_id + " and contacts: " + self.phone_number + " " + self.email) 

class Document:
    def __init__(self, name):
        self.name = name
    def generateAgreement(self, renter_name, renter_family, renter_id, renter_cardId, vehicle_brand, vehicle_model, vehicle_plate, vehicle_year, vehicle_color, vehicle_fee):
        f = open(self.name, "w")
        f.write("Car Rental Agreement\n")
        f.write("Agreement between Rent a car company and " + renter_name + " " + renter.family + "\n")
        f.write("entered on date " + str(date.today()) +"\n")
        f.write("1. Rental company agrees to rent to the Renter the following vehicle:\n")
        f.write("   Brand/model" + vehicle_brand + " " + vehicle_model + " \n License plate: " + vehicle_plate + "\n Year of manufacture: " + vehicle_year + "\n Color: " +vehicle_color+"\n")
        f.write("2. Rental Fees and Payment:")
        f.write("The Renter agrees to pay the Rental Company the total sum of " + str(vehicle_fee) + " leva for the entire rental period.\n")
        f.close()
        
   
        
   
    
def adminLogin():
    print("Enter username:")
    username = input()
    encpass = base64.b64encode(maskpass.advpass().encode("utf-8"))
    
    with open(".admin_credentials", "r") as f:
        lines = f.read().split('\n')
        cr_user = base64.b64encode(lines[0].encode("utf-8"))
        cr_pass = base64.b64encode(lines[1].encode("utf-8"))
    print(base64.b64decode(cr_user).decode("utf-8"))
    print(base64.b64decode(cr_pass).decode("utf-8"))
    if(username == base64.b64decode(cr_user).decode("utf-8") and base64.b64decode(encpass).decode("utf-8") == base64.b64decode(cr_pass).decode("utf-8")):
        print("Hello admin")
    else:
        print("Invalid username or password!")
 #   if(username == "admin" && )
    
    
#USAGE
print("Welcome to Car rental software")
print("Statrting with user priviliges")
print("Enter 1 to choose car")
print("Enter 2 to choose Motorbike")
print("Enter 3 to login as admin")
print("Enter 0 to close")
action = int(input("choose action"))
if action == 0:
    exit()
elif action == 1:
    print("Loading cars list")
    #TODO read cars from csv, coose car reserve car create document
    
elif action == 2:
    print("Loading motorbikes list")
    #TODO read motorbike from csv and create instance of bike and reserve it and create document
elif action == 3:
    print("Logging as admin")
    adminLogin()
    


    
my_car = Car(brand = "Dacia", model="Duster", reg_plate="r 1352 kn", year="2024", color="white", mileage="10000", reserved="false", car_type="SUV")
my_car.reserve(datetime.time,5)
my_bike = MotorBike(brand="KTM", model="Duke", reg_plate="r 1234 ak", year="2016", color="orange", mileage="20000", reserved="false", cc=390)
my_bike.reserve(datetime.time,3)
renter = RentalPerson(firstName="Deyan", family="Rusev",nationality="Bulgarian",identification_number="1234", card_id="12334",email="drusev@gmail.com",phone_number="0887610392")
renter.toString()
doc = Document("car_rental2.txt")
doc.generateAgreement(renter.firstName, renter.family, renter.identification_number, renter.card_id, my_car.brand, my_car.model,my_car.reg_plate,my_car.year, my_car.color, my_car.getRentalFee(5))