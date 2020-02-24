# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
from csv import reader


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f'{self.name} is located on latitude {self.lat} and longitude {self.lon}'


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.

print("\n", "=" * 70, sep="\n")
print("Initializing Google-fu! 3... 2... 1... haha")
print("=" * 70, "\n")

# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []


def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list

    # open csv and read file
    with open("cities.csv") as us_cities:
        '''
        with open("cities.csv") as us_cities:
        works only when you are running the code on teh cmd using 'python <filename>'
        '''
        # use reader to use file
        read_file = reader(us_cities)
        '''
        # use DictReader instead of reader to automaticallyconvert output to array
        cities_data = DictReader(us_cities)
        '''
        # convert to list
        cities_data = list(read_file)
        # exclude the first row which holds the header
        for row in cities_data[1:]:
            cities.append(City(row[0], float(row[3]), float(row[4])))

    # verify that file has been closed automatically after reading
    print(us_cities.closed)  # should be True
    return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#


def range_format(a, b):
    # This function will account for the condition above
    if a > b:
        return range(b, a)
    else:
        return range(a, b)

# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = [city for city in cities if (
        int(city.lat) in range_format(lat2, lat1) and int(city.lon) in range_format(lon2, lon1))]

    # TODO Ensure that the lat and lon values are all floats
    # Go through each city and check to see if it falls within
    # the specified coordinates.

    return within


def take_input():
    '''
    using list comprehension to read input,
    then remove leading or trailing spaces with strip(), if any
    and convert to int, in any case input is str or float
    '''
    pair1 = [pair.strip() for pair in input(
        "\nEnter first coordinate pair in form of lat,lon \n").split(",")]
    pair2 = [pair.strip() for pair in input(
        "\nEnter second coordinate pair in form of lat,lon \n").split(",")]

    if len(pair1) == 2 and len(pair2) == 2:
        print("Correct!")
        print(pair1, pair2, sep="\n")
        print(cityreader_stretch(int(pair1[0]), int(
            pair1[1]), int(pair2[0]), int(pair2[1]), cities))
    else:
        print("Seems like you did not specify the inputs correctly. Take a look", end=" ")
        print(pair1, pair2, sep="\n")
        take_input()


# read user input
take_input()
