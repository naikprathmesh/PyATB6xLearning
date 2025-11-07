# *
# **
# ***
# ****
# *****

num = int(input("Enter No of Rows for the Triangle: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print()