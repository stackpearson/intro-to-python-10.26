def csOppositeReverse(txt):
    reversedOrder = txt[::-1]
    reversedCase = reversedOrder.swapcase()
    return reversedCase

print(csOppositeReverse('Hello World'))