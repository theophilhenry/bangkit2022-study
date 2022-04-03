<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Monitoring <hr/>
`Monitoring` lets us look into the history and current status of a system with `metrics`.

Some metrics are general like seing memory. or :

- Monitoring web service,<br>
Response in 500 range, means something bad in server<br>
Response in 400 range, means something bad in clinet-side

- Monitoring e-commerce,<br>
How many purchases sucessful, and failed.

- Monitoring mail server,<br>
How many sent and got stuck.

### Monitoring systems example : 
- Available in Cloud Providers : AWS Cloudwatch, Google Stack Driver, or Azure Metrics
- Across Vendors Usage : Prometheus, Datadog, or Nagios

### Models :
- Some use `pull` model : the monitoring infrastruucture periodically queries our service to get the metrics. 
- Some use `push` model : our service needs to periodically connect to the system to send the metrics.

### Dashboard
Shows the progesssion of the metrics overtime. Compare it to the week earlier, and so on.<br>
You only want to store the metrics that you care about. It cost money!

## Type of Monitoring

- `Whitebox Monitoring` : Check the behavior of the system fro mthe inside. We know the information we want to track, and we're in charge of making it possible to track

- `Blackbox Monitoring` : Checks the behavior of the system from the outside. This is typically done by making a request to the service and then checking that the actual response matches the expected response. Or to see how long client from different part of the world to get a response from the system. 

<br>

## Alerting <hr/>
How to do alerting?
- Run a job/script periodically that checks the health of the system and sends out an email if the system isn't healthy (by evaluating the metrics before).<br>
in Linux you can use `CRON` : tool to schedule periodic jobs.

## 2 types of alerting :
- `pages` : Alert that need immediate attention (urgent problem).
- `ticket` : non-urgents alerts

All alerts should be actionable. When there's nothing for you to do, don't alert. If failed once or twice, it might be a noise!

<br>

## Service-Level Objectives <hr/>
Here we will talk about criteria we can use to decide which situation should raise alerts.

`SLO` : pre-established performance goals for a spesific service. SLO must be measurable, to check if the service meets the objectives or not.

Example : 
- 99% : 3.65 day in a year.
- 99.9% (three 9 service) : aim for 8 hours of downtime a year.
- 99.999% : five nine service, total down time up to five minutes.

If you're service is not super critical, and it's okay to be down, you don't have to do four nines (99.9999% availability). 

Some service have Service Level Agreements `SLAs`, a service level agreement commitment between a provider and client. SLOs are more soft. 

`Error Budget` : Up to (for example) 43 minute down time. If it almost reaches that point, stop pushing any new features and focus on resolving the problems that keep causing the downtime.

<br>

## Basic Monitoring in GCP <hr/>
We'll use `Stackdriver` in GCP. 

<br>

### Information on Monitoring and Alerting
<ul><li><p><a href="https://www.datadoghq.com/blog/monitoring-101-collecting-data/" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://www.datadoghq.com/blog/monitoring-101-collecting-data/</u></a></p></li><li><p><a href="https://www.digitalocean.com/community/tutorials/an-introduction-to-metrics-monitoring-and-alerting" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://www.digitalocean.com/community/tutorials/an-introduction-to-metrics-monitoring-and-alerting</u></a></p></li><li><p><a href="https://en.wikipedia.org/wiki/High_availability" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://en.wikipedia.org/wiki/High_availability</u></a></p></li><li><p><a href="https://landing.google.com/sre/books/" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://landing.google.com/sre/books/</u></a></p></li></ul>