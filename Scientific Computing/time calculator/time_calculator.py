def add_time(start, duration, setDay=None):
	startHour = int(start[:start.find(":")])
	addHour = int(duration[:duration.find(":")])
	hours = startHour + addHour
	
	startMin = int(start[start.find(":")+1:start.find("M")-1])
	addMin = int(duration[duration.find(":")+1:])
	minutes = startMin + addMin
	
	turn_i = start[-2:]
	turn_f = turn_i
	
	countDays = hours/24
	
	week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	
	sumHour = hours
	if minutes >= 60:
		hours += 1
		sumHour = hours
		countDays = hours/24
		while minutes > 59:
			minutes -= 60
			continue
	if int(hours/12) % 2 != 0:
		if turn_i == "PM":
			turn_f = "AM"
		else:
			turn_f = "PM"
	while hours > 12:
		hours -= 12
		continue
	
	if setDay == None:
		new_time = '{}:{} {}'.format(str(hours), str(minutes).zfill(2), turn_f)
		if turn_i == "AM" and  24 <= sumHour < 48:
			new_time = '{} (next day)'.format(new_time)
		elif turn_i == "PM" and  12 <= sumHour < 36:
			new_time = '{} (next day)'.format(new_time)
		elif sumHour >=36:
			new_time = '{} ({} days later)'.format(new_time, round(countDays))
	else:
		day = int(round(countDays) + week.index(setDay.capitalize()))
		if day >= 6:
			while day > 6:
				day -= 7
				continue
			day = week[day]
		else:
			day = week[day]
			
		new_time = '{}:{} {}, {}'.format(str(hours), str(minutes).zfill(2), turn_f, day)
		if turn_i == "AM" and  24 <= sumHour < 48:
			new_time = '{} (next day)'.format(new_time)
		elif turn_i == "PM" and  12 <= sumHour < 36:
			new_time = '{} (next day)'.format(new_time)
		elif sumHour >=36:
			new_time = '{} ({} days later)'.format(new_time, round(countDays))
			
	return new_time 