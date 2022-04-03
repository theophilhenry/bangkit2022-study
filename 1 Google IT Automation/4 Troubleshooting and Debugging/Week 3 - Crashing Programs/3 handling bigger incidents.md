<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Crashes in Complex Systems <hr/>
We need to look at the big picture. Find the log spesific to the error. <br>
You can also look at recent changes.<br>
A lot of companies today have automated process for deploying services to virtual machines running in the cloud.<br>

We've covered a bunch of techniques that you can use when facing a problem in a complex system. Looking at the available logs, figuring out what changed since the system was last working, rolling back to a previous state, removing faulty servers from the pool, or deploying new servers on demand. Up next, we'll explore a different part of dealing with bigger incidents, communication and documentation.

<br>

## Communication and Documentation During Incidents <hr/>
Write/Commmunicate/Documentate while doing solutions! It can helped everyone when revisiting the issues.<br>
Documenting what you do, lets you keep track of what you've tried and what the results were.<br>
We often forgot what we've tried, or what's the outcome of a spesific action.

If you don't know what the problem is, it's hard to give an estimation of when you'll have it fixed. But you can still provide timely updates about the work you're doing.

Roles when fixing a problem : <br>
`Communications Lead` needs to know what's going on and provide timely updates on the current state and how long until the problem's resolved. They can act as a shield for questions from users letting the rest of the team focus on the actual problem.<br>
`Incident Commander` or `Incident Controller` : Look at the big picture and decide what's the best use of the available resources. They can make sure that there's no duplication of work among team members and that only one person is modifying the production system at a time.<br>

Lastly, It's super-important to sum up the information that was helpful, such as :
- The root cause
- how you diagnose the problem and found that root cause
- what you did to fix the issue
- what needs to be done to prevent the problem from happening again

This summary can be last update to the bug, or it could be a `postmortem`. What is it?

<br>

## Writing Effective Postmorterms <hr/>
`postmortem` : Documents that describe details of incidence to help us learn from our mistakes.<br>
The goal isn't to `BLAME`, but to `LEARN` what happened to prevent the same issue from happening again.<br>
 we usually document 
 - `what` happened, 
 - `why` it happened, 
 - `how` it was `diagnosed`, 
 - `how` it was `fixed`, and 
 - figure out what we can do to `avoid` the same event happening in the future. 

How to write it then? In general, you want to include :
- what `caused` the issue
- what the `impact` of the issue was
- `how` it got `diagnosed`
- the `short-term` remediation you applied
- and the `long-term` remediation you recommend

It also good to write what went well. For example, the user hasn't noticed the bug because of our alert systems. This justifies keeping those systems running.



