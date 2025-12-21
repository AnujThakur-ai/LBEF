# to take basic salary from an employee and calculate salary grade pay is double, DA 70% OF BASIC, TA is RM 200, HRA is 20 % of basic 
# formula : grade pay + da + ta+ hra


# take basic 
basic = eval (input('enter basic salary: '))

grade_pay = basic*2
da = 0.7*basic
ta = 200
hra = 0.2 * basic

#gross salary

print(f'your gross salary is : {grade_pay+da+ta+hra}')
