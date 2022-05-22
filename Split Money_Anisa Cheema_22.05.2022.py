#Splitting Money_Anisa Cheema_22.05.2022
#Input
#number of persons
#amount paid by persons
#names of persons
  

persons_number = int(input("Number of Participants: "))
persons_name = input("\nNames of the Participants:  ")
income_source = input("\nWhat is source of Participants income: ")
expense_reason = input("\nWhat is the reason for contribution/money spliting: ")
total_funds = float(input("\nFunds already in hand:  "))
expense = float(input("\nAmount paid by persons/overall Cost: "))
share_per_person = expense / persons_number
print ("\n",persons_name, "will pay individually",share_per_person)

#output
#names of person
#net balance
balance_left = total_funds - expense
print ("\nNet Balance / Remaining balance after deductions:", balance_left)