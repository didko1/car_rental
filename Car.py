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
import os
class Vehicle:
    days_reserve = 0

    def __init__(self, brand, model, reg_plate, year, color, mileage):
        self.brand = brand
        self.model = model
        self.reg_plate = reg_plate
        self.year = year
        self.color = color
        self.mileage = mileage
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
    dbName = "CarsList.csv"
    reserved = False
    def __init__(self, brand, model, reg_plate, year, color, mileage, car_type):
        super().__init__( brand, model, reg_plate, year, color, mileage)
        self.car_type = car_type
    def reserve(self, start_date, days_reserve):
        reserved = True
        print("Vehicle " + self.brand + " " + self.model + " " + self.reg_plate + " " + " is reserved for " + str(days_reserve) + ". Price is " + str(self.price_per_day*days_reserve))
    def getRentalFee(self, days_reserved):
         return self.price_per_day*days_reserved
    def addToDb(self):
        line = [self.brand, self.model, self.reg_plate, self.year, self.color,self.mileage, self.car_type]
        with open(self.dbName, mode='a', newline='') as db:
            writer = csv.writer(db)
            writer.writerow(line)
    
class MotorBike(Vehicle):
    price_per_day = 90
    dbName = "MotorbikesList.csv"
    def __init__(self, brand, model, reg_plate, year, color, mileage, cc):
        super().__init__(brand,model, reg_plate, year, color, mileage)
        self.cc = cc
    def reserve(self, start_date, days_reserve):
        reserved = True
        print("Vehicle " + self.brand + " " + self.model + " " + self.reg_plate + " is reserved for " + str(days_reserve) + ". Price is " + str(self.price_per_day*days_reserve))
    def getRentalFee(self, days_reserve):
        return self.price_per_day*days_reserve
    def addToDb(self):
        record = [self.brand, self.model, self.reg_plate, self.year, self.color, self.mileage, self.cc]
        with open(self.dbName, mode='a', newline='') as db:
            writer = csv.writer(db)
            writer.writerow(record)
class RentalPerson:
    def __init__(self,firstName, family, nationality, identification_number, card_id, email, phone_number, rent_period):
        self.firstName = firstName
        self.family = family
        self.nationality = nationality
        self.identification_number = identification_number
        self.card_id = card_id
        self.email = email
        self.phone_number = phone_number
        self.rent_period = rent_period
    def toString(self):
        print("Renter " + self.firstName + " " + self.family +" from " + self.nationality + 
              " with id: " + self.identification_number +
              ", cardId: " + self.card_id + " and contacts: " + self.phone_number + " " + self.email) 

class Document:
    def __init__(self, vehicle, renter):
        self.name = vehicle.brand + "-" + vehicle.model + "-" + renter.firstName + "-" + renter.family + ".txt"
        self.renter_name = renter.firstName
        self.renter_family = renter.family
        self.renter_id = renter.identification_number
        self.renter_cardId = renter.card_id
        self.vehicle_brand = vehicle.brand
        self.vehicle_model = vehicle.model
        self.vehicle_plate = vehicle.reg_plate
        self.vehicle_year = vehicle.year
        self.vehicle_color = vehicle.color
        self.vehicle_fee = vehicle.getRentalFee(renter.rent_period)
        
    def generateAgreement(self):
        f = open(self.name, "w")
        f.write("Car Rental Agreement\n")
        f.write("Agreement between Rent a car company and " + self.renter_name + " " + self.renter_family + "\n")
        f.write("entered on date " + str(date.today()) +"\n")
        f.write("1. Rental company agrees to rent to the Renter the following vehicle:\n")
        f.write("   Brand/model" + self.vehicle_brand + " " + self.vehicle_model + " \n License plate: " + self.vehicle_plate + "\n Year of manufacture: " + self.vehicle_year + "\n Color: " + self.vehicle_color+"\n")
        f.write("2. Rental Fees and Payment:")
        f.write("The Renter agrees to pay the Rental Company the total sum of " + str(self.vehicle_fee) + " leva for the entire rental period.\n")
        f.close()
        
   
    
