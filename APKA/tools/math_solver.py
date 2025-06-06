from sympy import symbols, simplify, solve, diff, integrate, sympify
from sympy.parsing.sympy_parser import parse_expr
import re

# Understand which mathematical task to address (patch == v1.5)
def get_math_task(question: str) -> str:
    q = question.lower()

    # Keyword mapping (supporting common typos and synonyms)
    keyword_map = {
        "integrate": "integrate",
        "integration": "integrate",
        "differentiate": "differentiate",
        "derivative": "differentiate",
        "derivate": "differentiate", 
        "simplify": "simplify",
        "unscramble": "simplify", 
        "solve": "solve",
        "equation": "solve"
    }

    for key, value in keyword_map.items():
        if key in q:
            return value
    return "simplify"
    

def extract_expression(question: str) -> str:
    # Match command followed by expression, e.g., "differentiate x^2 + 2x"
    match = re.search(r'(integrate|differentiate|simplify|solve|derivative|derivate|unscramble)\s+(.+)', question, re.IGNORECASE)

    if match:
        expr = match.group(2)
    else:
        # Fallback: use the full question as expression (not ideal, but prevents crash)
        expr = question


    expr = expr.replace('^', '**')  # covert ^ to * (patch == v1.4)
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)   # 2x → 2*x
    expr = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expr)   # x2 → x*2
    return expr.strip()


def solve_math_expression(question: str, task: str = None) -> str:
    try:
        expression = extract_expression(question)
        task = task or get_math_task(question)
        x = symbols('x')
        expr = sympify(expression)

        if task.lower() == 'simplify':
            return str(simplify(expr))
        elif task.lower() == 'solve':
            return str(solve(expr, x))
        elif task.lower() == 'differentiate':
            return str(diff(expr, x))
        elif task.lower() == 'integrate':
            return str(integrate(expr, x)) + "+ c" # Indefinate integral
        else:
            return "Unknown task."

    except Exception as e:
        return f"Error: {e}"
