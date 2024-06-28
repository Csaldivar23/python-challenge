# adding modules
import os 
import csv

# setting variables and counters
total_months = 0
net_total = 0
entire_period = 0
average_change = 0
previous_profit_loss = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""
changes = []

# creating path to budget data csv file
csvpath = os.path.join("..", "Resources", "budget_data.csv")
with open(csvpath) as csvfile:

# reading csv file and setting header
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")

# retrieving data for month and net totals
    for row in csvreader:
        print(row) # printing to make sure csv file is being retrieved
        date = row[0]
        profit_losses = int(row[1])

        total_months = total_months + 1

        net_total += profit_losses
        
        # calculating profit/losses changes over entire period
        if total_months > 1:
            change = profit_losses - previous_profit_loss
            entire_period += change
            changes.append(change)
            
            # greatest increase and decrease for entire period
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date
        
        # update previous profit/loss
        previous_profit_loss = profit_losses

# calculating average profit/losses change
if total_months > 1:
    average_change = entire_period / (total_months - 1)

# print financial analysis
print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# export the results to a text file
output_path = os.path.join("..", "Analysis", "Financial_Analysis.txt")
with open(output_path, 'w') as txtfile:
        txtfile.write("Financial Analysis\n")
        txtfile.write(f"Total Months: {total_months}\n")
        txtfile.write(f"Total: ${net_total}\n")
        txtfile.write(f"Average Change: ${average_change:.2f}\n")
        txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
        txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")