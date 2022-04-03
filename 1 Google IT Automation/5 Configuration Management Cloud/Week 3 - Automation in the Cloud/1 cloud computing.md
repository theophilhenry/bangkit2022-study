<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Cloud Computing <hr/>
`SaaS` : [Software] Cloud provider, delivers an entire application or program to the customer. (pre-packaged software)

`PaaS` : [Platform] Cloud provider, offers preconfigured platform to the customer. 

`Iaas` : [Infrastructure] Cloud provider, supplies only the bare-bones computing experience.(virtual machines)

<br>

## Scaling in the Cloud <hr/>
`Capacity` : How much the service can deliver. 

There are different ways we can scale our service :
- `Horizontally` : Add more nodes to the pool that's part of a spesific service. For example, add more server to distribute load across them. 

- `Vertically` : Making the nodes bigger. Resources like memories, CPU, and disk space.

- `Automatic` Scaling : Dynamically change and remove unused resource. Big Cost.

- `Manual` Scaling : Needs good monitoring and alerting.

<br>

## Evaluating the Cloud <hr/>
- Check the provider has security certification
- Use security procedures : Multi-factor auth, Encrypted file system, Public key cryptography

<br>

## Migrating to the Cloud <hr/>
- `IaaS` : Useful for administrators to use Lift and Shift strategy. First lifting the server to a new location. Shifting from one service to another. Server configuration still the same. 
- `PaaS` : You don't want to get involve in day-to-day management.<br>
    Example : <br>
    - `Managed Web Application` : You only have to care about writing the code for the web-app (not the framework). (Amazon Elastic Beanstalk, Microsoft App Service, Google App Engine). This may require code changes.
    - `Containers` : App that are packaged together with their configuration and dependencies. 

When moving to a cloud, you might hear the term :
- Public clouds : Cloud the Cloud services provided to you by a third party
- Private clouds : Your company owns the services and the rest of your infrastructure, whether that's on-site or in a remote data center. It's private because it's just for your company
- Hybrid clouds : Some workloads are run on servers owned by your company, while others are run on servers owned by a third party. You might want to ensure everything is integrated smoothly.
- Multi clouds : Mixture of public and/or private Clouds across vendors (may include servers hosted with Google, Amazon, Microsoft, and on-premise). 
    
