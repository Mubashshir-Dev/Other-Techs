import requests as req
import dotenv
from pprint import pprint

dotenv.load()
api=os.environ['API']

class Irctc:
	base_url="https://api.railradar.in/v1/trains/"
	headers={"Authorization": api }
	def __init__(self):
		self.num=input("train num : ")
		self.menu()

	def menu(self):
		print(" enter 1 -> Get Train details :")
		print(" enter 2 -> Live Train status :")
		print(" enter 3 -> Train route Geometry :")
		user_input=input()
		if user_input=="1":
			self.get_train_details()
		elif user_input=="2":
			self.live_train_status()
		elif user_input=="3":
			self.get_train_route_geo()

	def fetch(self,details):
		url=self.base_url+self.num+details
		response= req.get(url,headers=self.headers)
		data=response.json()
		if data["success"]:
			train_info=data["data"]
			pprint(train_info,sort_dicts=False)
			print("\n"*10)
			return train_info
		else:
			pprint(data["error"],sort_dicts=False)
			print("\n"*10)
			return data["error"]

	def get_train_details(self):
		qus=input("only halting stops (excludes pass-through) (Y/N):")
		if(qus.upper()=="Y"):
			return self.fetch(details="?haltsOnly=true")
		else:
			return self.fetch(details="?haltsOnly=false")

	def live_train_status(self):
		return self.fetch(details="/live")

	def get_train_route_geo(self):
		return self.fetch(details="/route?format=geojson&stops=true")

while True:
	obj=Irctc()



