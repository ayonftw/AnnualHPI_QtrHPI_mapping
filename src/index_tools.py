"""
file: index_tools.py
author: <Aniruddha Roy (Ayon)> <ar7475@rit.edu>
course: csci141
assignment: project
date: <05 December 2022>
notes: <:)>
"""

from dataclasses import dataclass


@dataclass
class QuarterHPI:
    year: int
    qtr: int
    index: float


@dataclass
class AnnualHPI:
    year: int
    index: float


def read_state_house_price_data(filepath):
    '''
    this function reads the data and makes a dictionary with state being the key,
    dataclass QuarterHPI
    :param filepath: A string, giving the path name of a data file.
    :return: A dictionary mapping state abbreviation strings to lists of QuarterHPI objects.
    '''
    dic = {}
    lst = []
    with open(filepath) as file:
        next(file)
        for line in file:
            data = line.strip().split('\t')
            if data[3] == ".":
                    print("Data unavailable: ")
                    print(line)
            else:
                state = data[0]
                year = int(data[1])
                qtr = int(data[2])
                index = float(data[3])
                lst += [QuarterHPI(year, qtr, index)]
                if state in dic:
                    dic[state] += lst
                else:
                    dic[state] = lst
            lst = []
    return dic


def read_zip_house_price_data(filepath):
    '''
    this function reads the data and makes a dictionary with zip being the key,
    dataclass AnnualHPI
    :param filepath: A string giving the path name of a ZIP5 data file.
    :return: A dictionary mapping zip codes to lists of AnnualHPI objects.
    '''
    dic = {}
    lst = []
    count = 0
    uncounted = 0
    with open(filepath) as file:
        next(file)
        for line in file:
            data = line.strip().split('\t')
            if data[3] == ".":
                uncounted += 1
            else:
                zip = str(data[0])
                year = int(data[1])
                index = float(data[3])
                count += 1
                lst.append(AnnualHPI(year, index))
                if zip in dic:
                    dic[zip] += lst
                else:
                    dic[zip] = lst
                lst = []
    print("count: ", count, "uncounted: ", uncounted)
    return dic


def index_range(data, region):
    '''
    Starts of with 1st index in list being lowest & largest index value
    Iterates through the list and updates lowest & largest index value
    :param data: A dictionary mapping regions to lists *HPI objects
    :param region: region name.
    :return: A tuple of the *HPI objects that are respectively the low and high index values
    of the dataset.

    '''
    lst = data[region]
    smallest = lst[0].index
    largest = lst[0].index
    small = lst[0]
    large = lst[0]
    for x in lst:
        if x.index > largest:
            largest = x.index
            large = x

        if x.index < smallest:
            smallest = x.index
            small = x

    return small, large


def print_range(data, region):
    '''

    :param data: A dictionary mapping regions to lists of *HPI objects
    :param region: region name
    :return: Prints the low and high values (range) of the house price index for
    the given region
    '''
    xrange = index_range(data, region)
    print("Region: ", region)
    if hasattr(xrange[0], "qtr"):
        print("Low: year/quarter/index: ", xrange[0].year, "/", xrange[0].qtr, "/", xrange[0].index)
        print("High: year/quarter/index: ", xrange[-1].year, "/", xrange[-1].qtr, "/", xrange[-1].index)
    else:
        print("Low: year/index: ", xrange[0].year, "/", xrange[0].index)
        print("High: year/index: ", xrange[-1].year, "/", xrange[-1].index)


def print_ranking(data, heading="Ranking"):
    '''
    From a sorted list of object, this function returns the top 10 & lowest 10
    iteratively
    :param data: The data is a sorted list of objects
    :param heading:  a text message whose default value is “Ranking”.
    :return: it prints the first 10 and last 10 elements in the list.
    '''
    print(heading)
    print("The Top 10:")
    number = 1
    while number <= 10:
        for i in data[:10]:
            print(number, ":", i)
            number += 1

    print("The Bottom 10:")
    number = len(data) - 9
    while number <= len(data):
        for i in data[-10:]:
            print(number, ":", i)
            number += 1


def annualize(data):
    '''
    This function operates only on a dictionary whose value type is list of QuarterHPI objects. It
    averages those objects to create the lists of AnnualHPI objects. Since some quarterly data may be unavailable,
    it averages whatever ones actually exist, whether
    that be one, two, three or four items per year.
    :param data: A dictionary mapping regions to lists of QuarterHPI objects.
    :return: A dictionary mapping regions to lists of AnnualHPI objects.
    '''
    dmap = dict()
    for region in data:
        lst = []
        count = 0
        sum = 0
        year = data[region][0].year

        for el in data[region]:
            if el.year == year:
                count += 1
                sum += el.index
            elif el.year != year:
                average = sum / count
                annual = AnnualHPI(year, float(average))
                lst.append(annual)
                year = el.year
                count = 1
                sum = el.index

        average = sum / count
        annual = AnnualHPI(year, float(average))
        lst.append(annual)
        dmap[region] = lst
    return dmap


def main():
    region_list = []
    file = input("Enter house price index file: ")

    if "ZIP" in file:
        data = read_zip_house_price_data("data/"+file)
    else:
        data = read_state_house_price_data("data/"+file)

    region = input("Next region of interest( Hit ENTER to stop): ")
    region_list.append(region)

    while region != "":
        region = input("Next region of interest( Hit ENTER to stop): ")
        if region == "":
            break
        else:
            region_list.append(region)

    print("======================================================================")

    for i in region_list:
        print_range(data, i)
        map = annualize(data)
        print_range(map, i)
        print("Annualized Index Values for", i)
        for z in map[i]:
            print(z)


if __name__ == "__main__":
    main()
