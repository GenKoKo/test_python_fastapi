def hello() :
    print("hello")
    return "hello"

def add(a: int, b: int) -> int:
    return a + b
    
print(f"add 1 + 2 = {add(1, 2)}")

# create two functions
def add(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b
