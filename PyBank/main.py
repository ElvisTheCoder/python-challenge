import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "budget_data.csv")

# Open the election results and read the file.
with open(file_to_load, 'r') as budget_data:

    # Read the file object.
    csvreader = csv.reader(budget_data, delimiter=',')

    # Skip the header row.
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Declare variables.
    total_months = 0
    net_profit = 0
    change = 0
    previous = 0
    change_list = []
    sum_change = 0
    average_change = 0
    greatest_increase = 0
    greatest_decrease = 0

    # Loop through each row in the CSV file and find the total number of months and the net profit.
    for row in csvreader:
        total_months += 1
        net_profit += int(row[1])
        # if the row isnt the first row, calculate the change and add it to the list

        current = int(row[1])
        if (previous != 0):
            change = current - previous
        sum_change += change
        previous  = current

        # find the greatest increase and decrease.
        if (change > greatest_increase):
            greatest_increase = change
            greatest_increase_date = row[0]
        if (change < greatest_decrease):
            greatest_decrease = change
            greatest_decrease_date = row[0]
    average_change = round(sum_change / (total_months - 1), 2)
   
# Export a text file with the results.
output_path = os.path.join("analysis", "budget_analysis.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_profit}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")




