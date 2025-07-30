#a python program to initialize a list with 10 names of your friends
friends = ["Ankit", "Bhavya", "Chirag", "Deepak", "Esha", "Farhan", "Gaurav", "Harsh", "Ishita", "Jay"]

print("First name:", friends[0])

print("Last name:", friends[-1])

print("Names from third to fifth index:", friends[3:6])

print("Names in reverse order:", friends[::-1])

print("Names from eighth to third index:", friends[8:2:-1])

# 2. Tuple operations
students = ("Rahul", "Neha", "Aman", "Priya", "Kiran")
print(students)
students_list = list(students)
students_list.append("Simran")
students_list.remove("Aman")
students = tuple(students_list)
print(students[1:4])
# Tuples are immutable; you cannot modify the value directly

# 3. Dictionary operations
student_ages = {"Rahul": 19, "Neha": 22, "Aman": 21, "Priya": 20}
for name, age in student_ages.items():
    if age > 20:
        print(name, age)
student_ages["Kiran"] = 30
print(student_ages.items())
del student_ages["Aman"]
average_age = sum(student_ages.values()) / len(student_ages)
print("Average Age:", average_age)

# 4. Even numbers from list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for num in numbers:
    if num % 2 == 0:
        print(num)

# 5. Duplicate elements in list
lst = [1, 2, 3, 2, 4, 5, 1, 6]
duplicates = set([x for x in lst if lst.count(x) > 1])
print(duplicates)

# 6. Reverse a string
s = "hello"
print(s[::-1])

# 7. Fibonacci series till 5th term
a, b = 0, 1
for _ in range(5):
    print(a)
    a, b = b, a + b

# 8. Replace contents of txt file
with open("data.txt", "w") as f:
    f.write("Hi, I am currently pursuing my BTech from Jaypee.")

# 9. Reverse lines of a file
with open("reverse.py", "r") as f:
    lines = f.readlines()
for line in reversed(lines):
    print(line.strip())

# 10. Odd elements using list comprehension
lst = [1, 2, 3, 4, 5, 6]
odds = [x for x in lst if x % 2 != 0]
print(odds)

# 11. Count characters in a file
with open("data.txt", "r") as f:
    content = f.read()
print("Character count:", len(content))

# 12. Anagram finder
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
from collections import defaultdict
anagrams = defaultdict(list)
for word in words:
    key = "".join(sorted(word))
    anagrams[key].append(word)
for group in anagrams.values():
    if len(group) > 1:
        print(group)

