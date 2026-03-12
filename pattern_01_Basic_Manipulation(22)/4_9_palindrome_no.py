#find reverse of that given number and compare with original number 
num = 1213
reverse = 0
while num:
    last_digit = num % 10
    reverse = reverse * 10 + last_digit
    num = num // 10
    print(last_digit)
print(reverse)