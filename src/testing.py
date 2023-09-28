# import trending as t

'''task 0 test'''
# data = index_tools.read_state_house_price_data( "HPI_AT_state.txt")
# (data["NY"][:6])

# data = index_tools.read_zip_house_price_data( "HPI_AT_ZIP5.txt")
# print(data)
# print(data['14610'][:3])
# data = index_tools.read_state_house_price_data('HPI_PO_state.txt')
# print(index_tools.index_range( data, "NY"))
# index_tools.print_range( data, "NY" )

# data = index_tools.read_state_house_price_data( "data/HPI_PO_state.txt")
# year = 1998
# qtr = 1
# index_tools.print_ranking(period_ranking.quarter_data( data, year, qtr), str( year) + "/Q" + str( qtr) + " Quarterly Ranking"  )

# data = index_tools.read_state_house_price_data("HPI_PO_state.txt")
# annual = index_tools.annualize( data )
# print(annual["NY"][:3])

'''task 1'''
# data = index_tools.read_state_house_price_data("HPI_PO_state.txt")
# qd = period_ranking.quarter_data( data, 1998, 2)
# print(qd[:2])
#
# data = index_tools.read_state_house_price_data( "HPI_PO_state.txt")
# annual = index_tools.annualize( data )
# p=period_ranking.annual_data( annual, 2003)
# print(p)

'''task 2'''
# p= t.cagr((80.26, 110.3), 10)
# print(p)


'''task 3'''
# data = index_tools.read_zip_house_price_data("HPI_AT_ZIP5.txt")
# yValues = timeline_plot.build_plottable_array([i for i in range(1999,
# 2012)], data[’16034’])