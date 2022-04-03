<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Puppet Nodes <hr/>
You also can apply different rules to different systems using `Separate Node Deffinitions`.

`node` : System where you can run Puppet agent. (physical workstation, a server, a virtual machine, or even a network router)

We usually have `default node` that lists the classes taht should be included for all the nodes.
```puppet
node default {
    class { 'sudo': } # We call module here
    class { 'ntp': 
        servers => {'ntp1.example.com', 'ntp2.example.com'}
    }
}
```

We can have add more node definitions like so
```puppet
node webserver.example.com { # Identified by FQDN (fully qualified domain names)
    # We still need to list same classes, 
    # because the default node only applied to nodes that don't have explicit entry
    class { 'sudo': }
    class { 'ntp': 
        servers => {'ntp1.example.com', 'ntp2.example.com'}
    }
    class { 'apache': }
}
```

To avoid writing the same class, we might want to define a `base class`. 

`site.pp` : Stores The Node Deffinitions.  

<br>

## Puppet's Certificate Infrastructure <hr/>
The client send their name to the server when they connect, but how can the server trust that a client is really who he claims to be?

uppet uses Public Key Infrastructure `PKI` to establish secure connections between the server and the clients. Its called Secure Socket Layer (SSL). Client and Server checks each other identity.

How computer know which public keys to trust?<br>
This is where `Certificate Authority` comes in. 
- It verifies the identity, then creates a certificate stating that the public key goes with that machine. 
- Other machines can rely on that certificate to know that they can trust the public key

How about baked-in CA in Puppet?
1. Node (first time) request certificate from Puppet master
2. Puppet master verify the node's identity and create a certificate<br>
    It can be checked manually by the System Administrator, or automatically with additional information about the machines (copying a unique piece of information into the machines when they get provisioned and then use this pre-shared data as part of the certificate request). 
3. Agent picks the certificate and trust the master. Then on, use the certificate to create request.

Why care about identity of nodes?
1. Puppet rules include confidential information
2. Don't apply to the wrong computer

Btw, you can configure puppet to sign all request.
```shell
~$ sudo puppet config --section master set autosign true
```

<br>

## Setting up Puppet Clients and Servers <hr/>
Say this is the current master, 
1. You want to accept all autosign. You can now connect to client.
2. Connect using SSH to a client machine 
    ```shell
    ~$ ssh webserver
    ```
    1. In the client, install the puppet first. Then configure the server
        ```shell
        ~$ sudo puppet config set server ubuntu.example.com
        ```
    2. Now you can test connection to the puppet master using
        ```shell
        ~$ sudo puppet agent -v --test # --test to test run
        ```
5. In master, create site.pp
    ```shell
    ~$ nano /etc/puppet/code/environments/production/manifests/site.pp
    ```
    ```puppet
    node webserver.example.com {
        class {'apache':}
    }

    node default {}
    ```
    1. Now you can run the client again

### Automating the Puppet
`System CTL` : Control services that are enabled when the machine starts and running. 
```shell
~$ sudo systemctl enable puppet # You can start if it's haven't been started yet.
```

<br>

### More information

<ul><li><p><a href="http://www.masterzen.fr/2010/11/14/puppet-ssl-explained/" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>http://www.masterzen.fr/2010/11/14/puppet-ssl-explained/</u></a></p></li></ul>

Note : 
- `Templates` are documents that combine code, system facts, and text to render a configuration output fitting predefined rules.