import pandas
import calendar
from datetime import date
import os

today = date.today()

current_day = today.day
month = today.month
year = today.year

day_in_month = calendar.monthrange(year, month)[1]

cards_list = []

with os.scandir('dbase/') as base_files:
	for find_files in base_files:
		try:
			file = find_files.name.endswith('.xlsx')
			if file == True:
				file = int(find_files.name[0:4])
				cards_list.append(file)
			else:
				pass
		except ValueError:
			pass

index_days_list = [0.0, 0.1, 0.2, 0.3, 0.4,
0.5, 0.6, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6,
2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 3.0, 3.1,
3.2, 3.3, 3.4, 3.5, 3.6, 4.0, 4.1, 4.2, 4.3, 4.4,
4.5, 4.6, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6]

month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

work_days_list = ['First shift', 'Second shift',
'Conditionally the second shift', 'Night shift', 'Sleep day',
'Day off', 'No data']

def month_names(month):
	match month:
		case 1:
			return 'January'
		case 2:
			return 'February'
		case 3:
			return 'March'
		case 4:
			return 'April'
		case 5:
			return 'May'
		case 6:
			return 'June'
		case 7:
			return 'July'
		case 8:
			return 'August'
		case 9:
			return 'September'
		case 10:
			return 'October'
		case 11:
			return 'November'
		case 12:
			return 'December'

def timesheet(card, current_day, month):
	for month_detecting in month_list:
		if month_detecting == month:
			match card:
				case card:
					day_blocks = pandas.read_excel('dbase/{0}.xlsx'.format(card), sheet_name = str(month))
					for index_days_detecting in index_days_list:
						y_axis, x_axis = str(index_days_detecting).split('.')
						y_axis, x_axis = int(y_axis), int(x_axis)
						if day_blocks.iloc[y_axis, x_axis] == current_day:
							x_axis_increase = x_axis + 8
							match day_blocks.iloc[y_axis, x_axis_increase]:
								case 1:
									return work_days_list[0]
								case 2:
									return work_days_list[1]
								case 2.5:
									return work_days_list[2]
								case 3:
									return work_days_list[3]
								case 3.5:
									return work_days_list[4]
								case 4:
									return work_days_list[5]
								case 0:
									return work_days_list[6]

def processing(card, current_day, month):
	if card in cards_list:
		today_result = timesheet(card, current_day, month)
		print(' Results by card number: {3} \n Today {0} {1}, {2}.'.format(current_day, month_names(month), today_result, card))
		if current_day == day_in_month:
			current_day = 1
			if month == 12:
				month = 1
			else:
				month += 1
			tomorrow_result = timesheet(card, current_day, month)
			print(' Tomorrow {0} {1}, {2}.\n'.format(current_day, month_names(month), tomorrow_result))
		else:
			tomorrow_result = timesheet(card, current_day + 1, month)
			print(' Tomorrow {0} {1}, {2}.\n'.format(current_day + 1, month_names(month), tomorrow_result))
	else:
		print(' Incorrect input, no such card number')

def main_start():
	art_line_a = '              _..----.._    _'
	art_line_b = "            .'  .--.    ""-.(0)_"
	art_line_c = ''"-.__.-'"'=:|   ,  _)_ \\__ . c\\''-..'
	art_line_d = '             '''"------'---''---'-"
	print('{0}\n{1}\n{2}\n{3}\n'.format(art_line_a, art_line_b, art_line_c, art_line_d))
	while True:
		try:
			card = int(input(' Enter your card number: '))
			processing(card, current_day, month)
		except ValueError:
			print(' Incorrect input, please enter numeric data')

main_start()