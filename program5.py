#A company needs a program that reads employee names and their basic salary.The program should: Calculate total salary including HRA (20%) and DA (10%).Stop taking input when the user types "stop". Display each employee’s total salary at the end.

employees = []   


while True:
    name = input("Enter employee name (type 'stop' to end): ")

    if name.lower() == "stop":
        break

    salary = float(input("Enter basic salary: "))

    # Calculate allowances
    hra = 0.20 * salary
    da = 0.10 * salary
    total = salary + hra + da

    # Store result in list
    employees.append((name, total))

print("\n--- Employee Total Salaries ---")
for emp in employees:
    print(f"Employee: {emp[0]}  |  Total Salary: ₹{emp[1]:.2f}")
print(employees)