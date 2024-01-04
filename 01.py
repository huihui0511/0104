class FriedChicken:
    def __init__(self, name, size, price, spice_level, sauce):
        # 建構子初始化物件屬性
        self.name = name
        self.size = size
        self.price = price
        self.spice_level = spice_level
        self.sauce = sauce
    
    def display_info(self):
        # 顯示炸雞的資訊
        print(f"名稱: {self.name}")
        print(f"尺寸: {self.size}")
        print(f"價格: {self.price}")
        print(f"辣度: {self.spice_level}")
        print(f"醬料: {self.sauce}")
    
    def change_price(self, new_price):
        # 修改價格
        self.price = new_price
        print(f"{self.name} 的價格已更新為 {self.price}。")
    
    def change_spice_level(self, new_spice_level):
        # 修改辣度
        self.spice_level = new_spice_level
        print(f"{self.name} 的辣度已更改為 {self.spice_level}。")
    
    def add_extra_sauce(self, extra_sauce):
        # 增加額外醬料的
        self.sauce += f", {extra_sauce}"
        print(f"{self.name} 已添加額外醬料: {extra_sauce}。")

# 建立四個 FriedChicken 物件
chicken_1 = FriedChicken("辣味雞塊", "大份", 70, "大", "BBQ")
chicken_2 = FriedChicken("蒜香雞翅", "中份", 60, "中", "蒜味奶油")
chicken_3 = FriedChicken("原味雞排", "小份", 90, "小", "蜂蜜芥末")
chicken_4 = FriedChicken("照燒雞肉", "中份", 100, "中", "照燒醬")

# 呼叫副函式
chicken_1.display_info()
chicken_2.change_price(65)
chicken_3.change_spice_level("中")
chicken_4.add_extra_sauce("醬油")
chicken_1.display_info()
chicken_2.change_price(75)
chicken_3.change_spice_level("中")
chicken_4.add_extra_sauce("醬油")
