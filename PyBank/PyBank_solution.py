import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
changes = []
previous_profit_loss = None
months = [] # list to store months

# Open and read the csv
with open(file_to_load) as input_data:
    reader = csv.reader(input_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        # Track the total months
        total_months += 1

        # Append the month to the months list
        months.append(row[0])  # Assuming the month is in the first column

        # Track the net total
        current_profit_loss = float(row[1])
        total_net += current_profit_loss
        
        # Calculate the changes in profit/loss
        if previous_profit_loss is not None:
            change = current_profit_loss - previous_profit_loss
            changes.append(change)

        # Update the previous profit/loss to current
        previous_profit_loss = current_profit_loss

# Calculate the average change across the months
if changes:
    average_change = sum(changes) / len(changes)
    average_change = round(average_change, 2)
else:
    average_change = 0  # Set to 0 if there are no changes

# Calculate the greatest increase in profits (month and amount)
if changes:
    greatest_increase = max(changes)
    greatest_increase_month_index = changes.index(greatest_increase) +1  # for month index
    greatest_increase_month = months[greatest_increase_month_index]
else:
    greatest_increase = 0
    greatest_increase_month = None  # No month available

# Calculate the greatest decrease in losses (month and amount)
if changes:
    greatest_decrease = min(changes)
    greatest_decrease_month_index = changes.index(greatest_decrease) + 1  # for month index
    greatest_decrease_month = months[greatest_decrease_month_index]
else:
    greatest_decrease = 0
    greatest_decrease_month = None  # No month available

# Generate the output summary
output = (
    f"Financial Analysis\n"

    f"----------------------------\n"
    
    f"Total Months: {total_months}\n"
    f"Total: ${round(total_net)}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${round(greatest_increase)})\n"
    f"Greatest Decrease in Losses: {greatest_decrease_month} (${round(greatest_decrease)})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)








