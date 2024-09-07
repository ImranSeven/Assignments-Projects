"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the class Country.

@file country.py
"""
from tabulate import tabulate
from city import City, create_example_cities

class Country():
    """
    Represents a country.
    """

    name_to_countries = dict() # a dict that associates country names to instances.

    def __init__(self, name: str, iso3: str) -> None:
        """
        Creates an instance with a country name and a country ISO code with 3 characters.

        :param country_name: The name of the country
        :param country_iso3: The unique 3-letter identifier of this country
	    :return: None
        """
        self.name = name
        self.iso3 = iso3
        #TODO
        self.city_list = [] # create a list for city in the country 
        Country.name_to_countries[self.name] = self # add the instances as value into the dictionary of country, country name is the key

    def add_city(self, city: City) -> None:
        """
        Adds a city to the country.

        :param city: The city to add to this country
        :return: None
        """
        #TODO
        self.city_list.append(city) # append city (class) into the city_list of country
        

    def get_cities(self, city_type: list[str] = None) -> list[City]:
        """
        Returns a list of cities of this country.

        The argument city_type can be given to specify a subset of
        the city types that must be returned.
        Cities that do not correspond to these city types are not returned.
        If None is given, all cities are returned.

        :param city_type: None, or a list of strings, each of which describes the type of city.
        :return: a list of cities in this country that have the specified city types.
        """
        #TODO
        list_city = []
        if city_type == None: # if the city type is None, return all city of the country
            return self.city_list
        else:
            for citytype in city_type: # run the city type (list) that input
                for city in self.city_list: # run the city in the city list of a Country
                    if city.city_type == citytype: # check all the type of city same as the city type given or not, if same then append into a list
                        list_city.append(city)
            return list_city
            
    def print_cities(self) -> None:
        """
        Prints a table of the cities in the country, from most populous at the top
        to least populous. Use the tabulate module to print the table, with row headers:
        "Order", "Name", "Coordinates", "City type", "Population", "City ID".
        Order should start at 0 for the most populous city, and increase by 1 for each city.
        """
        #TODO
        list_city = []
        for city in self.city_list: # run the city in the country
            list_city.append(City.get_table_data(city)) # get a list of data of the city from City and append it into a list
        list_city = sorted(list_city, key=lambda city: int(city[3]), reverse=True) # sort the list (outer list) according to the population of cities
        for index_number in range(len(list_city)):
            list_city[index_number][0:0] = list(str(index_number)) # for each city add order at the first place of the list (inner list)
        list_city[0:0] = [["Order", "Name", "Coordinates", "City type", "Population", "City ID"]]
        print(f"Cities of {self.name}") 
        print(tabulate(list_city)) # use tabulate to form a table

    def __str__(self) -> str:
        """
        Returns the name of the country.
        """
        return self.name


def add_city_to_country(city: City, country_name: str, country_iso3: str) -> None:
    """
    Adds a City to a country.
    If the country does not exist, create it.

    :param country_name: The name of the country
    :param country_iso3: The unique 3-letter identifier of this country
    :return: None
    """
    #TODO
    if country_name not in Country.name_to_countries: # check whether the country already in the dictionary or not, if not then create the country and name of the country as the key
        Country(country_name, country_iso3) # create country
    country = Country.name_to_countries[country_name] # find the country from the dictionary
    country.city_list.append(city) # append the city into the city list of the country

def find_country_of_city(city: City) -> Country:
    """
    Returns the Country this city belongs to.
    We assume there is exactly one country containing this city.

    :param city: The city.
    :return: The country where the city is.
    """
    #TODO
    for country in Country.name_to_countries.values(): # run all the country in the city
        if city in country.city_list: # if city is in the city list of the country, return the country
            return country

def create_example_countries() -> None:
    """
    Creates a few countries for testing purposes.
    Adds some cities to it.
    """
    create_example_cities()
    malaysia = Country("Malaysia", "MAS")
    kuala_lumpur = City.name_to_cities["Kuala Lumpur"][0]
    malaysia.add_city(kuala_lumpur)
    print(type(kuala_lumpur))
    for city_name in ["Melbourne", "Canberra", "Sydney"]:
        add_city_to_country(City.name_to_cities[city_name][0], "Australia", "AUS")

def test_example_countries() -> None:
    """
    Assuming the correct countries have been created, runs a small test.
    """
    Country.name_to_countries["Australia"].print_cities()


if __name__ == "__main__":
    create_example_countries()
    test_example_countries()
