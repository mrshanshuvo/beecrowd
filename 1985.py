# products = [
#   {1001 : 1.50},
#   {1002 : 2.50},
#   {1003 : 3.50},
#   {1004 : 4.50},
#   {1005 : 5.50},
# ]
products_total = []

n = int(input())
for i in range(n):
  a, b = map(int, input().split())
  if(a == 1001):
    b = b * 1.5
    products_total.append(b)
  elif(a == 1002):
    b = b * 2.5
    products_total.append(b)
  elif(a == 1003):
    b = b * 3.5
    products_total.append(b)
  elif(a == 1004):
    b = b * 4.5
    products_total.append(b)
  elif(a == 1005):
    b = b * 5.5
    products_total.append(b)

total = sum(products_total)

print(f"{total:.2f}")