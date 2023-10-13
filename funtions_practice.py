def hello():
    print("Hello from inside a file!")


def pack(item1, item2, item3):
    return [item1, item2, item3]


def eat_lunch(lunchbox):
    number_of_foods = len(lunchbox)
    if number_of_foods == 0:
       print("lunchbox is empty")
    elif number_of_foods == 1:
     first = (f"We are eating {lunchbox[0]}.")
     print(first)
    else:
       first = (f"first we eat {lunchbox[0]}.")
       x = 1
       print(first)
       while x < number_of_foods:
             print(f"then we eat {lunchbox[x]}")
             x += 1


hello()
print(pack(
    1, 2, 3))
eat_lunch(["banana", "sandwich", "Salmon"])