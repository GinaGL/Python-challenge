import csv

read_fpath = r'C:\Users\gawin\Documents\GitHub\Python-challenge\PyBank\Resources\budget_data.csv'
write_fpath = r'C:\Users\gawin\Documents\GitHub\Python-challenge\PyBank\Analysis\Output.txt'


total_months = 0
total_PL= 0 
value = 0 
change = 0 
profit = []
dates = []

with open(read_fpath, "r", newline="" )as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    next(csvreader)

    First_row = next(csvreader)
    total_months +=1
    total_PL +=int(First_row[1])
    value=int(First_row[1])

    for row in csvreader:
        dates.append(row[0])
        change= int(row[1]) -value
        profit.append(change)
        value=int(row[1])

        total_months+=1
        total_PL=total_PL+int(row[1])

        greatest_increase=max(profit)
        greatest_index=profit.index(greatest_increase)
        greatest_date=dates[greatest_index]

        greatest_decrease=min(profit)
        worst_index=profit.index(greatest_decrease)
        worst_date=dates[worst_index]

        avg_change = round(sum(profit)/len(profit),2)

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_PL)}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {worst_date} (${greatest_decrease})")

output= open(write_fpath, "w", newline="")
output.write("Financial Analysis\n")
output.write("---------------------\n")
output.write(f"Total Months: {str(total_months)}\n")
output.write(f"Total: ${str(total_PL)}\n")
output.write(f"Average Change: ${str(round(avg_change,2))}\n")
output.write(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})\n")
output.write(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})\n")
output.close()

