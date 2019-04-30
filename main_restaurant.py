import datetime
import hotpot
import restaurant
# from hotpot import HotPot


my_res1 = restaurant.Restaurant('重庆小面', '面馆', 10)
my_res1.get_resInfo()

my_res1.get_resWorkingTime(9)
my_res1.get_resWorkingTime(23)
print()

# 获取当前时间
now_time = datetime.datetime.now()
print()
my_res1.get_eatNumber()
my_res1.change_eatNuber(12)
my_res1.change_eatNuber(10)


my_res = hotpot.HotPot('小明', '火锅', 10, '四川', 10)
my_res.get_resInfo()
# 正数表示入职
my_res.update_employeeNum(1)
# 负数表示离职
my_res.update_employeeNum(-1)