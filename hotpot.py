from restaurant import Restaurant


class HotPot(Restaurant):

    def __init__(self, resName, resStyle, eatNumber, hotPotStyle, employeeNum):
        super().__init__(resName, resStyle, eatNumber)
        self.hotPotStyle = hotPotStyle
        self.employeeNum = employeeNum


    def get_resInfo(self):
        print('欢迎在' + self.resName + self.hotPotStyle+ self.resStyle + '就餐\n')


    def update_employeeNum(self, update_employeeNum):
        # 更新员工人数
        if update_employeeNum < 0:
            # 小于0表示离职
            self.employeeNum = self.employeeNum + update_employeeNum
            print('离职人数：' + str(abs(update_employeeNum)) + '人，员工总人数变为' + str(self.employeeNum))
        else:
            self.employeeNum = self.employeeNum + update_employeeNum
            print('入职人数：' + str(abs(update_employeeNum)) + '人，员工总人数为' + str(self.employeeNum))
