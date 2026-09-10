price = int(input())
discount = int(input())
vat = int(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(round(base,2), '$')
print(round(vat_amount,2), '$')
print(round(total,2), '$')
