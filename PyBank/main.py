import csv
budget_file1 = "/raw_data/budget_data_1.csv"
budget_output1 = "analysis/budget_analysis_1.txt"

month_total = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0

with open(budget_file1) as budget_data:
    reader = csv.DictReader(budget_data)
    for row in reader:
        month_total = month_total + 1
        total_revenue = total_revenue + int(row["Revenue"])
        revenue_change = int(row["Revenue"]) - prev_revenue
        prev_revenue = int(row["Revenue"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

revenue_avg = sum(revenue_change_list) / len(revenue_change_list)
analysis_output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {month_total}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(analysis_output)

# Export the results to text file
with open(budget_output1, "w") as txt_file:
    txt_file.write(analysis_output)
