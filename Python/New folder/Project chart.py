from Project import M1, M2
import xlsxwriter

book2 = xlsxwriter.Workbook('D://Prog/Python/New Folder/Chart.xlsx')
heading = book2.add_format({'bold':True,'font_color':'yellow','bg_color':'blue','font_size':15})
finalSheet = book2.add_worksheet('graphs')

print('Generating final excel with graphs')

finalSheet.write("A1","Domain",heading)
finalSheet.write("B1","URL",heading)
finalSheet.write("C1","Keyword",heading)
finalSheet.write("D1","Density",heading)

finalSheet.write("A2",M1[0][0])
finalSheet.write("B2",M1[0][1])
finalSheet.write("C2",M1[0][2])
finalSheet.write("D2",M1[0][3])

finalSheet.write("A3",M1[1][0])
finalSheet.write("B3",M1[1][1])
finalSheet.write("C3",M1[1][2])
finalSheet.write("D3",M1[1][3])

finalSheet.write("A4",M1[2][0])
finalSheet.write("B4",M1[2][1])
finalSheet.write("C4",M1[2][2])
finalSheet.write("D4",M1[2][3])

chart1 = book2.add_chart({'type':'line'})
chart1.set_title({'name':'Results of url analysis of 1st worksheet'})
chart1.set_x_axis({'name':'word'})
chart1.set_y_axis({'name':'density'})
chart1.add_series({'values':'=graphs!$D2:$D4'})
finalSheet.insert_chart("B6",chart1)
#####################################

finalSheet.write("A24","Domain",heading)
finalSheet.write("B24","URL",heading)
finalSheet.write("C24","Word",heading)
finalSheet.write("D24","Density",heading)

finalSheet.write("A25",M2[0][0])
finalSheet.write("B25",M2[0][1])
finalSheet.write("C25",M2[0][2])
finalSheet.write("D25",M2[0][3])

finalSheet.write("A26",M2[1][0])
finalSheet.write("B26",M2[1][1])
finalSheet.write("C26",M2[1][2])
finalSheet.write("D26",M2[1][3])

finalSheet.write("A27",M2[2][0])
finalSheet.write("B27",M2[2][1])
finalSheet.write("C27",M2[2][2])
finalSheet.write("D27",M2[2][3])

chart2 = book2.add_chart({'type':'pie'})
chart2.set_title({'name':'Results of url analysis of 2nd woksheet'})
chart2.set_x_axis({'name':'word'})
chart2.set_y_axis({'name':'density'})
chart2.add_series({'values':'=graphs!$D25:$D27'})
finalSheet.insert_chart("B30",chart2)

book2.close()
