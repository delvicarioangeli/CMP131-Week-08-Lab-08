#Angelina Del Vicario
#10/30/2026
#CMP131
#Lab 8




ast=""
store = int(input("Enter number of stores"))
for i in range (store):
    sales = int(input("Enter todays sales "+ str((i+1))+" : "))
    sales = sales/100
    sales=int(sales)
    for j in range (sales):
        ast = ast + "*"
    ast = ast + "\n"
print(ast)