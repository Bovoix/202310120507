from datetime import datetime
from enum import Enum
from abc import ABC, abstractmethod

# 订单状态枚举
class OrderStatus(Enum):
    CREATE = "CREATE"
    PAID = "PAID"
    SHIPPING = "SHIPPING"
    DELIVERED = "DELIVERED"
    CANCEL = "CANCEL"

# 商品类
class Product:
    def __init__(self, title: str, weight: float, description: str, price: float):
        self.__title = title
        self.__weight = weight
        self.__description = description
        self.__price = price

    def getPriceForQuantity(self, quantity: int) -> float:
        """根据数量计算商品总价"""
        return self.__price * quantity

    def getWeight(self) -> float:
        """获取商品单重"""
        return self.__weight

    def getTitle(self) -> str:
        """获取商品名称"""
        return self.__title

# 抽象支付类
class Payment(ABC):
    def __init__(self, amount: float):
        self.__amount = amount

    @property
    def amount(self) -> float:
        return self.__amount

    @abstractmethod
    def validate(self) -> bool:
        """抽象方法：验证支付有效性"""
        pass

# 支付方式子类
class Credit(Payment):
    def __init__(self, amount: float, number: str, type_: str, expire_date: str):
        super().__init__(amount)
        self.__number = number
        self.__type = type_
        self.__expire_date = expire_date

    def validate(self) -> bool:
        """验证信用卡：卡号非空、有效期未过期"""
        if not self.__number:
            return False
        try:
            expire = datetime.strptime(self.__expire_date, "%Y-%m")
            return expire >= datetime.now()
        except:
            return False

class Cash(Payment):
    def __init__(self, amount: float, cash_tendered: float):
        super().__init__(amount)
        self.__cash_tendered = cash_tendered

    def validate(self) -> bool:
        """验证现金：支付金额不小于应付金额"""
        return self.__cash_tendered >= self.amount

class WireTransfer(Payment):
    def __init__(self, amount: float, bank_id: str, bank_name: str):
        super().__init__(amount)
        self.__bank_id = bank_id
        self.__bank_name = bank_name

    def validate(self) -> bool:
        """验证转账：银行ID和名称非空"""
        return bool(self.__bank_id and self.__bank_name)

class AliPay(Payment):
    def __init__(self, amount: float, number: str):
        super().__init__(amount)
        self.__number = number

    def validate(self) -> bool:
        """验证支付宝：账号非空"""
        return bool(self.__number)

class WeixinPay(Payment):
    def __init__(self, amount: float, number: str):
        super().__init__(amount)
        self.__number = number

    def validate(self) -> bool:
        """验证微信支付：账号非空"""
        return bool(self.__number)

# 订单详情类
class OrderDetail:
    def __init__(self, product: Product, quantity: int):
        self.__product = product
        self.__quantity = quantity

    def calculateSubTotal(self) -> float:
        """计算该商品的小计金额"""
        return self.__product.getPriceForQuantity(self.__quantity)

    def calculateWeight(self) -> float:
        """计算该商品的总重量"""
        return self.__product.getWeight() * self.__quantity

    def getDetailInfo(self) -> str:
        """获取订单详情信息"""
        return f"商品：{self.__product.getTitle()}，数量：{self.__quantity}，小计：{self.calculateSubTotal():.2f}元"

# 订单类
class Order:
    def __init__(self):
        self.__create_date = datetime.now()
        self.__status = OrderStatus.CREATE
        self.__order_details = []
        self.__payment = None

    def addOrderDetail(self, detail: OrderDetail) -> None:
        """添加订单详情"""
        self.__order_details.append(detail)

    def setPayment(self, payment: Payment) -> bool:
        """设置支付方式并验证，验证通过则更新订单状态为PAID"""
        if payment.validate():
            self.__payment = payment
            self.__status = OrderStatus.PAID
            return True
        return False

    def getTotalAmount(self) -> float:
        """计算订单总金额"""
        return sum(detail.calculateSubTotal() for detail in self.__order_details)

    def getOrderInfo(self) -> str:
        """获取订单信息"""
        details = "\n  ".join([detail.getDetailInfo() for detail in self.__order_details])
        return f"创建时间：{self.__create_date.strftime('%Y-%m-%d %H:%M:%S')}\n状态：{self.__status.value}\n订单详情：\n  {details}\n总金额：{self.getTotalAmount():.2f}元"

# 客户类
class Customer:
    def __init__(self, name: str, contact: str, delivery_address: str, active: bool = True):
        self.__name = name
        self.__contact = contact
        self.__delivery_address = delivery_address
        self.__active = active
        self.__orders = []

    def createOrder(self, order: Order) -> None:
        """创建订单"""
        if self.__active:
            self.__orders.append(order)

    def getOrders(self) -> list:
        """获取客户所有订单"""
        return self.__orders

# 测试代码（回归测试用例）
if __name__ == "__main__":
    # 创建商品
    apple = Product("红富士苹果", 0.2, "新鲜水果", 5.99)
    milk = Product("纯牛奶", 1.0, "常温奶", 39.9)
    
    # 创建订单详情
    detail1 = OrderDetail(apple, 10)  # 10个苹果
    detail2 = OrderDetail(milk, 2)    # 2箱牛奶
    
    # 创建订单并添加详情
    order = Order()
    order.addOrderDetail(detail1)
    order.addOrderDetail(detail2)
    
    # 验证订单总金额
    expected_total = 5.99*10 + 39.9*2 = 59.9 + 79.8 = 139.7
    assert order.getTotalAmount() == 139.7, "订单总金额计算错误"
    
    # 创建支付方式并验证
    alipay = AliPay(139.7, "13800138000")
    assert order.setPayment(alipay) is True, "支付宝支付验证失败"
    assert order._Order__status == OrderStatus.PAID, "订单状态未更新为PAID"
    
    # 创建客户并关联订单
    customer = Customer("张三", "13800138000", "北京市海淀区XX路")
    customer.createOrder(order)
    assert len(customer.getOrders()) == 1, "客户订单创建失败"
    
    print("A1-4 测试通过！")
    print("\n订单详情：")
    print(order.getOrderInfo())