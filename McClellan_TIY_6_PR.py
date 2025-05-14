import csv
# Pull in the CSV file
filename = 'candy_type.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Loop through the csv file and create two lists
    candy_type = []
    candy_price = []

    for row in reader:
        candy = row[1]
        price = float(row[2])
        candy_type.append(candy)
        candy_price.append(price)



candy = {'candy': 'price', 'Chacolate candy': ['Hersheys Special Dark Zero Sugar Chocolate Bar', 'Almond Joy', 'Reeses', 'Snickers']}
print(f'{candy} must be refrigerated')

dup = []

for candy in candy_type:
    if candy_type.count(candy) > 1:
        dup.append(candy)

print('Duplicate list', dup)

overpriced = []

for price in candy_price:
    if price <= 3:
        overpriced.append(price)
print('The candy under $3', overpriced)
