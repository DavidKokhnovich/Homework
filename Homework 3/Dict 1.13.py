my_dict = {"book": "worm", "white": "black", "cat": "dog"}
if my_dict.get("white", False) != False:
    print("Есть")
else:
    print("Нет")
