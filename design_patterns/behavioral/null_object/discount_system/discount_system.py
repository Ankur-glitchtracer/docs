from abc import ABC, abstractmethod

class Coupon(ABC):
    def __init__(self, code: str) -> None:
        self.code : str = code

    @abstractmethod
    def applyDiscount(self, price: float) -> float:
        pass


class PercentageCoupon(Coupon):
    def applyDiscount(self, price: float) -> float:
        return price * 0.9


class FlatCoupon(Coupon):
    def applyDiscount(self, price: float) -> float:
        if price > 20:
            return price - 20
        return 0.0


class NoDiscountCoupon(Coupon):
    def applyDiscount(self, price: float) -> float:
        return price


class DiscountEngine:
    def __init__(self, coupons: list[Coupon]) -> None:
        self.coupons : list[Coupon] = coupons
        # self.noDiscount : Coupon = NoDiscountCoupon(code="INVALID") // don't do this. since let's say 
        # if we want to calculate how many instances where invalid coupons where entered. then we can know by
        # create new instances every time and log them. but if we use the same instance them we may not!

    def getCoupon(self, code: str) -> Coupon:
        for coupon in self.coupons:
            if coupon.code == code:
                return coupon

        return NoDiscountCoupon(code="INVALID")

code1 = "PERC10"
code2 = "FLAT20"
code3 = "FAKE30"

coupon1 = PercentageCoupon(code=code1)
coupon2 = FlatCoupon(code=code2)

coupons = [coupon1, coupon2]
discountEngine = DiscountEngine(coupons=coupons)

print(discountEngine.getCoupon(code=code3).applyDiscount(price=50.4))
print(discountEngine.getCoupon(code=code1).applyDiscount(price=50.4))


