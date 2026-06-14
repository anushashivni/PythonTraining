# text = "Anusha@gmail.com"
# print(text.split('@')[0])

# print(text[2:4].upper())

list1=[1,2,3]

list2=["Anusha",5,6]
# list1.append(list2)
# [1, 2, 3, [4, 5, 6]]

list1.extend(list2)
# [1, 2, 3, 4, 5, 6]
# x = list1.index(2)
# 1
list1[3]="Advithi"
print(list1)

# list1.insert(3,5)
# [1, 2, 3, 5]

# list1.insert(2,5)
# [1, 2, 5, 3]

# list1.reverse()r      
# [3, 2, 1]


# for x in list1:
#     print(x)

#     age = 10
# s = "Adult" if age >= 18 else "Minor"
# print(s)

# for i in range(0,4):
#     for j in range(i):
#         print(i)

# 1
# 2
# 2
# 3
# 3
# 3

# x = 0
# while x < 100:
#     print(x)
#     x += 2
# print(x)


# for i in range(10):
#     pass
#     print(i)

# x=(1,2,3)
# print(type(x))

# print(bool(False),bool(0),bool(' '))
# x1=12

# if x1 > 10:
#   print("Above ten,")
#   if x1 > 20: #41 > 20
#     print("and also above 20!")
#   elif x1 < 5:
#      print("and also above 20!")
#   else:
#     print("but not above 20.")
# else:
#   print("Below or equal to 1")

# x=["Ap","ba","ch"]
# for i in x:
#     print(i)
#     if(i=="ba"):
#         break


dictexample = {"brand":"Anusha",
               "Model":"Ultra",
               "Year":2020
               }

print(dictexample)

for x , y in dictexample.items():
    print(x,y)

for x in dictexample:
    print(x, dictexample[x])

dictexample1 = {"brand":
               {
               "Model":"Ultra",
               "Year":2020
               },

               "brand2":
               {
                 "Model":"Low"  ,
                 "Year":2019
               }
               }

print(dictexample1)

print(dictexample1.items())
print(dictexample1["brand"]["Year"])


