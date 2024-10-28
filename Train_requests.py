import train_api as tapi
import json


def simpleout(table):
    if table == "Error":
        print("Error")
    else:
        table = table.json()
        if table["services"] is None:
            print("No trains")
        else:
            for row in table["services"]:
                if row["isPassenger"] == True:
                    print(row["locationDetail"]["description"]," to ",row["locationDetail"]["destination"][0]['description']," ",row["locationDetail"]["gbttBookedDeparture"]," ",row["serviceUid"])


def directToFrom(x,y):
    table= tapi.depart_to(x,y)
    simpleout(table)

def trains_from(x):
    table= tapi.departures(x)
    simpleout(table)

def mainmenu():
    menu ={'1': 'Search trains from a station', '2': 'Search direct trains from one station to anothers','9': 'Exit'}
    while True: 
        options=menu.keys()
        print("Menu")
        for entry in options: 
            print (entry, menu[entry])
        selection=input("Please Select:")
        if selection =='1':
            x = input("From: ")
            trains_from(x)
        elif selection =='2':
            x = input("From: ")
            y = input("To: ")
            directToFrom(x,y)
        elif selection =='9':
            exit()
        else:
            print ("Invalid input")
            


while True:
    mainmenu()