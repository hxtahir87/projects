import json
import requests
import time

token = "4fcd36f0-023e-4af2-9af5-7d3043ab35ed"

myUrl = "https://intuit.wavefront.com/api/v2/alert?offset=0&limit=50000"
head = {'Authorization': 'Bearer {}'.format(token)}
response = requests.get(myUrl, headers=head).json()


for item in response['response']['items']:
    creator = item['updaterId']
    fileResponse = open("response.txt", "a+")
    fileResponse.write(creator + '\n')
    print(creator)

    fileResponse.close()


creatorsFile = open("response.txt", "r")
creatorsFileReadLines = creatorsFile.readlines()

metricsDictionary = {}
metricListValues = []

# For each metric name, count the number of occurrences and create a dictionary with metric name and their count
for line in creatorsFileReadLines:
    metricName = line
    number = creatorsFileReadLines.count(metricName)
    metricsDictionary[metricName] = number

# Sort the dictionary in descending order. It becomes a tuple. Convert it back into a dictionary.
sortedMetricsDictionary = sorted(metricsDictionary.items(), key=lambda x: x[1], reverse=True)
uniqueSortedUnaccessedMetrics = dict(sortedMetricsDictionary)

# Save the new dictionary into count.txt with metric name and its count
for unaccessedMetricsNewLine, values in uniqueSortedUnaccessedMetrics.items():
    unaccessedMetrics = unaccessedMetricsNewLine.replace("\n", "")

    countFile = open("count.txt", "a+")
    value = str(values)
    countFile.write(unaccessedMetrics + "\n" + value + "\n\n")
    countFile.close()
