"""Password"""
import hashlib
def main(password):
    """main"""
    print(hashlib.sha512(password).hexdigest().upper())
main(input().encode("utf-8"))
