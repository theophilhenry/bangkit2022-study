<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Introduction <hr/>
Site Reliability Engineering `SRE` : Reliability and Maintainabilit of Large Systems.

`Puppet` : Standard for configuration management

<br>

## Automation at Scale <hr/>
Concepts are the building blocks for letting manage a growing number of devices, without having to grow team in charge of them

> Being able to `scale` what we do, means that we can keep acheving larger impacts with the same amount of effort

Scalable System is a Flexible one

Too see how scalable our current setups is, ask :
- will `adding` more `servers` increase the `capacity` of the service? 
- How are new servers prepared, installed, and `configured`? 
- How `quickly` can you set up new computers to get them ready to be used? 
- Could you deploy a hundred servers with the same `IT team` that you have today? Or 
- would you need to hire `more people` to get it done faster? 
- Would all the deployed servers be `configured` exactly the `same` way?

<br>

## Configuration Management <hr/>
What does it mean for the configuration to be managed?<br>
`Configuration Management` system handle all of the configuration of the devices in your fleet, also known as nodes.

- Define a set of rules to the nodes you want to manage
- Ensures that those settings are true on each of the nodes

Change 1 configuration, it will be `repeatable` to the other computers. 

Example software : Puppet, Chef, Ansible, and CFEngine

<br>

## Infrastructure as Code <hr/>
We can `model` the `behavior` of our IT infrastructure in `files` that can be processed by automatic tools<br>
These files can be tracked in Version Control System.

Infrastructure as Code `IaC` : Storing all the configuration for the managed devices in version controlled files

This structure can be easily applied to another new computer, if the current one broke down.<br>
You can also run automated test.

Sum all things up, IaC system is :
- Consistent
- Versioned
- Reliable
- Repeatable




