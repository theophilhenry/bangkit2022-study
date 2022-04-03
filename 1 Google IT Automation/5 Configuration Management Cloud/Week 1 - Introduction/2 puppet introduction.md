<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Puppet <hr/>
Cross-platform tool created in 2005.<br>
Latest version puppet 6 (2018). 

Client-server architecture for Puppet : 
- Client : puppet agent
- Service  : Puppet master

Agent send facts describe the computer to the master.<br>
Master replied with generated rules need to be applied.<br>
Agent do the changes.

```puppet
class sudo {
    package { 'sudo'
        ensure => present,
    }
}
```
Code above ensures the package sudo available in all computers.

Where puppet install the package from?
- Linux : APT, Yum, DNF
- MacOS : Apple, MacPorts
- Windows : Add extra attribute stating where the installer on local disk, Chocolatey

<br>

## Puppet Resources <hr/>
In puppet, `resources` : Basic unit for modelling the configuration we want to manage.

Declaration
```puppet
<TYPE> { '<TITLE>': <ATTRIBUTE> => <VALUE>, }
```

Here we use the `file` resources. 
```puppet
class sysctl {
    file { '/etc/syctl.d':
        ensure => directory,
    }
}
```
```puppet
class timezone {
    file { 'etc/timezone':
        ensure => file, # Not dir or symlink
        content => 'UTC\n', # UTC Timezone
        replace => true, # Replace even the file even if already exists
    }
}
```

Puppet agent then turns the desired state into reality using `Providers`<br>
Provider depends on the OS, as explained above.

<br>

## Puppet Classes <hr/>
Classes is to collect resources to achieve a goal in a single pace. 

<br>

### Puppet Reading Resources

<ul><li><p><a href="https://puppet.com/docs/puppet/latest/lang_resources.html" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://puppet.com/docs/puppet/latest/lang_resources.html</u></a></p></li><li><p><a href="https://puppet.com/blog/deploy-packages-across-your-windows-estate-with-bolt-and-chocolatey/" title="" target="_blank" rel="noopener nofollow" aria-label="">https://puppet.com/blog/deploy-packages-across-your-windows-estate-with-bolt-and-chocolatey/</a></p></li></ul>
