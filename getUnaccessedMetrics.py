#!/usr/bin/env python3
#
# This script collects unaccessed metrics for the defined lookback period and collection period.
# It the saves the unique metric names and the number of times they were collected in count.text
# The unaccessed metrics collected are sampled so, using this script multiple times is suggested.
# Clean count.txt or save it as a different file as new samples will be appended at the end of the previous.
#
# Usage: getUnaccessedMetrics.py -c <cluster_name> -t <API_token> -l <lookback_period> -p <collection_period>
#
# htahir@vmware.com

import json
import requests
import time
import argparse
import sys

# Setting up arguments for the script

def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--cluster",
        "-c",
        help="Name of the Wavefront cluster to connect to",
        type=str,
        required=True)

    parser.add_argument(
        "--token",
        "-t",
        help="Wavefont API token with direct data ingest permission",
        type=str,
        required=True)

    parser.add_argument(
        "--lookback",
        "-l",
        default=28,
        help="Number of days to lookback for access. Maximum is 60",
        type=int)

    parser.add_argument(
        "--period",
        "-p",
        default=60,
        help="Time period in seconds the script should collect metrics for",
        type=int)

    return parser.parse_args()

# Listen to spy and collect only unaccessed metrics in response.txt

url = "https://{}.wavefront.com/api/spy/points?usage=true&usageThresholdDays={}"

def getUnaccPoints():
    myUrl = url.format(args.cluster, args.lookback)
    head = {'Authorization': 'Bearer {}'.format(args.token)}
    response = requests.get(myUrl, headers=head, stream = True)


    # If response code is not 200, give pointers to troubleshoot
    if response.status_code == 200:
        print("Connection established")
    else:
        print("Connection not established. Please verify the cluster, token and ensure the token has direct ingest permission.")

    print('Collecting unaccessed metrics for time (s): ' + str(args.period))

    startTime = time.time()

    for line in response.iter_lines():
        metric = str(line)
        subString = "[UNACCESSED]"
        if subString in metric:

            fileResponse = open("response.txt", "a+")
            fileResponse.write(metric + '\n')
            if time.time() > (startTime + args.period):
                break

    fileResponse.close()

# We have metrics with all attributes in response.txt. Lets collect only the metric names in metrics.txt
def getMetricNames():
    fileResponse = open("response.txt", "r")
    countM = 0
    for line in fileResponse:
        countM = countM + 1
        metricName = line.split()[1]
        metricName = metricName.replace('"', '')
        #print(metricName)
        metricsFile = open("metrics.txt", "a+")
        metricsFile.write(metricName + '\n')
        metricsFile.close()

    print("Total unaccessed metric names collected:\n" + str(countM))

# Now we have all of the metric names in metrics.txt. However, there could be multiple occurrences of each metric name. Let's unique-ify with the associated count
def getUniqueCount():

    print("Collecting unique metric names and their number of occurrences")

    metricsFile = open("metrics.txt", "r")
    metricFileReadLines = metricsFile.readlines()

    metricsDictionary = {}
    metricListValues = []

# For each metric name, count the number of occurrences and create a dictionary with metric name and their count
    for line in metricFileReadLines:
        metricName = line
        number = metricFileReadLines.count(metricName)
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

# Deleting files to keep disk space optimized
    print("*** Please see count.txt for the results ***")
    delResponseFile = open("response.txt","r+")
    delResponseFile.truncate(0)
    delResponseFile.close()
    delMetricsFile = open("metrics.txt", "r+")
    delMetricsFile.truncate(0)
    delMetricsFile.close()

def main():
    getUnaccPoints()
    getMetricNames()
    getUniqueCount()

if __name__ == "__main__":
    args = parse_args()
    sys.exit(main())
