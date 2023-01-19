import requests
import json
import time

#Global queries for Wavefront customer health check calculations
#ly is abbreviated for 'last year'

dir_query = "mavg(1d, rawsum(align(1m,mean,rate(ts(~collector.*points.reported or ~externalservices.*.points)))))"
dir_ly_query = "lag(365d, mavg(1d, rawsum(align(1m,mean,rate(ts(~collector.*points.reported or ~externalservices.*.points))))))"

dsr_query = "mavg(7d, rawsum(align(1m,mean,rate(ts(~query.summaries_scanned)))))"
dsr_ly_query = "lag(365d, mavg(7d, rawsum(align(1m,mean,rate(ts(~query.summaries_scanned))))))"

users_query = "ts(~wavefront.users.total)"
users_ly_query = "lag(365d, ts(~wavefront.users.total))"

users30_query = "mavg(7d, ts(~wavefront.users.actives.30day))"
users30_ly_query = "lag(365d, mavg(7d, ts(~wavefront.users.actives.30day)))"

users7_query = "mavg(7d, ts(~wavefront.users.actives.7day))"
users7_ly_query = "lag(365d, mavg(7d, ts(~wavefront.users.actives.7day)))"

db_query = "ts(~wavefront.dashboards.total)"
db_ly_query = "lag(365d, ts(~wavefront.dashboards.total))"

alert_query = "ts(~wavefront.alerts.all)"
alert_ly_query = "lag(365d, ts(~wavefront.alerts.all))"

while True:
    score = 0
    print("\n\n\n======== Wavefront Customer Health Check ========\n\n\n")
