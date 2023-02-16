"""RemoveTag"""
import re
def main(txt):
    """main"""
    result = re.compile('<.*?>')
    ans = re.sub(result, ' ', txt)
    print(ans.split())
main(input())
