#write a python program that checks whether a student is eligible to take an exam

attendance = int(input("Enter Your Attendance Percentage: "))
if attendance >= 75:
    fees=input("Fees Paid? (Y/N): ").lower()
    if fees == "y":
       print("Eligible For Exam")
    else:
        print("Pay the Fees first then your eligible for exam")
else:
    condonation = input("Did you pay the Condonation with Exam fees?(Y/N): ").lower()
    if condonation == "y":
        print("Eligible For Exam")
    else:
        print("Pay the Fees + Condonation then your eligible for exam")

