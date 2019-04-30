class Restaurant:


    def __init__(self, resName, resStyle, eatNumber):
        self.resName = resName
        self.resStyle = resStyle
        self.eatNumber = eatNumber
        self.worKingTime = '08:00-22:00'


    def get_resInfo(self):
        print('欢迎在'+self.resName + self.resStyle+'就餐\n',)


    def get_resWorkingTime(self,timeNow):
        print('本店营业时间'+self.worKingTime)


        if 8 < timeNow < 22:
            print(f'当前时间{timeNow},正在营业')
        else:
            print(f'当前时间{timeNow},已休息')


    def get_eatNumber(self):
        print('就餐人数：'+str(self.eatNumber))


    def change_eatNuber(self,eatingNum):
        if eatingNum > self.eatNumber:
            self.eatNumber = eatingNum
            print('当前就餐人数：'+str(self.eatNumber))
        else:
            print('用餐人数不可减少')