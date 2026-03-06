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


