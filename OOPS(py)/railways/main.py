# to be continue



#import requests
#
#response = requests.get(
#    "https://api.railradar.in/v1/trains/"+"12919"+"?haltsOnly=false",
#    headers={"Authorization": "rg_4d1dc81c60e14360877c375b9d61950c"},
#)
#
#
#
#
#class IRCTC:
#
#    def __init__(self):
#        user_input = input("""1. Enter 1 to check live train status
#                              2. Enter 2 to check PNR
#                              3. Enter 3 to check train schedule""")
#        
#        if user_input=="1":
#            print("live train status")
#        elif user_input=="2":
#            pass
#        elif user_input=="3":
#            self.train_schedule()
#        else:
#            pass
#
#        def train_schedule():
#            train_no = input("Enter the train no. ")
#            url="https://api.railradar.in/v1/trains/"+train_no+"?haltsOnly=false"
#            response = requests.get(url,headers={"Authorization": "rg_4d1dc81c60e14360877c375b9d61950c"},)
#            data=response.json()
#            train_data=data["data"]
#        
#        def fetch_data():
#