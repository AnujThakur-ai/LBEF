def add_emp():
    """Add employee records to the list"""
    emp = []
    
    try:
        n = int(input('How many employees to add? '))
        if n <= 0:
            print("Number of employees must be positive!")
            return emp
            
        for i in range(n):
            print(f"\n--- Employee {i+1} of {n} ---")
            d = {}
            
            name = input('Enter name: ').strip()
            while not name:
                print("Name cannot be empty!")
                name = input('Enter name: ').strip()
            d['name'] = name
            
            age = 0
            while True:
                try:
                    age = int(input('Enter age: '))
                    if age < 18 or age > 100:
                        print("Age must be between 18 and 100!")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number!")
            d['age'] = age
            
            email = input('Enter email: ').strip()
            while '@' not in email or '.' not in email:
                print("Please enter a valid email!")
                email = input('Enter email: ').strip()
            d['email'] = email
            
            post = input('Enter post: ').strip()
            while not post:
                print("Post cannot be empty!")
                post = input('Enter post: ').strip()
            d['post'] = post
            
            salary = 0
            while True:
                try:
                    salary = float(input('Enter salary: '))
                    if salary <= 0:
                        print("Salary must be positive!")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number!")
            d['salary'] = salary
            
            emp.append(d)
            print(f"Added: {d['name']}, {d['post']}, ${d['salary']:,.2f}")
            
    except ValueError:
        print("Invalid input!")
        
    return emp

def display_employees(emp_list):
    """Display all employees"""
    if not emp_list:
        print("\nNo employees to display!")
        return
    
    print("\n" + "="*60)
    print(f"{'Name':<20} {'Age':<5} {'Post':<15} {'Salary':<15}")
    print("="*60)
    
    for emp in emp_list:
        print(f"{emp['name']:<20} {emp['age']:<5} {emp['post']:<15} ${emp['salary']:,.2f}")
    print("="*60)
    print(f"Total employees: {len(emp_list)}")

def search_employee(emp_list):
    """Search for an employee by name"""
    if not emp_list:
        print("\nNo employees in database!")
        return
    
    search_name = input('Enter employee name to search: ').strip().lower()
    found = False
    
    for emp in emp_list:
        if search_name in emp['name'].lower():
            print(f"\nFound: {emp['name']}")
            print(f"  Age: {emp['age']}")
            print(f"  Email: {emp['email']}")
            print(f"  Post: {emp['post']}")
            print(f"  Salary: ${emp['salary']:,.2f}")
            found = True
    
    if not found:
        print(f"No employee found with name containing '{search_name}'")

def main_menu():
    """Main menu for employee management"""
    employees = []
    
    while True:
        print("\n" + "="*40)
        print("   EMPLOYEE MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add Employees")
        print("2. Display All Employees")
        print("3. Search Employee")
        print("4. Exit")
        print("="*40)
        
        choice = input('Enter your choice (1-4): ').strip()
        
        if choice == '1':
            employees = add_emp()
        elif choice == '2':
            display_employees(employees)
        elif choice == '3':
            search_employee(employees)
        elif choice == '4':
            print("\nThank you for using Employee Management System!")
            break
        else:
            print("Invalid choice! Please enter 1-4")

if __name__ == "__main__":
    main_menu()
