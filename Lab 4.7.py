# student ID: 1201200431 #
# student Name: Tan Jun Yuan #

studnames =  ["John", "Viktor", "Mary"] [::-1]
for name in studnames:
    print(name)

studnames =  ["John", "Viktor", "Mary"]
for name in reversed(studnames):
    print(name)

studnames =  ["John", "Viktor", "Mary"]
for name in range(2,-1,-1):
    print(studnames[name])

studnames =  ["John", "Viktor", "Mary"]
studnames.append("Yasuo")
for name in studnames:
    print(name)

# studnames.reverse ... reverse list
# studnames.append  ... to add a new value
# studnames.remove  ... to remove the value