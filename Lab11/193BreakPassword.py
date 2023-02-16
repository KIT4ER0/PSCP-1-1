"""BreakPassword"""
import hashlib
def main():
    """main"""
    hashpassword = input()
    for i in range(0, 100000):
        val = str("%05d" %i)
        check = hashlib.sha512(val.encode("utf-8")).hexdigest().upper()
        if check == hashpassword:
            print(val)
main()
