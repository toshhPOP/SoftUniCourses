def age_assignment(*args,**kwargs):

    age = {}
    for name in args:
        for letter,years in sorted(kwargs.items(),key=lambda x: x[0]):
            if name.startswith(letter):
                age[name] = int(years)
    return age
# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))