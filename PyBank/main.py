import csv

# Define csv_file
csv_file = "budget_data.csv"

# Make Variables for fin data
total_months = 0
net_total = 0
prev_profit = None
profit_changes = []
months = []

# Read CSV
with open(csv_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    for row in csvreader:
        # Get data out of CSV
        date, profit_loss = row[0], int(row[1])

        # Calc total months
        total_months += 1
        
        #calc total profit
        net_total += profit_loss
        
        # Calc change in profit from prev month
        if prev_profit is not None:
            profit_change = profit_loss - prev_profit
            profit_changes.append(profit_change)
            months.append(date)
        
        prev_profit = profit_loss
        
# Calc avg change
avg_change = sum(profit_changes)/len(profit_changes)

# Find the greatest increase and decrease
greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)

# Date the high and low
greatest_increase_date = months[profit_changes.index(greatest_increase)]
greatest_decrease_date = months[profit_changes.index(greatest_decrease)]

# Print Analysis results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease}")

# Define the path to the output text file
output_file = "financial_analysis.txt"

# Write the analysis results to the text file
with open(output_file, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_total}\n")
    textfile.write(f"Average Change: ${avg_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Losses: {greatest_decrease_date} (${greatest_decrease})\n")

print("Financial analysis has been exported to 'financial_analysis.txt'.")