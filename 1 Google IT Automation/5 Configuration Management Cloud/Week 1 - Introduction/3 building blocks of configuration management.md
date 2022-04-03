<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Domain Spesific Language <hr/>
`DSL` : Limted in scope. 

puppet `Facts` : Variables that represent the characteristics of the system.<br>
Facts returns :
- OS
- Memory
- Virtual Machine or not
- IP

We can also create custom Facts. 

Here is an example of facts usage
```puppet
if $facts['is_virtual'] {
    package { 'smartmontools' : ensure => purged, }
} else {
    package { 'smartmontools' : ensure => installed, }
}
```
`smartmontools` : Monitors the state of hard drives. If virtual machine, don't install it.

\$ is variable in Puppet's DSL. Facts is data structure known as `hash` (like dict in py).

<br>

## Driving Principles of Configuration Management <hr/>
See that we don't tell steps, but declare the end goal.

`Declarative Language` : declare the state that we want to achieve rather than the steps to get there.

`Procedural Language` : write out the procedure that the computer needs to follow to reach our desired goal.<br>

Aspects of Configuration Management
- Operation of Configuration Management has to be idempotent

    `Idempotent` : Can be performed over and over again without changing the system after the first time the action was performed, and with no unintended side effects.

    An exception for that is `exec` resource, since it modify the system each time it's executed. Like "mv". To avoid problem, we can do
    ```puppet
    exec { 'move example file': 
        command => 'mv /home/user/example.txt /home/user/Desktop',
        onlyif => 'test -e /home/user/example.txt',
    }
    ```

- Test and Repair Paradigm

    Actions are taken only when they are necessary to achieve a goal. avoids wasting time doing actions that aren't needed.

- Puppet is Stateless

    No state being kept between runs of the agent. Each Puppet run is independent of the previous one, and the next one. 

<br>

### Reading Resources
<ul><li><p><a href="https://en.wikipedia.org/wiki/Domain-specific_language" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://en.wikipedia.org/wiki/Domain-specific_language</u></a></p></li><li><p><a href="http://radar.oreilly.com/2015/04/the-puppet-design-philosophy.html" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>http://radar.oreilly.com/2015/04/the-puppet-design-philosophy.html</u></a></p></li></ul>