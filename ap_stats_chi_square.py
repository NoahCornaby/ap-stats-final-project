import csv

expected_counts = [6, 6, 6, 6, 6, 6]
results = []

with open('ap_stats_observed_counts.csv', 'r', newline='') as csvfile:
    recorder = csv.reader(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in recorder:
        observed_counts = []
        for i in row:
            temp = i.replace(',', '')
            temp = float(temp) * 36
            observed_counts.append(temp)
        temporary_calculations = [i - 6 for i in observed_counts]
        temporary_calculations = [j * j for j in temporary_calculations]
        temporary_calculations = [k/6 for k in temporary_calculations]
        chi_square = sum(temporary_calculations)

        """chi-square cutoff value is 11.070"""
        if chi_square > 11.070:
            results.append('no')
        else:
            results.append('yes')

print(results)