def adminAction():
    print("1: Add car ")
    print("2: Add motorbike ")
    print("0 Exit ")
    action = int(input("Enter action "))
    if action == 1:
        #add new car to cars list
        print("Provide car info:")
        brand = input("brand: ")
        model = input("model: ")
        reg_plate = input("license plate: ")
        year = input("manufacture year: ")
        color = input("color: ")
        mileage = input("mileage: ")
        car_type = input("type: ")
        car = Car(brand, model,reg_plate,year,color,mileage,car_type)
        car.addToDb()
        adminAction()
    elif action == 2:
        #add new motrobike to bikes
        brand = input("brand: ")
        model = input("model: ")
        reg_plate = input("license plate: ")
        year = input("manufacture year: ")
        color = input("color: ")
        mileage = input("mileage: ")
        cc = input("CC: ")
        bike = MotorBike(brand, model, reg_plate, year, color, mileage, cc)
        bike.addToDb()
        adminAction()
    elif action == 0:
        showHomeMenu()
    else:
        print("Invalid action code")
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
        adminAction()
    else:
        print("Invalid username or password!")

def showVehicleList(listname):
    with open(listname,"r") as vehicle_list:
        reader = csv.reader(vehicle_list)
        rows = list(vehicle_list)
    for row in range(len(rows)):
        if row == 0:
            print("   " + rows[row])
            continue
        print(str(row) +", " + rows[row])

def collectRenterInfo():
    firstName = input("Enter first name: ")
    family = input("Enter second name: ")
    nationality = input("Enter nationality: ")
    identification_number = input("Enter identification number: ")
    card_id = input("Enter card id: ")
    email = input("Enter e-mail: ")
    phone_number = input("Enter phone number: ")
    rent_period = int(input("Enter rent period - days: "))
    renter = RentalPerson(firstName, family, nationality, identification_number, card_id, email, phone_number, rent_period)
    return renter

def bookVehicle(listname):
    action = int(input("Enter vehicle id or 0 to go to home"))
    if action == 0:
        showHomeMenu()
    else:
        if action > 0 and action < len(listname):
            with open(listname,"r") as vehicle_list:
                reader = csv.reader(vehicle_list)
                rows = list(vehicle_list) 
        vehicle_info = rows[action].split(",")
        car = Car(vehicle_info[0], vehicle_info[1], vehicle_info[2], vehicle_info[3], vehicle_info[4], vehicle_info[5], vehicle_info[6])
        renter = collectRenterInfo()
        doc = Document(car, renter)
        doc.generateAgreement()
            
            
            
            
        

def showHomeMenu():
    print("Welcome to Car rental software")
    print("Statrting with user priviliges")
    print("Enter 1 to choose car")
    print("Enter 2 to choose Motorbike")
    print("Enter 3 to login as admin")
    print("Enter 0 to close")
    action = int(input("choose action: "))
    if action == 0:
        exit()
    elif action == 1:
        print("Loading cars list")
        cars = "CarsList.csv"
        showVehicleList(cars)
        bookVehicle(cars)
    elif action == 2:
        print("Loading motorbikes list")
        showVehicleList("MotorbikesList.csv")
    elif action == 3:
        print("Logging as admin")
        adminLogin()
    

#Main
showHomeMenu()
    


    
'''my_car = Car(brand = "Dacia", model="Duster", reg_plate="r 1352 kn", year="2024", color="white", mileage="10000", car_type="SUV")
my_car.reserve(datetime.time,5)
my_bike = MotorBike(brand="KTM", model="Duke", reg_plate="r 1234 ak", year="2016", color="orange", mileage="20000", cc=390)
my_bike.reserve(datetime.time,3)
renter = RentalPerson(firstName="Deyan", family="Rusev",nationality="Bulgarian",identification_number="1234", card_id="12334",email="drusev@gmail.com",phone_number="0887610392")
renter.toString()
doc = Document("car_rental2.txt")
doc.generateAgreement(renter.firstName, renter.family, renter.identification_number, renter.card_id, my_car.brand, my_car.model,my_car.reg_plate,my_car.year, my_car.color, my_car.getRentalFee(5))
'''
