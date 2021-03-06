from Project import L7,L8
import xlsxwriter

workbook2=xlsxwriter.Workbook('D://Prog/Python/result.xlsx')
heading=workbook2.add_format({'bold':True,'font_color':'red','bg_color':'yellow','font_size':15})
resultWorksheet=workbook2.add_worksheet('result')
print('generating result excel')
resultWorksheet.write("A1","Domain",heading)
resultWorksheet.write("B1","URL",heading)
resultWorksheet.write("C1","Word",heading)
resultWorksheet.write("D1","Density",heading)

resultWorksheet.write("A2",L7[0][0])
resultWorksheet.write("B2",L7[0][1])
resultWorksheet.write("C2",L7[0][2])
resultWorksheet.write("D2",L7[0][3])


resultWorksheet.write("A3",L7[1][0])
resultWorksheet.write("B3",L7[1][1])
resultWorksheet.write("C3",L7[1][2])
resultWorksheet.write("D3",L7[1][3])


chart1=workbook2.add_chart({'type':'pie'})
chart1.set_title({'name':'Results of url analysis'})
chart1.set_x_axis({'name':'word'})
chart1.set_y_axis({'name':'density'})
chart1.add_series({'values':'=result!$D2:$D3'})
resultWorksheet.insert_chart("B8",chart1)



#-----------------------------------



resultWorksheet.write("A24","Domain",heading)
resultWorksheet.write("B24","URL",heading)
resultWorksheet.write("C24","Word",heading)
resultWorksheet.write("D24","Density",heading)

resultWorksheet.write("A25",L8[0][0])
resultWorksheet.write("B25",L8[0][1])
resultWorksheet.write("C25",L8[0][2])
resultWorksheet.write("D25",L8[0][3])


resultWorksheet.write("A26",L8[1][0])
resultWorksheet.write("B26",L8[1][1])
resultWorksheet.write("C26",L8[1][2])
resultWorksheet.write("D26",L8[1][3])

resultWorksheet.write("A27",L8[2][0])
resultWorksheet.write("B27",L8[2][1])
resultWorksheet.write("C27",L8[2][2])
resultWorksheet.write("D27",L8[2][3])


chart2=workbook2.add_chart({'type':'pie'})
chart2.set_title({'name':'Results of url analysis'})
chart2.set_x_axis({'name':'word'})
chart2.set_y_axis({'name':'density'})
chart2.add_series({'values':'=result!$D25:$D27'})
resultWorksheet.insert_chart("B33",chart2)

workbook2.close()
