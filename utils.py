def check_float(value):
    try:
        value = float(value)
        return True
    except ValueError:
        return False
