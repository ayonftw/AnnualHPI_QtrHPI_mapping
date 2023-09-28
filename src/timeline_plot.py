"""
file: timeline_plot.py
author: <Aniruddha Roy (Ayon)> <ar7475@rit.edu>
course: csci141
assignment: project
date: <05 December 2022>
notes: <:)>
"""

import numpy.ma as ma
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
import copy
import index_tools


def build_plottable_array(xyears, regiondata):
    '''
    builds the bridge over the gaps of unavailable data to plot.
    :param xyears: xyears is a list of integer year values
    :param regiondata: regiondata is a list of AnnualHPI objects
    :return:
    '''
    lst = []
    mask = []

    for Values in xyears:
        Mark = True
        for el in regiondata:
            if el.year == Values:
                Mark = False
                lst.append(el.index)
        if Mark:
            lst.append(1e+20)
        mask.append(Mark)
    return ma.array(lst, mask=mask, fill_value=1e+20)


def filter_years(data, year0, year1):
    '''
    filters the AnnualHPI values for all regions so that each list of values
    contains data for only the span of the given years. The order of each
    key’s list is by ascending year.
    :param data: dictionary mapping from regions to lists of AnnualHPI
    :param year0: starting year
    :param year1: ending year
    The pre-condition is year0 <= year1.
    :return: A dictionary mapping regions to lists of HPI values that are within the year0
    to year1 inclusive range. In ascending order o year
    '''
    temp_list = []
    for num in range(year0, year1 + 1):
        temp_list.append(num)
    dict = {}
    for el in data:
        dict[el] = []
        for mark in data[el]:
            if mark.year in temp_list:
                dict[el].append(mark)

    return dict


def plot_HPI(data, regionList):
    '''
    function plots a timeline from point to point over
    the time period of the data
    :param data: a dictionary mapping a state or zip code to a list of AnnualHPI objects
    :param regionlist: a list of key values whose type is string.
    :return: NoneType
    '''
    largest = 8000
    small = -1
    for el in regionList:
        if data[el][1].year > small:
            small = data[el][1].year
        if data[el][-1].year < largest:
            largest= data[el][-1].year
    years = []
    for year in range(small,largest):
        years.append(year)

    for region in regionList:
        plt.plot(years, build_plottable_array(years, data[region]))

    plt.show()


def plot_whiskers(data, regionList):
    '''
    The whiskers plotted output is found in the accompanying file of
    graph outputs.

    :param data:data is a dictionary mapping a state or zip code to a list of AnnualHPI objects.
    :param regionList: .List is a list of key values whose type is string
    :return: NoneTypeegion
    '''
    xtotal = []
    for region in regionList:
        xpart = []
        for el in data[region]:
            xpart.append(el.index)
        xtotal.append(xpart)
    plt.boxplot(xtotal, labels=regionList)
    plt.show()


def main():
    region_list = []
    file = input("Enter house price index filename: ")
    start = int(input("Enter the start year of the range to plot: "))
    end = int(input("Enter the end of the range to plot: "))
    if "ZIP" in file:
        data = index_tools.read_zip_house_price_data("data/" + file)
    else:
        data = index_tools.read_state_house_price_data("data/" + file)

    region = input("Enter next region for plots (<ENTER> to stop): ")
    region_list.append(region)

    while region != "":
        region = input("Next region of interest( Hit ENTER to stop): ")
        if region == "":
            break
        else:
            region_list.append(region)

    for i in region_list:
        index_tools.print_range(data, i)
    annual = index_tools.annualize(data)
    plot = filter_years(annual, start, end)
    plt.title("Home Price Index Comparison")
    plot_HPI(plot, region_list)
    print("Close display window to continue")
    plot_whiskers(plot, region_list)


if __name__ == "__main__":
    main()
