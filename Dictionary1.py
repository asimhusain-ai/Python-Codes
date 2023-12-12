dict = {
    "Name": "John",
    "Age": 30,
    "City": "New York"
}
name = dict["Name"]
dict["gender"] = "Male"
City = dict["City"] = "Moradabad"
is_gender_present = "gender" in dict
print("Name:", name)
print("Is 'gender' present?", is_gender_present)
print("My Home Town Is:- ", City)
print("Age Is:- ", dict["Age"])