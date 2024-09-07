# Paste your solution from previous tasks below
"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a function to create a path, encoded as an Itinerary, that is shortest for some Vehicle.

@file path_finding.py
"""
import math
import networkx

from city import City, get_city_by_id
from itinerary import Itinerary
from vehicles import Vehicle, create_example_vehicles
from csv_parsing import create_cities_countries_from_csv


def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Itinerary | None:
    """
    Returns a shortest path between two cities for a given vehicle as an Itinerary,
    or None if there is no path.

    :param vehicle: The vehicle to use.
    :param from_city: The departure city.
    :param to_city: The arrival city.
    :return: A shortest path from departure to arrival, or None if there is none.
    """
    #TODO
    # create a graph G
    G = networkx.Graph()
    # add all city (class) into a list
    city_list = []
    for key in City.id_to_cities.keys():
        city_list.append(City.id_to_cities[key])
    # find the travel time between all the city
    for city_index_1 in range(len(city_list)): # run the city in the list
        for city_index_2 in range(city_index_1 + 1, len(city_list)): # match the city to other city in the list(match all city)
            city_1 = city_list[city_index_1]
            city_2 = city_list[city_index_2]
            time = vehicle.compute_travel_time(city_1, city_2) # find the travel time of the city
            if time != math.inf: # if can travel between the two cities, add edge into the graph
                G.add_edge(city_1, city_2, weight = time)
    try: # try the shortest path of the two cities
        shortest_path = Itinerary(networkx.shortest_path(G, from_city, to_city))
        Itinerary(shortest_path)
        return shortest_path
    except: # if shortest path give error, return none
        return None

if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")
    vehicles = create_example_vehicles()

    from_cities = set()
    for city_id in [1036533631, 1036142029, 1458988644]:
        from_cities.add(get_city_by_id(city_id))


    #we create some vehicles
    vehicles = create_example_vehicles()

    to_cities = set(from_cities)
    for from_city in from_cities:
        to_cities -= {from_city}
        for to_city in to_cities:
            print(f"{from_city} to {to_city}:")
            for test_vehicle in vehicles:
                shortest_path = find_shortest_path(test_vehicle, from_city, to_city)
                print(f"\t{test_vehicle.compute_itinerary_time(shortest_path)}"
                      f" hours with {test_vehicle} with path {shortest_path}.")
