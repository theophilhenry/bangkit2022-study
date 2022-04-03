<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Can't Physically be There <hr/>
- Rollback, 
- Snapshot the broken, move it to healthy, see what's wrong, 
- Call the providers
- Find the logs. 

<br>

## Finding the Root Problem <hr/>
- `Provider` Problem : Problems on the provider side, tend to be isolated to geographical regions. Try move it to a different region. If it fails in the other region, the problem is in your system.
- `Resource Usage` Problem : Move it to another computer with higher resource.
- `Update` Issue : Do a rollback

<br>

## Recovering from Failure <hr/>
If you operate a service that stores any kind of data, it's critical that you implement automatic backups and that you periodically check that those backups are working correctly by performing restores.
- Well backups and well-documented recovery plan.
- Have secondary instances already up and running
- Have service running on different data centers around the world
- Have 2 different connections (running a service-on-premise). 
- Run service on 2 different cloud vendors.

<br>

### Reading Debugging Problems on the Cloud
<ul><li><p><a href="https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-instances" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-instances</u></a></p></li><li><p><a href="https://docs.microsoft.com/en-us/azure/virtual-machines/troubleshooting/" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://docs.microsoft.com/en-us/azure/virtual-machines/troubleshooting/</u></a></p></li><li><p><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.html" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.htm</u></a></p></li></ul>