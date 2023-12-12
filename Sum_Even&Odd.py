sum_even = 0
sum_odd = 0
for i in range(1,100):
    if i % 2 == 0:
        sum_even = sum_even + i
        
    else:
        sum_odd = sum_odd + i
print("The Even Sum Is_ ",sum_even)
print("The Odd Sum Is_ ",sum_odd)