'''

Find the student with highest score

Return both name and score
'''
# empty dictinary 
d = {}
while True:
    name = input('Enter student name (or type exit to stop): ')
    if name.lower() == 'exit':
        break
    score = float(input(f'Enter score for {name}: '))
    d[name] = score
    
    
def highest_score(student: dict):
    if not student:
        raise ValueError("The student dictionary is empty.")

    return {k: v for k, v in student.items() if v == max(student.values())}

if __name__ == "__main__":
    result = highest_score(d)
    print('original dictionary:', d)
    print('student with highest score:', result)