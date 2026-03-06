# The Interpreter Design Pattern is essentially about defining a grammar for a simple language and providing an evaluator to process it.

# The Challenge: The "Smart Home" Rule Engine
# Imagine you are building a backend for a Smart Home Hub. Users want to create custom automation rules using simple logic.

# The Problem Statement
# You need to build a system that can evaluate Boolean Expressions entered by a user as a string. 
# These expressions determine if an action (like turning on a heater) should trigger based on sensor data.

# The Constraints:
# Variables: Your system should handle variables like TEMP, HUMIDITY, and TIME.
# Operations: You must support > (Greater Than), < (Less Than), and == (Equals).
# Logic: You must support AND and OR to combine conditions.

# Example Scenario
# A user inputs the following rule: "TEMP > 30 AND HUMIDITY > 70"

# Your engine should:
# Parse this string into a tree of "Expression" objects.
# Assign current values (e.g., TEMP = 32, HUMIDITY = 75).
# Evaluate the tree to return a final Boolean result (in this case, true).

# How to Approach the Implementation
# If you want to try this from scratch without looking at the "official" pattern first, follow these steps:
# Define the Interface: Create a common interface or abstract class (e.g., Expression) 
# with a method interpret(Context context). The Context will hold your sensor data.

# Terminal Expressions: Create classes for the "leaves" of your tree—things that don't need further evaluation, like a Number or a Variable.

# Non-Terminal Expressions: Create classes for the "operators" like AndExpression or GreaterThanExpression.
# These will hold references to other expressions.

# The Parser: (This is the hard part!) Write a small piece of code that takes the string "TEMP > 30 AND HUMIDITY > 70" and
# turns it into a nested object structure.

# Why this pattern?
# Once you finish, you'll notice that adding a new rule (like a NOT operator) doesn't require changing your existing logic
# you just add a new class. That’s the "magic" of the Interpreter pattern.

from abc import ABC, abstractmethod

class Context:
    def __init__(self, data: dict) -> None:
        self.data: dict = data # e.g., {"TEMP": 32, "HUMIDITY": 75}

    def get_value(self, name: str) -> int:
        return self.data.get(name, 0)


class Expression(ABC):
    @abstractmethod
    def interpret(self, context: Context) -> bool:
        pass

# Leaf Expressions
class NumberExpression(Expression):
    def __init__(self, value: int) -> None:
        self.value: int = value

    def interpret(self, context: Context) -> int:
        return self.value


class VariableExpression(Expression):
    def __init__(self, name: str) -> None:
        self.name: str = name

    def interpret(self, context: Context) -> int:
        return context.get_value(name=self.name)


# Non-Leaf Expressions
class AndExpression(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left: Expression = left
        self.right: Expression = right

    def interpret(self, context: Context) -> bool:
        return self.left.interpret(context=context) and self.right.interpret(context=context)


class OrExpression(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left: Expression = left
        self.right: Expression = right

    def interpret(self, context: Context) -> bool:
        return self.left.interpret(context=context) or self.right.interpret(context=context)


class NotExpression(Expression):
    def __init__(self, expression: Expression) -> None:
        self.expression: Expression = expression

    def interpret(self, context: Context) -> bool:
        return not self.expression.interpret(context=context)


class GreaterThanExpression(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left: Expression = left
        self.right: Expression = right

    def interpret(self, context: Context) -> bool:
        return self.left.interpret(context=context) > self.right.interpret(context=context)


class EqualExpression(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left: Expression = left
        self.right: Expression = right

    def interpret(self, context: Context) -> bool:
        return self.left.interpret(context=context) == self.right.interpret(context=context)


class LessThanExpression(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left: Expression = left
        self.right: Expression = right

    def interpret(self, context: Context) -> bool:
        return self.left.interpret(context=context) < self.right.interpret(context=context)


class Parser:
    def __init__(self, input: str) -> None:
        self.input: str = input

    def _parse(self) -> Expression:
        expressions = self.input.split()

        def comparison():
            left_name = expressions.pop(0)
            operator = expressions.pop(0)
            right_val = expressions.pop(0)

            left_expression = VariableExpression(name=left_name)
            right_expression = NumberExpression(value=int(right_val))

            if operator == ">": return GreaterThanExpression(left=left_expression, right=right_expression)
            if operator == "==": return EqualExpression(left=left_expression, right=right_expression)
            return LessThanExpression(left=left_expression, right=right_expression)

        logical_operator = expressions[0]
        if logical_operator == "NOT":
            expressions.pop(0)
            final_expression = NotExpression(expression=comparison())
        else:
            final_expression = comparison()

        while expressions:
            logical_operator = expressions.pop(0)
            right_comparision = comparison()

            if logical_operator == "AND":
                final_expression = AndExpression(left=final_expression, right=right_comparision)
            elif logical_operator == "OR":
                final_expression = OrExpression(left=final_expression, right=right_comparision)

        return final_expression
    
# Setup
context = Context({"TEMP": 32, "HUMIDITY": 75})
parser = Parser("TEMP > 30 AND HUMIDITY > 70")

# Execute
tree = parser._parse()
result = tree.interpret(context)

print(f"Is the rule triggered? {result}") # Should be True


