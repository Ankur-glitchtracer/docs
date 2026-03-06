# Problem Statement: The Coupon Factory
# Your e-commerce system is growing. Coupon data is now coming from an external source (like a database or a JSON config).
# Each entry has a type and a value.

# 1. The Challenge
# The DiscountEngine shouldn't have to know that a PercentageCoupon needs a percentage calculation
# while a FlatCoupon needs a subtraction. It definitely shouldn't be responsible for deciding to return the NoDiscountCoupon.

# 2. Your Task
# Modify your Coupons: Update PercentageCoupon and FlatCoupon to accept a value (e.g., 0.10 for 10% or 20.0 for a flat discount).

# Create the CouponFactory:
# Create a class (or a static method) called CouponFactory.
# It should have a method get_coupon(code, type, value).
# Inside this method, use a switch or if/elif block to return the correct Coupon object based on the type.

# Refactor DiscountEngine:
# The engine should now use the CouponFactory to generate its list of coupons from "raw data" (simulated by a list of dictionaries).

# 3. Example Data to "Process"
# Python
# # Simulate database records
# raw_coupon_data = [
#     {"code": "SAVE10", "type": "PERCENT", "value": 0.10},
#     {"code": "CASH20", "type": "FLAT", "value": 20.0},
# ]
# Why we are doing this:
# By the time you finish, your Business Logic (the engine) will be totally separated from your Creation Logic (the factory). If you decide to add a new BuyOneGetOne coupon later, you only change the Factory, and the Engine never even knows anything changed.

# Give it a shot—try to integrate your NoDiscountCoupon into the Factory logic as well!

from abc import ABC, abstractmethod

class Coupon(ABC):
    def __init__(self, code: str, value: float) -> None:
        self.code : str = code
        self.value : float = value

    @abstractmethod
    def applyDiscount(self, price: float) -> float:
        pass


class PercentageCoupon(Coupon):
    def applyDiscount(self, price: float) -> float:
        print(f"Applying Percentage discount of {self.value}% on the price {price}")
        return price * (1 - self.value)


class FlatCoupon(Coupon):
    def applyDiscount(self, price: float) -> float:
        print(f"Applying Flat discount of {self.value}")
        if price > self.value:
            return price - self.value
        return 0.0


class NoDiscountCoupon(Coupon):
    def applyDiscount(self, price: float) -> float:
        print("No Discount Applied")
        return price


class CouponFactory:
    def getCoupon(self, code: str, type: str, value: float) -> Coupon:
        if type == "PERCENT":
            return PercentageCoupon(code=code, value=value)
        elif type == "FLAT":
            return FlatCoupon(code=code, value=value)

        return NoDiscountCoupon(code="INVALID", value=0.0)


class DiscountEnginer:
    def __init__(self) -> None:
        self.couponFactory : CouponFactory = CouponFactory()

    def generateCoupons(self, raw_coupon_data: list[dict]) -> list[Coupon]:
        coupons: list[Coupon] = []
        for data in raw_coupon_data:
            coupons.append(self.couponFactory.getCoupon(code=data.get("code", ""), type=data.get("type", ""), value=data.get("value", 0.0)))

        return coupons

# Simulate database records
raw_coupon_data = [
    {"code": "SAVE10", "type": "PERCENT", "value": 0.10},
    {"code": "CASH20", "type": "FLAT", "value": 20.0},
    {"code": "SAVER2", "type": "APPROX", "value": 4.5},
]

engine = DiscountEnginer()
coupons = engine.generateCoupons(raw_coupon_data=raw_coupon_data)

for coupon in coupons:
    print(coupon.applyDiscount(price=60))
