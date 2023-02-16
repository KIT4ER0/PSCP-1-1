"""Safe"""
def rodown(unlock, lock):
    """down"""
    down = 0
    while lock != unlock:
        if lock >= 25:
            lock = -1
        down += 1
        lock += 1
    return down

def roup(unlock, lock):
    """up"""
    upp = 0
    while lock != unlock:
        if lock <= 0:
            lock = 26
        upp += 1
        lock -= 1
    return upp

def main():
    """main"""
    txt_unlock = input()
    txt_lock = input()
    count = 0
    for i in range(len(txt_unlock)):
        unlock = ord(txt_unlock[i])-65
        lock = ord(txt_lock[i])-65
        if unlock != lock:
            down = rodown(unlock, lock)
            upp = roup(unlock, lock)
            if upp <= down:
                count += upp
            else:
                count += down
    print(count)
main()
