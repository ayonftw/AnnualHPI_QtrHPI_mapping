"""
file: period_ranking.py
author: <Aniruddha Roy (Ayon)> <ar7475@rit.edu>
course: csci141
assignment: project
date: <05 December 2022>
notes: <:)>
"""

from Project.src import index_tools as it


def quarter_data(data, year, qtr):
    '''
    From dict data, it checks for x.year & x.qtr iteratively with respect to
    parameters, adds them to a list and sorts it in ascending order
    :param data: dictionary mapping a state region to a list of QuarterHPI
    :param year: year of interest
    :param qtr: qtr is the quarter of interest
    :return: A list of (region, HPI) tuples sorted from high value HPI to low value HPI.
    '''
    lst = []
    for state in data:
        for x in data[state]:
            if x.year == year and x.qtr == qtr:
                lst.append((state, x.index))
    lst.sort(key=lambda x: x[1], reverse=True)
    return lst


def annual_data(data, year):
    '''
    Creates a list of (region, HPI) tuples sorted from high value HPI to low value HPI
    :param data: dictionary mapping a state or zip code to a list of AnnualHPI objects
    :param year: year is the year of interest
    :return: A list of (region, HPI) tuples sorted from high value HPI to low value HPI
    '''
    lst = []
    for state in data:
        for x in data[state]:
            if x.year == year:
                lst.append((state, x.index))
    lst.sort(key=lambda x: x[1], reverse=True)
    return lst


def main():
    file = input("Enter region-based house price index filename: ")
    year = int(input("Enter year of interest for house prices: "))

    if "ZIP" in file:
        data = it.read_zip_house_price_data("data/"+file)
    else:
        data = it.read_state_house_price_data("data/"+file)

    data1 = it.annualize(data)
    data2 = annual_data(data1, year)
    it.print_ranking(data2, str(year) + "Annual Ranking")


if __name__ == "__main__":
    main()
