# this uses the datetime module
# note from author : while working in networking, he says diff vendors will use diff date/time formates in their software. 
# this example is from a real production example script. the format given is 12-Jul-17.

# the objective is to manipulate and convert the date to the correct format to find out how old the IOS is.


from datetime import datetime
IOS_rel_date = '12-Jul-17'
x = IOS_rel_date.replace('-',' ')
y = datetime.strptime(x, '%d %b %y')
y.date() 
y_day = y.date() # the .date() method drops the hour and minute information
datetime.today()
datetime.today().date()
t_day = datetime.today().date()
delta = t_day - y_day # delta refers to difference
years = round(((delta.days)/365), 2)
print(years)

# reduced version of first example :

from datetime import datetime           # note for line 26 - the datetime module expects this format
IOS_rel_date = '12-Jul-17'
x = IOS_rel_date.replace('-', ' ') # replace the - in release date with blank spaces
y_day = datetime.strptime(x, '%d %b %y').date() # convert x to correct date format. %d means days, %b means months, %y means year without leading digits.
t_day = datetime.today().date() #   the today() method shows todays date and adding the .date() method drops the hour and minute information. 
delta = t_day - y_day # delta refers to difference
years = round(((delta.days)/365), 2) # rounding number of days (per delta.days) to 2 decimal places
print(years)

#output will vary based on actual date