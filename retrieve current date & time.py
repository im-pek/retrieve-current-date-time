from datetime import datetime
	
dateTimeObj = datetime.now()

day = str(dateTimeObj.day)
month = str(dateTimeObj.month)
year = str(dateTimeObj.year)

print(type(day + '-' + month + '-' + year))