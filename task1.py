import requests

answer = input("Enter address or lat/log coordinates: ")

if answer == 'address':
	address = input("What is your address?")
	address.strip().split()
	api_url = 'https://developer.nrel.gov/api/utility_rates/v3.json' 
			  + '?address=' + address 
			  + '&api_key=zlllkbtTApEZhSsAewdMglmE9kf7lrPP3nnVN75x&format=JSON'
else:
	print("If you need to look up your address for lat/lon, you can go to the following url: mygeoposition.com")
	lat = float(input("Enter your latitude(number must be between -90 and 90): "))
	if lat < -90 or lat > 90:
		print("That number is out of range, please try again")
		lat = float(input("Enter your latitude(number must be between -90 and 90): "))
	lon = float(input("Enter you longitude(number must be between -180 and 180):"))
	if lon < -180 or lon > 180:
		print("That number is out of range, please try again")
		lon = float(input("Enter your longitude(number must be between -180 and 180): "))
	api_url = 'https://developer.nrel.gov/api/utility_rates/v3.json' + '?lat=' + str(lat) + '&lon=' + str(lon) + '&api_key=zlllkbtTApEZhSsAewdMglmE9kf7lrPP3nnVN75x&format=JSON'

r = requests.get(api_url)
print(r.text)


def address():
	address = input("What is your address?")
	address.strip().split()
	api_url = 'https://developer.nrel.gov/api/utility_rates/v3.json' 
			  + '?address=' + address 
			  + '&api_key=zlllkbtTApEZhSsAewdMglmE9kf7lrPP3nnVN75x&format=JSON'
	return api_url

def lat_lon():
	print("If you need to look up your address for lat/lon, you can go to the following url: mygeoposition.com")
	lat = float(input("Enter your latitude(number must be between -90 and 90): "))
	if lat < -90 or lat > 90:
		print("That number is out of range, please try again")
		lat = float(input("Enter your latitude(number must be between -90 and 90): "))
	lon = float(input("Enter you longitude(number must be between -180 and 180):"))
	if lon < -180 or lon > 180:
		print("That number is out of range, please try again")
		lon = float(input("Enter your longitude(number must be between -180 and 180): "))
	api_url = 'https://developer.nrel.gov/api/utility_rates/v3.json' + '?lat=' + str(lat) + '&lon=' + str(lon) + '&api_key=zlllkbtTApEZhSsAewdMglmE9kf7lrPP3nnVN75x&format=JSON'
	return api_url


address = address()
lat_lon = lat_lon()

def question():
	answer = input("Enter address or lat/log coordinates: ")
	if answer == 'address':
		return address
	else: 
		return lat_lon
	go_again = input("Would you like to enter another address? [y/n]")
	if go_again == 'y' or go_again == 'yes':
		return question()
	else: 
		pass

#to use later:

'''import urllib.parse

api_url = 'https://developer.nrel.gov/api/utility_rates/v3.json?'
data = {
    "lat": lat,
    "lon": lon,
    "api_key": "zlllkbtTApEZhSsAewdMglmE9kf7lrPP3nnVN75x",
    "format": "JSON"
}
api_url += urllib.parse.urlencode(data)

def response_in_range(question, low, high, type=float):
    answer = get_response(question, type)
    if low > answer > high:
        print("Pick a number between: {} - {}".format(low, high))
        return response_in_range(question, low, high, type)
    return answer

def get_response(question, type):
    try:
        return type(input(question))
    except ValueError:
        print("Invalid Input!")
        return get_response(question, type)


lat = response_in_range("Enter Latitude", -90, 90)'''