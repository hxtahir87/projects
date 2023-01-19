import json
import requests
import time

token = "8f1b5856-2482-42a6-b4b2-ffdc53edac7e"
#myUrl = "https://try.wavefront.com/report"
myUrl = "http://localhost:2878"
head = {'Authorization': 'Bearer {}'.format(token), 'Content-Type': 'text/plain'}


metric =  ("test.metric2 100 source=")

# observability.FDSize MetricName='FDSize' appliance='2d1ca7ba-6319-445b-98fc-b20320449a87' application='SreHealth' env='stg' host='vmc-odp-forwarder-service' level='service' metricType='process' org_id='b97ca954-03d0-41cb-92a3-26671cfadae3' orgtype='INTERNAL_NON_CORE' pluginName='ProcCollectorPlugin' port='5003' region='US_WEST_2 sddc_id=2d1ca7ba-6319-445b-98fc-b20320449a87' serviceName='vsphere-ui' source=2d1ca7ba-6319-445b-98fc-b20320449a87 value='51' 2 1640280387000000000

metric_post = requests.post(myUrl, headers=head, data=metric)

print(metric_post.status_code)
print(metric_post.text)

# "stats.counters.search-platform-es-sink.esdoc.eswrite.total.count 7628 cluster=PROD esIndex=prod_consumer_search_index_v9 esdocType=_doc statistic=count source=ip-172-31-19-138.us-west-2.compute.internal source=search-platform-es-sink"
