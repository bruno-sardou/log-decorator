from log_decorator import log_decorator

@log_decorator
def test_function():
    return "It works!"

print(test_function())