def reverse_num(num):
    palindrome_num = 121
    revrse_no =  0
    while num > 0:
        remainder = num % 10
        revrse_no = (revrse_no * 10) + remainder
        num = num // 10
    if revrse_no == palindrome_num:
        print("palindrom")
    if revrse_no != palindrome_num:
        print("not palindrom")
    return revrse_no

print(reverse_num(121))