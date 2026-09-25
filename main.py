from collection_comparison_utility import exclude_by as eb

names_of_students = ["Prince","Abigail","Vivian","Hannah","Richard","Pius","Bernard"]
names_of_students_present = ["Bernard","Abigail","Richard","Pius"]

results = eb(names_of_students,names_of_students_present)
print(f"List of student not present: {results}")