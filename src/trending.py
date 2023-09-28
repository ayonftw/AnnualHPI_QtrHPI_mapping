"""
file: trending.py
author: <Aniruddha Roy (Ayon)> <ar7475@rit.edu>
course: csci141
assignment: project
date: <05 December 2022>
notes: <:)>
"""

from Project.src import index_tools as it


def cagr(idxlist, periods):
    '''
    Compute the compound annual growth rate, CAGR, for a period.
    :param idxlist:  2-item list of [HPI0, HPI1], where HPI0 is the index value of
    the earlier period.
    :param periods: number (N) of periods (years) between the two HPI values in the list.
    :return: ((index1/index0)^(1/N − 1) ∗ 100.
    '''
    return (((idxlist[1] / idxlist[0]) ** (1 / periods)) - 1) * 100


def calculate_trends(data, year0, year1):
    '''
    It returns a list of (region, rate) tuples sorted in descending order by the compound
    :param data: dictionary from region to a list of AnnualHPI
    :param year0: starting year
    :param year1:  ending year
    pre-condition is year0 < year1
    :return: list of (region, rate) tuples sorted in descending order by the compound
    '''
    lst = []
    for i in data.keys():
        list = []

        for j in data[i]:
            if j.year == year0:
                list.append(j.index)
            if j.year == year1:

                list.append(j.index)
                period = year1 - year0
                llen = len(list)
                if (llen != 2):
                    continue
                lst.append((i, cagr(list, period)))
                continue
    lst.sort(key=lambda x: x[1], reverse=True)
    return lst


def main():
    file = input("Enter house price index filename: ")
    start = int(input("Enter start year of interest: "))
    end = int(input("Enter ending year of interest: "))
    if "ZIP" in file:
        data = it.read_zip_house_price_data("data/"+file)
    else:
        data = it.read_state_house_price_data("data/"+file)

    annual = it.annualize(data)
    interest = calculate_trends(annual, start, end)
    it.print_ranking(interest, "Compound Annual Growth Rate")


if __name__ == "__main__":
    main()