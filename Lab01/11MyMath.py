"""1"""
def main():
    """Mymath"""
    import math
    text1 = math.radians(90)
    text2 = math.radians(60)
    text3 = math.radians(245**2)
    text4 = math.radians(45+135)
    text5 = (math.log(4234, 5) + math.log2(8191) + (71*math.log10(156154)))
    text6 = (math.log(777, 7) - math.log(888, 8) - math.log(999, 9))
    print((math.sin(text1) + (math.sin(text2)**2)) / (math.cos(text3) + math.cos(text4)))
    print((math.factorial(16) * math.factorial(4)) / (math.factorial(8)))
    print((15 + 25) / math.sqrt(((25 - 12)**2) + ((12 - 15)**2)))
    print(math.log10(1234**4))
    print(text5 / text6)
main()