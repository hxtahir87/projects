import json
import requests
import time
# Create a file response.txt in the same directory as this file
# Make sure the token has Direct Ingest permission
# Adjust the number of metrics by adjusting the 'metricNumber' below
token = "89fe74ef-d645-4b53-b104-2ef8775a31dc"
metricNumber = 2628288
myUrl = "https://intuit.wavefront.com/api/spy/points"
head = {'Authorization': 'Bearer {}'.format(token)}
response = requests.get(myUrl, headers=head, stream = True)
count = 0
#for each metric in response, print it, print the number, append it to the file response.txt
print(response.status_code)
for line in response.iter_lines():
    print(line)
    count = count + 1
    if count < metricNumber:
        metric = str(line)
        file = open("response.txt", "a+")
        file.write(metric + '\n')
        print("Total metrics\n" + str(count))
    else:
        print("Number of metrics defined reached\n")
        break
file.close()
print("Total metrics\n" + str(count))
