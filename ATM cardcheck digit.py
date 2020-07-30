def remove_non_digit(s):
    # d = []
    # for c in s:
    #     if c.isdigit():
    #     d.append(int(c))
    # return d
    return [int(c) for c in s if c.isdigit()]

def print_digit(v):
    for i in v:
        print("{:^2} |".format(i),end='') #ต่อกันโดยไม่ต้องขึ้นบรรทัดใหม่เลย
    print()
    #[print("{:^2} |".format(i),end='') for i in v]


if __name__ == '__main__':
    card = '4597 7632 5230 415'
    print(card)
    card = (remove_non_digit(card))
    print_digit(range(15))
    print_digit(card)
    a = [2,1]*7 +[2]
    print_digit(a)
    print("-"*60)
    y = [(m*n) for m,n in zip(card,a)]
    print_digit(y)
    y2 = [ n if n <10 else n //10 + n%10 for n in y] #each n in y
    print_digit(y2)
    sum_y2 = sum(y2)
    print("sum = ",(sum_y2))
    r = sum_y2%10
    chk_digit = 0 if r == 0  else 10-r
    print("check digit = {}".format(chk_digit))



