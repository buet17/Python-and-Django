# # # thisdict =	{
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964
# # # }
# # # x = thisdict["model"]
# # # print(x)

# # myfamily = {
# #   "child1" : {
# #     "name" : "Emil",
# #     "year" : 2004,
# #     "joint":{"T":"Y","F":"N"}
# #   },
# #   "child2" : {
# #     "name" : "Tobias",
# #     "year" : 2007
# #   },
# #   "child3" : {
# #     "name" : "Linus",
# #     "year" : 2011
# #   }
# # } 

# # print(myfamily["child1"]["year"])

student_records = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "courses": {
            "math": 95,
            "history": 87,
            "science": 92
        }
    },
    "student2": {
        "name": "Bob",
        "age": 21,
        "courses": {
            "math": 88,
            "history": 78,
            "science": 84
        }
    },
    "student3": {
        "name": "Charlie",
        "age": 19,
        "courses": {
            "math": 92,
            "history": 90,
            "science": 88
        }
    }
}

# print(student_records["student1"]["courses"]["math"])

for x,y in student_records.items():
  print(x,y)
    # print(x,y)

#  create a nested dictionary with 3 
# fields of 3 students
# data = {
#     'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
#     'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
#     'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
# }
 
 
# # iterate all the nested dictionaries with 
# # both keys and values
# for i,j in data.items():
    
#     # display
#     print(j)

# a=200
# b=500
# c=78

# # x=lambda a,b,c:a>b>c
# # print(200,33,55)
# if a>=b and a>=c:
#     comp=a
#     print(a)
# elif b>=a and b>=c:
#     comp=b
#     print(b)
# else:
#     comp=c
#     print(c)
# print(comp)

