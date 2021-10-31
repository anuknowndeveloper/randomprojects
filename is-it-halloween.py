#date library to see what the day is
from datetime import date

#variable decloration
today = date.today()
todayy = str(today)
#if some parts of the variable "todayy" are 10-31 (october 31) then it tells the user yes!
if todayy[5:10] == "10-31":
    print('yes, it is halloween!')
#slight rejection
elif toddayy[5:7] == "10":
    print("it's not halloween, but it's october.")
    daysaway = 31 - int(todayy[8:10])
    print('you are: ' + daysaway + ' away from halloween!')
#total rejection
else:
    print('nope. too bad bud.')
