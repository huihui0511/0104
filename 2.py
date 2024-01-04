class BeverageShopEmployee:
    def __init__(self, name, seniority, work_hours):
        # 初始化員工的屬性
        self.name = name
        self.seniority = seniority
        self.work_hours = work_hours
    
    def get_name(self):
        return self.name
    
    def get_seniority(self):
        return self.seniority
    
    def get_work_hours(self):
        return self.work_hours
    
    def calculate_monthly_salary(self, hourly_rate):
        return self.work_hours * hourly_rate
    
    def increase_work_hours(self, additional_hours):
        self.work_hours += additional_hours
    
    def increase_annual_salary(self, bonus):
        self.seniority += bonus

class Beverage:
    def __init__(self, name, price):
        # 初始化飲料的屬性
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_name(self, new_name):  # 修改飲料名稱
        self.name = new_name

    def adjust_sweetness(self, new_sweetness):  # 調整甜度
        self.sweetness = new_sweetness

    def adjust_ice_amount(self, new_ice_amount):  # 調整冰量
        self.ice_amount = new_ice_amount


class ColdBeverage(Beverage):
    def __init__(self, name, sweetness, ice_amount, price):
        super().__init__(name, price)
        # 冷飲的甜度和冰量
        self.sweetness = sweetness
        self.ice_amount = ice_amount

    def set_name(self, new_name):  # 修改飲料名稱
        self.name = new_name

    def adjust_sweetness(self, new_sweetness):  # 調整甜度
        self.sweetness = new_sweetness

    def adjust_ice_amount(self, new_ice_amount):  # 調整冰量
        self.ice_amount = new_ice_amount


class HotBeverage(Beverage):
    def __init__(self, name, sweetness, price):
        super().__init__(name, price)
        # 熱飲的甜度
        self.sweetness = sweetness

    def set_name(self, new_name):  # 修改飲料名稱
        self.name = new_name

    def adjust_sweetness(self, new_sweetness):  # 調整甜度
        self.sweetness = new_sweetness


# 測試程式碼
employee = BeverageShopEmployee("John", 2, 150)
print(f"員工名稱: {employee.get_name()}")
print(f"年資: {employee.get_seniority()} 年")
print(f"工作時數: {employee.get_work_hours()} 小時")
print(f"月薪: ${employee.calculate_monthly_salary(183)}")

employee.increase_work_hours(15)
print(f"更新後工作時數: {employee.get_work_hours()} 小時")

employee.increase_annual_salary(1)
print(f"更新後年資: {employee.get_seniority()} 年")

cold_beverage_1 = ColdBeverage("冰淇淋紅茶", "微糖", "少冰", "50")
cold_beverage_2 = ColdBeverage("蘋果綠茶", "少糖", "去冰", "40")
cold_beverage_3 = ColdBeverage("烏龍青", "無糖", "多冰", "30")

hot_beverage_1 = HotBeverage("阿華田", "無糖","45")
hot_beverage_2 = HotBeverage("熱可可", "半糖", "55")
hot_beverage_3 = HotBeverage("熱抹茶", "正常糖", "35")

print(f"冷飲名稱: {cold_beverage_1.name}, 甜度: {cold_beverage_1.sweetness}, 冰量: {cold_beverage_1.ice_amount}, 價格: ${cold_beverage_1.price}")
print(f"熱飲名稱: {hot_beverage_1.name}, 甜度: {hot_beverage_1.sweetness}, 價格: ${cold_beverage_1.price}")

cold_beverage_1.set_name("冰淇淋綠茶")
print(f"修改後冷飲名稱: {cold_beverage_1.get_name()}")

cold_beverage_1.adjust_sweetness("半糖")
print(f"調整甜度後: {cold_beverage_1.sweetness}")

cold_beverage_1.adjust_ice_amount("正常冰")
print(f"調整冰量後: {cold_beverage_1.ice_amount}")

hot_beverage_3.set_name("紅豆拿鐵")
print(f"修改後熱飲名稱: {hot_beverage_3.get_name()}")

hot_beverage_3.adjust_sweetness("無糖")
print(f"調整甜度後: {hot_beverage_3.sweetness}")
