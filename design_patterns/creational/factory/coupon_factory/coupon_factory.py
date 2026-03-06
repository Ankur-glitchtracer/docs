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
