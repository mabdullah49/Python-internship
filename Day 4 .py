

student_ids = (101, 102, 103, 104)  
print("Student IDs (Immutable):", student_ids)

courses = {"Python", "AI", "ML"}  
print("Initial Courses:", courses)


courses.add("Data Science") 
print("After Adding 'Data Science':", courses)

courses.add("Python")  
print("After Trying to Add Duplicate 'Python':", courses)


courses.discard("AI")  
print("After Removing 'AI':", courses)

print("Final Course List:", courses)


