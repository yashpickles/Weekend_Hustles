from sympy import symbols, simplify, solve, diff, integrate, sympify, sin, cos, trigsimp, cancel
from sympy.parsing.sympy_parser import parse_expr

# Could Solve multiple mathematical problems
def solve_math_expression(expression: str, task: str = "Simplify") -> str:
    try:
        expr = parse_expr(expression)
        x = symbols('x')
        if task == 'simplify':
            return str(simplify(expr))
        elif task == 'solve':
            return str(solve(expr))
        elif task == 'differentiate':
            return str(diff(expr, x))
        elif task == 'integrate':
            return str(integrate(expr, x))
        else:
            return "Unknown task."
    except Exception as e:
        return f"Error: {e}"
    