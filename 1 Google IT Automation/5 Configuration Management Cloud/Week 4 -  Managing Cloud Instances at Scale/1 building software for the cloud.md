<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Storing data in the Cloud <hr/>
Factor choosing the right data storage :
- how `much` data you want to store, 
- what `kind` of data that is, 
- what `geographical` locations you'll be using it in, 
- whether you're mostly `writing` or `reading` the data, 
- how `often` the data changes, or
- what your `budget` is.

### Type of Data Storage

- `block` storage : resembles physical drive, like local disk attached to VM.
    - `persistent` storage : Instances that are long lived, and need to keep data across reboots and upgrades
    - `ephemeral` storage :  instances that are only temporary, and only need to keep local data while they're running. This common on containers 

        `shared` file system : Using the providers through network file system protocols (NFS/CIFS).

<br>

- `blob` or `object` storage : Lets you place in retrieve objects in a storage bucket. Ex generic object like photos, videos, encoded, and stored on disk as binary data. 

    blob object stored into storage with name. To interact, use API or special utilities.

    Cloud providers offer db as service, SQL and NoSQL.
    - `SQL` : use the traditional database format and query language. Data is stored in tables with columns and rows that can be indexed, and we retrieve the data by writing SQL queries.
    - `NoSQL` : offer a lot of advantages related to scale. They're designed to be distributed across tons of machines and are super fast when retrieving results. Need to use `API` provided by the db. 

### Storage `Class`
Providers offer storage at different prices. Performance, availability, how often data access, will affect monthly prices.

Perfomance of storage solution is influenced by many factors : 
- `Throughput` : the `amount` of data that you can `read` and `write` in a given amount of `time`

- `IOPS` Input/Ouput Operation per second : measures how `many` `reads` or `writes` you can do in `one second`, no matter how much data you're accessing

- `latency` : the amount of time it takes to complete a read or write operation (take into account the impact of IOPS, throughput)
    - `Read latency` is sometimes reported as the time it takes a storage system to start delivering data after a read request has been made, also known as time to first byte

    - `write latency` is typically measured as the amount of time it takes for a write operation to complete

When chosing storage class, there is
- `hot` data : Accesed frequently and stored in hot storage
- `cold` data : accesed infrequently and stored in cold storage

hot storage back ends are usually built using `SSD`

<br>

## Load Balancing <hr/>
We want to distribute requests accross instances. 

Load balancing techniques :
- `Round-Robin DNS`<br>
Example : First you make sure each of your friend got a cookie. Then you give everyone a second serving, and so on until your guest say thankyou. 

    In a simplest DNS configuration, your hostname always translated to the same IP.  

    But with `Round-Robin`, it'll give each `client` asking for the translation, a `group IP addresses` in different `order`. The client picks one of the `addresses`. If the attempt fails, the client tries the next IP on the list. 

    Limitations, 
    - You `can't control` which addresses get picked by the clients. Even if it's overloaded.
    - DNS are `cached` by the clients and other servers, if you need to change the list of addresses for the instances, you have to wait until all of the DNS records that were cached by the clients `expire`.

- `Dedicated server as Load Balancer`<br>
    Machine that acts as a proxy between clients and servers. It recieves request, and based on the rules that we provide, it directs them to the selected back-end server.

    Load balances can be super complex depending on the service :
    - Say your service needs to keep track of the actions that a user has taken. You want `Sticky Sessions` : All requests from the same client always go to the same backend server. Only use it when you need it.
    - You can check health of the backend server. Do this by `simple query`, and checks that the `reply matches` the expected reply. If it's unhealty, the load balancer will stop sending requests to it, and keep only the healthy servers in the pool. 

Adding  a new machine to the pool is as easy as creating an instance! 

### Service Around the World
How to make sure clients `connect` to the `servers` that are `closest` to them?

Use `GeoDNS` and `GeoIP`, these are DNS configurations that will direct your clients to the closest geographical load balancer.

This mechanism relies on the how DNS servers replies to a request (How it will give the IP back to the client)

There are some providers dedicatedd to bringing the contents of your services as close to the user as possible.<br>
`CDNs` Content Delivery Network : Make up a `network` of physical `hosts` that are `geographically` located as `close` to the end `user` as possible

CDNs often the same data center as the users Internet service provider. Caching content super close to the user. 

<br>

## Deploy Changes Safely to Cloud Services / Change Management <hr/>
`Change Management` : Lets us keep innovating while our services keep running.

1. Make sure they're well tested. un init and integration tests. 
2. Use Continous Integration to build and test automatically when there's change (Jenkins, Travis CI)
3. Use Continous Deployment to control deployment with rules. Like only deploy if tests passed successfully.
4. Use CD to push to different env, based on some rules. We could push the changes to test env first, then if it still working, manually tell deployment to push changes to production. <br>
You might also want to push on dev env, and have another called pre-prod. These instances kept as similar to prod as possible.

### Experiment with a new service feature.

When you want to test in production, use <br>
`A/B` testing : Some request are served using one set of code and configuration (A), and the other requests are served using a different set of code configuration (B).

For example, only 1% of requests to instance in the pool with (B) configuration. Make sure you have a monitoring system. 

<br>

## Understasnding Limitations <hr/>
Problem you might come accross :
- `Rate Limits` : Prevent one service from overloading the whole system. There might be a rate limit of one call per second for an expensive API call
- `Untilization Limits` : Cap the total amount of a certain resource that you can provision. 

You may want to request quota increase. 

- `Depedencies`. When you use PaaS, the maintenance and upgrade handled by the provider. But, you don't get to choose what version of software you're using. You might want to keep the old, or hurries to update the new version.

You can set up test env, that uses `beta` or `pre-release` version, to let you test before it impacts production.

<br>

### More about Cloud Providers
Common Quotas you’ll find in various cloud providers
<ul><li><p><a href="https://cloud.google.com/compute/quotas#understanding_vm_cpu_and_ip_address_quotas" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://cloud.google.com/compute/quotas#understanding_vm_cpu_and_ip_address_quotas</u></a></p></li><li><p><a href="https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html</u></a></p></li><li><p><a href="https://docs.microsoft.com/en-us/azure/azure-subscription-service-limits#service-specific-limits" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://docs.microsoft.com/en-us/azure/azure-subscription-service-limits#service-specific-limits</u></a></p></li></ul>