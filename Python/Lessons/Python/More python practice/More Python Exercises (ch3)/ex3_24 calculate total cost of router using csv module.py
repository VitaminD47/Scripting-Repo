import csv
total = 0.0

with open (r'C:\Users\David\Documents\2020_router_purchase.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        row [4] = row[4].strip ('$')
        row [4] = float(row [4])
        row [3] = int(row [3])
        total += row [3] * row [4]
    print ('Total cost: $', total)

    # this is nearly identical to ex_23, except we use the csv module instead. end result should be the same.
    