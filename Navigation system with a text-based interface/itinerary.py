"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the class Itinerary.

@file itinerary.py
"""
import math
from city import City, create_example_cities, get_cities_by_name

class Itinerary():
    """
    A sequence of cities.
    """


    def __init__(self, cities: list[City]) -> None:
        """
        Creates an itinerary with the provided sequence of cities,
        conserving order.
        :param cities: a sequence of cities, possibly empty.
        :return: None
        """
        #TODO
        self.cities = cities


    def total_distance(self) -> int:
        """
        Returns the total distance (in km) of the itinerary, which is
        the sum of the distances between successive cities.
        :return: the total distance.
        """
        #TODO
        distance = 0
        for list_index in range(1, len(self.cities)): 
            distance += City.distance(self.cities[list_index - 1], self.cities[list_index]) # find the distance of the two cites and add to total distance
        return distance

    def append_city(self, city: City) -> None:
        """
        Adds a city at the end of the sequence of cities to visit.
        :param city: the city to append
        :return: None.
        """
        #TODO
        self.cities.append(city) # append city into the instance

    def min_distance_insert_city(self, city: City) -> None:
        """
        Inserts a city in the itinerary so that the resulting
        total distance of the itinerary is minimised.
        :param city: the city to insert
        :return: None.
        """
        #TODO
        total_distance_list = []
        for index_to_add in range(0, len(self.cities)): # try to add the city to each index of the list and find the distance
            self.cities[index_to_add:index_to_add] = [city]
            total_distance_list.append(Itinerary.total_distance(self)) # append the distance into a list
            del self.cities[index_to_add] # delete before trying to add the city to next index
        min_distance = min(total_distance_list) # find the minimum distance
        for element_index in range(len(total_distance_list)):
            if min_distance == total_distance_list[element_index]:
                num = element_index #find the index that give the minimum distance
                break
        self.cities[num:num] = [city] # add the city to the index


    def __str__(self) -> str:
        """
        Returns the sequence of cities and the distance in parentheses
        For example, "Melbourne -> Kuala Lumpur (6368 km)"

        :return: a string representing the itinerary.
        """
        #TODO
        string = ''
        if len(self.cities) == 0:
            return "(0 km)"
        else:
            for city in self.cities: # run the city in the list
                if city == self.cities[len(self.cities) - 1]:
                    string += f"{city.name}"
                    string += f" ({Itinerary.total_distance(self)} km)"
                else:
                    string += f"{city.name}"
                    string += " -> "
            return string


if __name__ == "__main__":
    create_example_cities()
    test_itin = Itinerary([get_cities_by_name("Melbourne")[0],
                           get_cities_by_name("Kuala Lumpur")[0]])
    print(test_itin)

    #we try adding a city
    test_itin.append_city(get_cities_by_name("Baoding")[0])
    print(test_itin)

    #we try inserting a city
    test_itin.min_distance_insert_city(get_cities_by_name("Sydney")[0])
    print(test_itin)

    #we try inserting another city
    test_itin.min_distance_insert_city(get_cities_by_name("Canberra")[0])
    print(test_itin)