#First, we query current metric, then from exactly an year ago. After that we locally compute the difference and percentage

    cluster = input("Please enter name of the Wavefront cluster. Example intuit, box, groupon etc\n")
    Token = input("Please enter your token\n")

    def dir_calc():

        global score

        print("\n\n\n======== Data Ingest Rate ========\n")

        myUrl = "https://{}.wavefront.com/api/v2/chart/api?q={}&s={}&g=m&view=METRIC&sorted=false&cached=true&includeObsoleteMetrics=true".format(cluster, dir_query, time.time())
        head = {'Authorization': 'Bearer {}'.format(Token)}
        dir_response = requests.get(myUrl, headers=head).json()
        dir = round(dir_response['timeseries'][0]['data'][0][1], 2)
        print("Current data ingest rate is:\n" + str(dir))

        myUrl = "https://{}.wavefront.com/api/v2/chart/api?q={}&s={}&g=m&view=METRIC&sorted=false&cached=true&includeObsoleteMetrics=true".format(cluster, dir_ly_query, time.time())
        head = {'Authorization': 'Bearer {}'.format(Token)}
        dir_ly_response = requests.get(myUrl, headers=head).json()
        dir_ly = round(dir_ly_response['timeseries'][0]['data'][0][1], 2)
        print("\nData ingest rate last year was:\n" + str(dir_ly))

        dir_diff = round(dir - dir_ly, 2)
        print("\nYoY change in ingest rate is:\n" + str(dir_diff))

        dir_pdiff = round(((dir - dir_ly)/dir_ly)*100, 2)
        print("\nYoY percentage change in ingest rate is:\n" + str(dir_pdiff))

        if dir_pdiff > 0:
            score = score + 1
            if dir_pdiff > 10:
                score = score + 1
                if dir_pdiff > 20:
                    score = score + 1
                    if dir_pdiff > 30:
                        score = score +1
                        if dir_pdiff > 40:
                            score = score + 1
                            if dir_pdiff > 50:
                                score = score + 1
                                if dir_pdiff > 60:
                                    score = score + 1
                                    if dir_pdiff > 70:
                                        score = score + 1
                                        if dir_pdiff > 80:
                                            score = score + 1
                                            if dir_pdiff > 90:
                                                score = score + 1
            else:
                score = score + 0

    def dsr_calc():

        global score

        print("\n======== Data Scan Rate ========\n")

        myUrl = "https://{}.wavefront.com/api/v2/chart/api?q={}&s={}&g=m&view=METRIC&sorted=false&cached=true&includeObsoleteMetrics=true".format(cluster, dsr_query, time.time())
        head = {'Authorization': 'Bearer {}'.format(Token)}
        dsr_response = requests.get(myUrl, headers=head).json()
        dsr = round(dsr_response['timeseries'][0]['data'][0][1], 2)
        print("Current scan rate is:\n" + str(dsr))

        myUrl = "https://{}.wavefront.com/api/v2/chart/api?q={}&s={}&g=m&view=METRIC&sorted=false&cached=true&includeObsoleteMetrics=true".format(cluster, dsr_ly_query, time.time())
        head = {'Authorization': 'Bearer {}'.format(Token)}
        dsr_ly_response = requests.get(myUrl, headers=head).json()
        dsr_ly = round(dsr_ly_response['timeseries'][0]['data'][0][1], 2)
        print("\nData scan rate last year was:\n" + str(dsr_ly))

        dsr_diff = round(dsr - dsr_ly, 2)
        print("\nYoY change in scan rate is:\n" + str(dsr_diff))

        dsr_pdiff = round(((dsr - dsr_ly)/dsr_ly)*100, 2)
        print("\nYoY percentage change in scan rate is:\n" + str(dsr_pdiff))

        if dsr_pdiff > 0:
            score = score + 1
            if dsr_pdiff > 10:
                score = score + 1
                if dsr_pdiff > 20:
                    score = score + 1
                    if dsr_pdiff > 30:
                        score = score +1
                        if dsr_pdiff > 40:
                            score = score + 1
                            if dsr_pdiff > 50:
                                score = score + 1
                                if dsr_pdiff > 60:
                                    score = score + 1
                                    if dsr_pdiff > 70:
                                        score = score + 1
                                        if dsr_pdiff > 80:
                                            score = score + 1
                                            if dsr_pdiff > 90:
                                                score = score + 1
            else:
                score = score + 0


    def users_calc():

        global score

        print("\n======== Total Users ========\n")

        myUrl = "https://{}.wavefront.com/api/v2/chart/api?q={}&s={}&g=m&view=METRIC&sorted=false&cached=true&includeObsoleteMetrics=true".format(cluster, users_query, time.time())
        head = {'Authorization': 'Bearer {}'.format(Token)}
        users_response = requests.get(myUrl, headers=head).json()
        users = users_response['timeseries'][0]['data'][0][1]
        print("Total number of users:\n" + str(users))

        myUrl = "https://{}.wavefront.com/api/v2/chart/api?q={}&s={}&g=m&view=METRIC&sorted=false&cached=true&includeObsoleteMetrics=true".format(cluster, users_ly_query, time.time())
        head = {'Authorization': 'Bearer {}'.format(Token)}
        users_ly_response = requests.get(myUrl, headers=head).json()
        users_ly = users_ly_response['timeseries'][0]['data'][0][1]
        print("\nTotal number of users last year was:\n" + str(users_ly))

        users_diff = round(users - users_ly, 2)
        print("\nYoY change in number of users is:\n" + str(users_diff))

        users_pdiff = round(((users - users_ly)/users_ly)*100, 2)
        print("\nYoY percentage change in number of users is:\n" + str(users_pdiff))

        if users_pdiff > 0:
            score = score + 1
            if users_pdiff > 10:
                score = score + 1
                if users_pdiff > 20:
                    score = score + 1
                    if users_pdiff > 30:
                        score = score +1
                        if users_pdiff > 40:
                            score = score + 1
                            if users_pdiff > 50:
                                score = score + 1
                                if users_pdiff > 60:
                                    score = score + 1
                                    if users_pdiff > 70:
                                        score = score + 1
                                        if users_pdiff > 80:
                                            score = score + 1
                                            if users_pdiff > 90:
                                                score = score + 1
            else:
                score = score + 0

    def users30_calc():

        global score

        print("\n======== Monthly Active Users ========\n")

        myUrl = "https://{}.wavefront.com/api/v2/chart/api?q={}&s={}&g=m&view=METRIC&sorted=false&cached=true&includeObsoleteMetrics=true".format(cluster, users30_query, time.time())
        head = {'Authorization': 'Bearer {}'.format(Token)}
        users30_response = requests.get(myUrl, headers=head).json()
        users30 = round(users30_response['timeseries'][0]['data'][0][1], 2)
        print("Monthly active users:\n" + str(users30))

        myUrl = "https://{}.wavefront.com/api/v2/chart/api?q={}&s={}&g=m&view=METRIC&sorted=false&cached=true&includeObsoleteMetrics=true".format(cluster, users30_ly_query, time.time())
        head = {'Authorization': 'Bearer {}'.format(Token)}
        users30_ly_response = requests.get(myUrl, headers=head).json()
        users30_ly = round(users30_ly_response['timeseries'][0]['data'][0][1], 2)
        print("\nMonthly active users last year:\n" + str(users30_ly))

        users30_diff = round(users30 - users30_ly, 2)
        print("\nYoY change in monthly active users:\n" + str(users30_diff))

        users30_pdiff = round(((users30 - users30_ly)/users30_ly)*100, 2)
        print("\nYoY percentage change in monthly active users:\n" + str(users30_pdiff))

        if users30_pdiff > 0:
            score = score + 1
            if users30_pdiff > 10:
                score = score + 1
                if users30_pdiff > 20:
                    score = score + 1
                    if users30_pdiff > 30:
                        score = score +1
                        if users30_pdiff > 40:
                            score = score + 1
                            if users30_pdiff > 50:
                                score = score + 1
                                if users30_pdiff > 60:
                                    score = score + 1
                                    if users30_pdiff > 70:
                                        score = score + 1
                                        if users30_pdiff > 80:
                                            score = score + 1
                                            if users30_pdiff > 90:
                                                score = score + 1
            else:
                score = score + 0

    def users7_calc():

        global score

        print("\n======== Weekly Active Users ========\n")

        myUrl = "https://{}.wavefront.com/api/v2/chart/api?q={}&s={}&g=m&view=METRIC&sorted=false&cached=true&includeObsoleteMetrics=true".format(cluster, users7_query, time.time())
        head = {'Authorization': 'Bearer {}'.format(Token)}
        users7_response = requests.get(myUrl, headers=head).json()
        users7 = round(users7_response['timeseries'][0]['data'][0][1], 2)
        print("Weekly active users:\n" + str(users7))

        myUrl = "https://{}.wavefront.com/api/v2/chart/api?q={}&s={}&g=m&view=METRIC&sorted=false&cached=true&includeObsoleteMetrics=true".format(cluster, users7_ly_query, time.time())
        head = {'Authorization': 'Bearer {}'.format(Token)}
        users7_ly_response = requests.get(myUrl, headers=head).json()
        users7_ly = round(users7_ly_response['timeseries'][0]['data'][0][1], 2)
        print("\nWeekly active users last year:\n" + str(users7_ly))

        users7_diff = round(users7 - users7_ly, 2)
        print("\nYoY change in weekly active users:\n" + str(users7_diff))

        users7_pdiff = round(((users7 - users7_ly)/users7_ly)*100, 2)
        print("\nYoY percentage change in weekly active users:\n" + str(users7_pdiff))

        if users7_pdiff > 0:
            score = score + 1
            if users7_pdiff > 10:
                score = score + 1
                if users7_pdiff > 20:
                    score = score + 1
                    if users7_pdiff > 30:
                        score = score +1
                        if users7_pdiff > 40:
                            score = score + 1
                            if users7_pdiff > 50:
                                score = score + 1
                                if users7_pdiff > 60:
                                    score = score + 1
                                    if users7_pdiff > 70:
                                        score = score + 1
                                        if users7_pdiff > 80:
                                            score = score + 1
                                            if users7_pdiff > 90:
                                                score = score + 1
            else:
                score = score + 0

    def db_calc():

        global score

        print("\n======== Dashboards ========\n")

        myUrl = "https://{}.wavefront.com/api/v2/chart/api?q={}&s={}&g=m&view=METRIC&sorted=false&cached=true&includeObsoleteMetrics=true".format(cluster, db_query, time.time())
        head = {'Authorization': 'Bearer {}'.format(Token)}
        db_response = requests.get(myUrl, headers=head).json()
        db = db_response['timeseries'][0]['data'][0][1]
        print("Total number of dashboards:\n" + str(db))

        myUrl = "https://{}.wavefront.com/api/v2/chart/api?q={}&s={}&g=m&view=METRIC&sorted=false&cached=true&includeObsoleteMetrics=true".format(cluster, db_ly_query, time.time())
        head = {'Authorization': 'Bearer {}'.format(Token)}
        db_ly_response = requests.get(myUrl, headers=head).json()
        db_ly = db_ly_response['timeseries'][0]['data'][0][1]
        print("\nTotal number of dashboards last year:\n" + str(db_ly))

        db_diff = db - db_ly
        print("\nYoY change in dashboards:\n" + str(db_diff))

        db_pdiff = round(((db - db_ly)/db_ly)*100, 2)
        print("\nYoY percentage change in dashboards:\n" + str(db_pdiff))

        if db_pdiff > 0:
            score = score + 1
            if db_pdiff > 10:
                score = score + 1
                if db_pdiff > 20:
                    score = score + 1
                    if db_pdiff > 30:
                        score = score +1
                        if db_pdiff > 40:
                            score = score + 1
                            if db_pdiff > 50:
                                score = score + 1
                                if db_pdiff > 60:
                                    score = score + 1
                                    if db_pdiff > 70:
                                        score = score + 1
                                        if db_pdiff > 80:
                                            score = score + 1
                                            if db_pdiff > 90:
                                                score = score + 1
            else:
                score = score + 0

    def alert_calc():

        global score

        print("\n======== Alerts ========\n")

        myUrl = "https://{}.wavefront.com/api/v2/chart/api?q={}&s={}&g=m&view=METRIC&sorted=false&cached=true&includeObsoleteMetrics=true".format(cluster, alert_query, time.time())
        head = {'Authorization': 'Bearer {}'.format(Token)}
        alert_response = requests.get(myUrl, headers=head).json()
        alert = alert_response['timeseries'][0]['data'][0][1]
        print("Total number of alerts:\n" + str(alert))

        myUrl = "https://{}.wavefront.com/api/v2/chart/api?q={}&s={}&g=m&view=METRIC&sorted=false&cached=true&includeObsoleteMetrics=true".format(cluster, alert_ly_query, time.time())
        head = {'Authorization': 'Bearer {}'.format(Token)}
        alert_ly_response = requests.get(myUrl, headers=head).json()
        alert_ly = alert_ly_response['timeseries'][0]['data'][0][1]
        print("\nTotal number of alerts last year:\n" + str(alert_ly))

        alert_diff = alert - alert_ly
        print("\nYoY change in alerts:\n" + str(alert_diff))

        alert_pdiff = round(((alert - alert_ly)/alert_ly)*100, 2)
        print("\nYoY percentage change in alerts:\n" + str(alert_pdiff))

        if alert_pdiff > 0:
            score = score + 1
            if alert_pdiff > 10:
                score = score + 1
                if alert_pdiff > 20:
                    score = score + 1
                    if alert_pdiff > 30:
                        score = score +1
                        if alert_pdiff > 40:
                            score = score + 1
                            if alert_pdiff > 50:
                                score = score + 1
                                if alert_pdiff > 60:
                                    score = score + 1
                                    if alert_pdiff > 70:
                                        score = score + 1
                                        if alert_pdiff > 80:
                                            score = score + 1
                                            if alert_pdiff > 90:
                                                score = score + 1
            else:
                score = score + 0

#execute for all
    dir_calc()
    dsr_calc()
    users_calc()
    users30_calc()
    users7_calc()
    db_calc()
    alert_calc()

#display scoring results

    def calc_score():
        print("\n\n\n======== Overall Score ========\n\n\n")
        print("Score is calculated based on percentage change on above collected heuristics.\nFor each 10% incremental change, customer gets 1 point.")
        print("\n\nScore for this customer (out of 70) = " + str(score))
        p_score = round((score / 70)*100, 2)
        print("Percentage score = " + str(p_score))

    calc_score()
