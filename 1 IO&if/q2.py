import math

a, b, c = map(float, input().split())
delta = b * b - 4 * a * c
if delta == 0:
    print("x1=x2={:.2f}".format(-b / (2 * a)))
elif delta > 0:
    sqrt_delta = math.sqrt(delta)
    x1 = (-b + sqrt_delta) / (2 * a)
    x2 = (-b - sqrt_delta) / (2 * a)
    print("x1={:.2f}".format(x1))
    print("x2={:.2f}".format(x2))
else:
    print("此方程无实数解")
