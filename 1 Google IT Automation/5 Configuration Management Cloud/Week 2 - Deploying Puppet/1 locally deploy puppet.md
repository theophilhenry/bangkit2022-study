<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Applying Rules Locally <hr/>
We can run puppet in CLI. 
```shell
~$ sudo apt install puppet-master
```
After that, create a `manifest` : file store rules we want to apply. This file uses `.pp` ext.

To create and run our puppet, do this
```shell
~$ nano tools.pp
~$ sudo puppet apply -v tools.pp # V for verbose output, what's going when script is running
```
`Catalog` : List of rules that are generated for one specific computer once the server has evaluated all variables, conditionals, and functions.

<br>

## Manage Puppet Resource Relationships <hr/>
Here is some example with related resources called ntp
```puppet
class ntp {
    package { 'ntp':
        ensure => latest,
    }
    file { '/etc/ntp.conf':
        source => '/home/user/ntp.conf',
        replace => true,
        require => Package['ntp'], # Configuration file requires NTP package
        notify => Service['ntp'], 
        # ntp Service should be notified if configuration changes, 
        # in the future, the service will get reloaded with the new settings.
    }
    service { 'ntp':
        enable => true,
        ensure => running,
        require => File['/etc/ntp.conf'] # Service require configuration file
    }
}

include ntp # We want to apply the rules descrbed in a class, typically in another file.
```
`Resource` types are written in `Lower-Case`, but <br>
`Relationship` use `Upper-Case` when reffering from another resource's attribute.

<br>

## Organizing Your Puppet Modules <hr/>
`Module` : Collection of manifest and associated data

Directories :
- `manifests` : Directory that stores all manifest.
- `files` : Files that are copied into the client machine without any changes. 
- `template` : Files that are preprocessed before they been copied into the client machines.

`init.pp` : A file in manifests folder, define the class with the same name as the module.<br>
This manifest is special and needs to `always` be `present`. `First` one that's read by puppet when module got included.

> Note : There's a command in linux called `tree [dir]` to view directory trees

There's a lot of prepackaged module, we can install it for our deployement.
```puppet
~$ sudo apt install puppet-module-puppetlabs-apache
~$ cd /usr/share/puppet/modules.avaialble/puppetlabs-apache/
```
`lib` : Adds function and fact to the ones already shipped by puppet.

`metadata.json` : Additional data about the module. Like which version of OS is compatible with. 

How to include module?<br>
```shell
~$ nano webserver.pp
```
```puppet
include ::apache # Double column means this is a global module
```
```shell
~$ sudo puppet apply -v webserver.pp
```

<br>

### More Reading Information
<ul><li><p><a href="https://puppet.com/docs/puppet/latest/style_guide.html" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://puppet.com/docs/puppet/latest/style_guide.html</u></a></p></li><li><p><a href="https://puppet.com/docs/puppetserver/latest/install_from_packages.html" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://puppet.com/docs/puppetserver/latest/install_from_packages.html</u></a></p></li></ul>