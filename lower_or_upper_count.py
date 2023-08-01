string='The quick Brow Fox'
# print(len(string))
upper_count=0
lower_count=0
for i in string:
    if i.isupper()==True:
        upper_count+=1
    elif i.islower()==True:
        lower_count+=1

print("No. of Upper case characters :"+str(upper_count))
print("No. of lower case characters :"+str(lower_count))
