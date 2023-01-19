import json
import requests
import time


# Create a file response.txt in the same directory as this file
# Make sure the token has Direct Ingest permission
# Adjust the number of metrics by adjusting the 'metricNumber' below

#token = input("Please enter your token")
#cluster = input("Please enter your cluster")
#thresholdDays = input("Please enter the lookback period in days. Max is 60" )
#metricNumber = int(input("Please enter the number of points you need to scan"))
token = "6de86aea-e204-48a7-9987-819342090767"
metricNumber = 10
subString = "[UNACCESSED]"
thresholdDays = 28

myUrl = "https://longboard.wavefront.com/api/spy/points?usage=true&usageThresholdDays=28"#.format(cluster, thresholdDays)
head = {'Authorization': 'Bearer {}'.format(token)}
response = requests.get(myUrl, headers=head, stream = True)

count = 0

#for each metric in response, print it, print the number, append it to the file response.txt
print(response.status_code)
for line in response.iter_lines():
    if count < metricNumber:
        metric = str(line)
        #if metric.find(subString) != -1:
        if subString in metric:
            count = count + 1
            print(metric)
            file = open("response.txt", "a+")
            file.write(metric + '\n')
            print("Total metrics\n" + str(count))
    else:
        print("Number of metrics defined reached\n")
        break
file.close()
print("Total metric points\n" + str(count))

fileOpen = open("response.txt", "r")

for line in fileOpen:
    word = line.split()[1]
    print(word)



    #x = line.split()
    #print(x)
