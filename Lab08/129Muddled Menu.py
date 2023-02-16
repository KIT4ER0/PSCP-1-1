"""Muddled Menu"""
def main(menu):
    """main"""
    while True:
        food = input()
        if food == "DONE":
            break
        elif food == "SOMETHING'S WRONG":
            menu.clear()
        elif food == "CLOSED":
            menu.clear()
            break
        elif food[:10] == "Can't do: ":
            menu.remove(food[10:])
        else:
            food = food.split(" #")
            if food[1] == "N":
                menu.append(food[0])
            elif food[1].isnumeric():
                menu.insert(int(food[1])-1, food[0])
    print("Full Course: %s Reversed: %s" %(menu, menu[::-1]))
main([])
