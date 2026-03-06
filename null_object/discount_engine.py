# Problem Statement: The E-Commerce Discount Engine
# You are building a checkout system for an e-commerce platform. The system
# applies discounts to a total price based on a Coupon Code entered by the user.

# 1. The Requirements
# Every coupon must have a applyDiscount(double price) method that returns the new price.

# There are different types of coupons:
# Percentage Coupon: Takes 10% or 20% off.
# Flat Coupon: Takes a fixed $20 off.
# The system looks up a coupon in a database (or a simple Map/Dictionary) based on a string code.

# 2. The Challenge (The "Null" Problem)
# In a standard implementation, if a user enters an invalid code (like "FAKE123"),
# your lookup function will likely return null. This forces you to write code like this everywhere:
# if (coupon != null) {
#     total = coupon.applyDiscount(total);
# }

# 3. Your Task
# Implement the design pattern so that the checkout logic never has to check for null.

# Create an Interface: Define the contract for all coupons.

# Implement Real Coupons: Create the Percentage and Flat discount classes.

# Implement the Null Object: Create a NoDiscount class that implements the interface but returns the price unchanged.

# Create a Factory/Repository: Write a method getCoupon(String code) that returns a real coupon if found,
# but returns your NoDiscount object if the code is invalid.

# Why this matters
# When you finish, notice how your "Main" or "Checkout" logic becomes a clean, one-line call. 
# You’ve moved the "what happens if it's missing" logic out of the business flow and into the object structure itself.

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


