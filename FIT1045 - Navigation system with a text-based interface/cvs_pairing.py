# Paste your solution from previous tasks below
"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a parser that reads a CSV file and creates instances 
of the class City and the class Country.

@file city_country_csv_reader.py
"""
import csv
from city import City
from country import Country, add_city_to_country

def create_cities_countries_from_csv(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.

    :param path_to_csv: The path to the CSV file.
    """
    #TODO
    # open the file
    with open(path_to_csv, mode="r") as csv_file:
        # read the file using DictReader
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row["population"] == "":  # set the empty population as 0
                row["population"] = 0
            city = City(row["city_ascii"], (float(row["lat"]), float(row["lng"])), row["capital"],
                        int(row["population"]), int(row["id"]))  # create city by taking data from the file
            add_city_to_country(city, row["country"], row["iso3"])  # add the city to the country


if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")
    for country in Country.name_to_countries.values():
        country.print_cities()
