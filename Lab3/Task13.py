s = input ( "enter string:")
letters = digits = 0
for ch in s:
    if ch.isalpha():
        letters +=1
    elif ch.isdigit():
        digits += 1
print (f"Letters {letters}") 
print (f"Digits {digits}")               