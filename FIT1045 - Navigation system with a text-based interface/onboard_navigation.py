"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It puts together all parts of the assignment.

@file onboard_navigation.py
"""

from city import City, get_cities_by_name
from country import Country
from itinerary import Itinerary
from map_plotting import plot_itinerary
from vehicles import Vehicle, create_example_vehicles
from csv_parsing import create_cities_countries_from_csv 
from path_finding import find_shortest_path

def validate_input(prompt, valid_inputs): # to check the input is valid or not
	data_input = input(prompt)
	#check input in list or not
	while data_input not in valid_inputs:
		print("Invalid input, please try again.")
		data_input = input(prompt)
	return data_input

create_cities_countries_from_csv("worldcities_truncated.csv") # create all country and city
vehicle = create_example_vehicles() # create vehicle

# input what vehicle to use and use validate_input to check whether is valid input or not
vehicle_index = validate_input("Please select a vehicle [1 CrappyCrepeCar, 2 DiplomacyDonutDinghy, 3 TeleportingTarteTrolley] (just enter the index of vehicle): ", ['1', '2', '3'])  
# user input index of the vehicle, and get the vehicle class
vehicle_use = vehicle[int(vehicle_index) - 1]

# input origin country, chech whether the country is in the dictionary, name_to_countries using validate_input
origin_country = Country.name_to_countries[validate_input("Please input the origin country: ", Country.name_to_countries)]
i = 0
# use while loop to make sure the country contain the city
while i == 0: 
	# input origin city, check whether the city is in the dictionary, name_to_cities using validate_input
	origin_city_list = get_cities_by_name(validate_input("Please input the origin city: ", City.name_to_cities))
	# check which city(type = class) in the city list is in the city(type = class) of country
	for city_city in origin_city_list: 
		for city_country in origin_country.city_list:
			if city_city == city_country: # compare the city from origin_city_list to the city in country
				origin_city = city_city
				i = 1
				break
	if i == 0: # if city is not in the city of the country, request another input
		print("Invalid input")

# same as about, but request for destination
destination_country = Country.name_to_countries[validate_input("Please input the detination country: ", Country.name_to_countries)]
i = 0
while i == 0:
	destination_city_list = get_cities_by_name(validate_input("Please input the destination city: ", City.name_to_cities))
	for city_city in destination_city_list:
		for city_country in destination_country.city_list:
			if city_city == city_country:
				destination_city = city_city
				i = 1
				break
	if i == 0:
		print("Invalid input")

# find the shortest_path by using find_shortest_path from path_finding
shortest_path = find_shortest_path(vehicle_use, origin_city, destination_city)
print(f"\t{vehicle_use.compute_itinerary_time(shortest_path)}"
		f" hours with {vehicle_use} with path {shortest_path}.")
if shortest_path == None: 
	print("No path between the cities")
else:
	plot_itinerary(shortest_path)

