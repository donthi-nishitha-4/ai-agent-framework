def calculate(expression: str) -> str:
    """
    Executes a simple mathematical calculation safely.

    Parameters:
        expression (str): Mathematical expression (e.g., "10 * 5")

    Returns:
        str: Result of the calculation or error message.
    """
    try:
        # Remove unwanted spaces
        expression = expression.strip()

        # Allow only numbers and math operators
        allowed_chars = "0123456789+-*/(). "
        for char in expression:
            if char not in allowed_chars:
                return "Invalid calculation"

        result = eval(expression)
        return str(result)

    except Exception:
        return "Invalid calculation"
