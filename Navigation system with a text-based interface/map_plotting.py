"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It allows plotting an Itinerary as the picture of a map.

@file map_plotting.py
"""
from mpl_toolkits.basemap import Basemap #have to do 'pip install basemap'
import matplotlib.pyplot as plt
from itinerary import Itinerary
from city import City

# check the centre of the map
# by default, north and south america will be at the left side of the map and europe, africa, asia and oceania will be at the right of the map
def map_center(itinerary: Itinerary): 
    for city_index in range(1, len(itinerary.cities)):
        city_1 = itinerary.cities[city_index - 1]
        city_2 = itinerary.cities[city_index]
        lon1 = city_1.coordinates[1]
        lon2 = city_2.coordinates[1]
        if abs(lon1 - lon2) >= 180: # if the absolute value of the difference between two longtitude mean the path will across the pacific ocean, the side need to change.
            return -200
    return 0


def plot_itinerary(itinerary: Itinerary, projection = 'robin', line_width=2, colour='b') -> None:
    """
    Plots an itinerary on a map and writes it to a file.
    Ensures a size of at least 50 degrees in each direction.
    Ensures the cities are not on the edge of the map by padding by 5 degrees.
    The name of the file is map_city1_city2_city3_..._cityX.png.

    :param itinerary: The itinerary to plot.
    :param projection: The map projection to use.
    :param line_width: The width of the line to draw.
    :param colour: The colour of the line to draw.
    """
    #TODO
    center = map_center(itinerary) # set the center of the grapg
    m = Basemap(projection=projection, lon_0=center,resolution='c')
    m.drawcoastlines() # draw the graph
    string = 'map'
    # plot the path on the graph
    # run all the city in the list, find the distance between two city
    # for example plot shortest distance of city[0] and city[1], city[1] and city[2].....city[k-1] and city[k]
    for city_index in range(1, len(itinerary.cities)): 
        # find the latitute and longtitude of the two city
        city_1 = itinerary.cities[city_index - 1] 
        city_2 = itinerary.cities[city_index]
        lon1 = city_1.coordinates[1]
        lat1 = city_1.coordinates[0]
        lon2 = city_2.coordinates[1]
        lat2 = city_2.coordinates[0]
        # draw the clossest distance between two cities on the graph
        m.drawgreatcircle(lon1, lat1, lon2, lat2, color = colour,linewidth = line_width)
        if city_index == 1:
            string += f"_{city_1.name}_{city_2.name}"
        else:
            string += f"_{city_2.name}"
    plt.savefig(f"{string}")
    plt.close()


if __name__ == "__main__":
    # create some cities
    city_list = list()

    city_list.append(City("Melbourne", (-37.8136, 144.9631), "primary", 4529500, 1036533631))
    city_list.append(City("Sydney", (-33.8688, 151.2093), "primary", 4840600, 1036074917))
    city_list.append(City("Brisbane", (-27.4698, 153.0251), "primary", 2314000, 1036192929))
    city_list.append(City("Perth", (-31.9505, 115.8605), "1992000", 2039200, 1036178956))

    # plot itinerary
    plot_itinerary(Itinerary(city_list))
