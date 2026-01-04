import os

# Create a dictionary to hold all the summary data. This structure is created once
daily_summary = {
    "total_orders": 0,
    "Orders In-Restaurant": 0,
    "Orders Takeaway": 0,
    "in_restaurant_items": {
        "Hummous": 0, "Fool": 0, "Falafel": 0, "Tea": 0, "Cola": 0, "Water": 0
    },
    "takeaway_items": {
        "Hummous": 0, "Fool": 0, "Falafel": 0, "Tea": 0, "Cola": 0, "Water": 0
    }
}


##this is variables for read multiple files in same path
directory = "."
# A single dot "." refers to the current directory where the script is running.
all_files = os.listdir(directory)
# Get a list of all file and directory names in the specified path.

T=open("Output.txt", "w")## this file to write all of output in its

for filename in all_files:
    if filename.endswith(".txt"):
        filepath = os.path.join(directory, filename)##this line to reach any file in this path

        with open(filepath, "r") as file:
            lines = file.readlines()

            if not lines:
                continue

            order_type = lines[0].strip()

            if order_type == "In":
                # Increment the counters for in-restaurant and total orders.
                daily_summary["Orders In-Restaurant"] += 1
                daily_summary["total_orders"] += 1
                for line in lines[1:]:## this is to know the order in second line to end without first line
                    # We Clean any line to remove any whitespace.
                    cleaned_line = line.strip()
                    if cleaned_line:
                        # Split the line by the comma to get details
                        parts = cleaned_line.split(',')
                        if len(parts) == 3 and parts[1].isdigit() > 0  and parts[0] in daily_summary["in_restaurant_items"] :
                            item_name = parts[0]
                            quantity = int(parts[1])
                            daily_summary["in_restaurant_items"][item_name] += quantity
                        else :
                            print(f"your input in    {cleaned_line}    of Orders in resturant are invalid")
                            T.write(f"your input in    {cleaned_line}    of Orders in resturant are invalid\n")

            elif order_type == "Out":
                # Increment the counters for takeaway and total orders.
                daily_summary["Orders Takeaway"] += 1
                daily_summary["total_orders"] += 1
                for line in lines[1:]:
                    cleaned_line = line.strip()
                    if cleaned_line:
                        parts = cleaned_line.split(',')
                        if len(parts) == 3 and parts[1].isdigit() and parts[0] in daily_summary["takeaway_items"]:
                            item_name = parts[0]
                            quantity = int(parts[1])
                            daily_summary["takeaway_items"][item_name] += quantity # Update the count in the takeaway items dictionary.
                        else :
                            print(f"your input in    {cleaned_line}    of Orders takeway are invalid")
                            T.write(f"your input in   {cleaned_line}   of Orders takeway are invalid\n")

# --- PRINT THE FINAL SUMMARY REPORT ---
item_units = {
    "Hummous": "dishes",
    "Fool": "dishes",
    "Falafel": "portions",
    "Tea": "cups",
    "Cola": "cans",
    "Water": "bottles"
}

print("Daily Sales Summary:")
T.write("\n Daily Sales Summary:\n")
print("--------------------")
T.write("--------------------\n")
print(f"Total orders: {daily_summary['total_orders']}")
T.write(f"Total orders: {daily_summary['total_orders']}\n")

# Print the 'In-Restaurant' part in terminal and file

print(f"Orders In-Restaurant: {daily_summary['Orders In-Restaurant']}")
T.write(f"Orders In-Restaurant: {daily_summary['Orders In-Restaurant']}\n")
for item, quantity in daily_summary['in_restaurant_items'].items():
    unit = item_units[item]
    print(f"\t{item} ({unit}): {quantity}")
    T.write(f"\t{item} ({unit}): {quantity}\n")

# Print the 'Takeaway' part in terminal and file.

print(f"Orders Takeaway: {daily_summary['Orders Takeaway']}")
T.write(f"Orders Takeaway: {daily_summary['Orders Takeaway']}\n")
for item, quantity in daily_summary['takeaway_items'].items():
    unit = item_units[item]
    print(f"\t{item} ({unit}): {quantity}")
    T.write(f"\t{item} ({unit}): {quantity}\n")



T.close()