# Double any number hold by parameter x
double = lambda x:x*2

students = [("Harsh",15),("Deepti",10),("Vishal",6)]
students.sort(key=lambda x:x[0])

result = double(6)
print(result)
print(students)