import csv
recording = True
list1 = list()

for i in range(40):
    observed_counts = [0, 0, 0, 0, 0, 0]
    counter = 0
    list1 = list()
    while recording:
        if counter < 36:
            print(counter)
            a = input(">>>")
            if a == 'a':
                recording = False
            elif a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a == '6':
                list1.append(a + ',')
                counter += 1
                if a == '1':
                    observed_counts[0] += 1
                if a == '2':
                    observed_counts[1] += 1
                if a == '3':
                    observed_counts[2] += 1
                if a == '4':
                    observed_counts[3] += 1
                if a == '5':
                    observed_counts[4] += 1
                if a == '6':
                    observed_counts[5] += 1
            else:
                print("ERROR: INVALID INPUT")
        else:
            for j in range(0, 6):
                observed_counts[j] = str(observed_counts[j]/36) + ','
            with open('ap_stats_observed_counts.csv', 'a', newline='') as csvfile:
                recorder = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                recorder.writerow(observed_counts)
            break
    with open('ap_stats_raw_data.csv', 'a', newline='') as csvfile:
        recorder = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        recorder.writerow(list1)

print(list1)

