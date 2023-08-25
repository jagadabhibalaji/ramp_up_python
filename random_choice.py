import random

user_input = int(input("How many employee details do you want :"))
def employee_details():
    for i in range(user_input):
        emp_id = random.randrange(1, 9999)

        emp_loc = ('Kormangala', 'HSR Layout', 'Ballary', 'Mumbai', 'Chennai', 'Nell2ore', 'Gurgaon', 'Hyderabad')
        loc = random.choice(emp_loc)

        emp_sal = random.randrange(20000, 150000)

        yield f"Employee id :{emp_id}, Employee location :{loc}, Employee salary :{emp_sal}"

obj = employee_details()
print(next(obj))
print(next(obj))
for i in obj:
    print(i)

