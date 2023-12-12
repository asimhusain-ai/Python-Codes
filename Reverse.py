def reverse(x):
    remainder = 0
    while x > 0:
        lastdigit = x % 10
        remainder = remainder * 10 + lastdigit
        x = x // 10
    print("The Reverse Is:- ",remainder)
reverse(324)