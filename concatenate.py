import csv

f1 = file('batch.csv', 'r')
f2 = file('upcatpassers.csv', 'r')
f3 = file('results1.csv', 'w')

c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)

masterlist = list(c2)

for hosts_row in c1:
    row = 1
    found = False
    for master_row in masterlist:
        results_row = hosts_row
        if hosts_row[0] in master_row[0]:
            results_row.append('FOUND in master list (row ' + str(row) + ')')
            found = True
            break
        row = row + 1
    if not found:
        results_row.append('NOT FOUND in master list')
    c3.writerow(results_row)

f1.close()
f2.close()
f3.close()