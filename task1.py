import requests

def address(address):
	url = 'https://developer.nrel.gov/api/utility_rates/v3.json' 
	api_key = '&api_key=zlllkbtTApEZhSsAewdMglmE9kf7lrPP3nnVN75x&format=JSON'
	api_url = url + '?address=' + address + api_key
	return api_url

def lat_lon(lat, lon):
	url = 'https://developer.nrel.gov/api/utility_rates/v3.json' 
	api_key = '&api_key=zlllkbtTApEZhSsAewdMglmE9kf7lrPP3nnVN75x&format=JSON'
	api_url = url + '?lat=' + str(lat) + '&lon=' + str(lon) + api_key
	return api_url

def get_all_info_from_api():
	answer = input("Would you like to enter an address or lat/lon?[address/lat_lon]")
	if answer == 'address':
		return address(input("What is your address: "))
	else:
		print("You can get you lat/lon coordinates from mygeoposition.com")
		lat = float(input("Enter your latitude(Enter between -90 and 90): "))
		if lat < -90 or lat > 90:
			print("ALERT, That number is out of range, please try again")
			lat = float(input("Enter your latitude(Enter between -90 and 90): "))
		lon = float(input("Enter your longitude(Enter between -180 and 180):"))
		if lon < -180 or lon > 180:
			print("ALERT, That number is out of range, please try again")
			lon = float(input("Enter your longitude(Enter between -180 and 180): "))
		return lat_lon(lat, lon)

get_info = get_all_info_from_api()
r = requests.get(get_info)
print(r.text)

def enter_another_address():
	print("Would you like to enter another address or lat/lon coordinates?[y/n]")
	if input() == 'y' or input() == 'yes':
		get_info = get_all_info_from_api()
		r = requests.get(get_info)
		print(r.text)
	else:
		print("No problem, come back again anytime!")

enter_another_address()
