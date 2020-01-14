import datetime

def get_date(current_date, dateFormat="%d/%m/%Y", addDays=0):
    current_date = datetime.datetime.strptime(str(current_date),"%Y-%m-%d %H:%M:%S.%f")
    addDays = int(addDays)
    print (dateFormat)
    print (addDays)
    #timeNow = datetime.datetime.now()
    if (addDays!=0):
        anotherTime = current_date + datetime.timedelta(days=addDays)
    else:
        anotherTime = current_date

    return anotherTime.strftime(dateFormat)

current_date = datetime.datetime.now()
addDays = -3 #days
output_format = '%d/%m/%Y'
output = get_date(current_date, output_format, addDays)
print (output)
