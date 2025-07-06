# Greetings    --- NAME USING + METHOD
# Input amount of subjects:
#    for each one input subj name(str)
#    for each one input its grade(int)
# Store subj names and its grades in a LIST: "Math: 85"
# Create an "avg_grade" calculator
# Print each subj with its grade(One avg grade for all subjects)

#AVERAGE = sum of all the grades per subj / amount of subjects

user = str(input("Greetings there, what's your name?: "))
print("Hello there, " + user)
print("Here we are going to calculate your whole average grade which combines all of your classes")

subject_list = []    # --- stores only strings(not numeric grades - no int)
grade_list = []

while True:
    subject = input('''\nInput your subject name("done" for average): \n''')
    if subject == "done":
        for subjects in subject_list:     # --- instead of printing out like [math: 85] it will access all with no brackets
            print(subjects)
        
        if len(subject_list) > 0:
            avg_grade = sum(grade_list)/len(subject_list)
            print(f"\nAverage grade:{avg_grade}")
        
        else:
            print("No subjects entered")
        exit()

    grade = int(input("Its grade: "))
    grade_list.append(grade)
    subject_list.append(f"{subject}: {grade}")
    print(f"{subject}: {grade}")
            
