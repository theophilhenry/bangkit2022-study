<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Dealing with Hard Problems <hr/>
> Everyone knows that debugging is twice as hard as writing a program in the first place. So if you're as clever as you can be when you write it, how will you ever debug it?
\- Brian Kernighan

Cool lesson : 
- Develop code in small digestible chunks!
- Keep your goal clear<br>
`Rubber Duck` debugging : Explaining the problem to a rubber duck. When we explain, we can think about the issues differently.

<br>

## Proactive Practices <hr/>
- Test program as expected
- Have good unit tests and integration tests
- Have continous integration
- Have test environment, to test code. 
    - Thorough check as it will be seen by the user
    - Troubleshoot whenever problems happen, without affecting the production environment
- Deploy software in phases or canaries. Instead upgrading all computer, do it one-by-one.
- Have good debug logging in the code
- Have centralized logs collection, in special servers from all servers or even all computer in the  network.
- Have a good monitoring system
- Have a good ticketng system to provide clear information up-front
- Have a good documentation and instructions on how to solve a spesific problem, knowing how to diagnose what's going on with the server, or tracking the known issues 
- Proactively plan additional capacity we'll need

<br>

## Planning Future Resource Usage <hr/>
Plan, 1mb per day? Plan when you want to buy. You can attach Network-Attached Storaged `NAT` : Additional diskspace. <br>
An interesting strategy for making the best possible use of resources, is to mix and match the processes that run on the computers, so they make use of all the available resources.

<br>

## Preventing Future Problems <hr/>
Report a bug to the relevant developers. For your own code, write a test!

### Readings

Preventing future breakage is a bit of a dynamic subject. Probably the most useful techniques here are identifying, isolating, and managing problem domains and failure domains. 

Problem Domains just describe the complexity of a given problem that one is trying to solve. Let’s look at an example below:

For example: counting the number of occurrences of a specific word in one of Shakespeare’s plays, like Hamlet. This is an indexing problem. And its problem domain is fairly limited in scope. It’s a single word, and a single play. A bit of BASH could easily solve this problem. So the problem domain is small, and the technical solution is fairly simple.

However, if the scope is widened slightly to include all of Shakespeare’s plays, the problem domain becomes larger. Any software solution used to try and solve this indexing problem has to now handle various logic that it did not have to handle before, like consolidating word occurrences in various plays. I.e. the word ‘Brevity’ may occur at least once in Hamlet, and N number of times in various other plays. Managing N occurrences of ‘Brevity’ over M works of Shakespeare is an order of magnitude more complex in terms of describing the problem domain. A bit of BASH could solve this problem, but it might be difficult.

If the problem becomes slightly more complex, such as finding the occurrences of various synonyms to a given word, then the problem domain becomes equally large. Managing original words, their synonyms, and their hit-count across multiple works of Shakespeare is even MORE complex.

So why is any of this useful? Well, if one can easily describe and reason about a problem in a lot of detail, they understand the Problem Domain fairly well. Producing a software solution for a given problem becomes easier when the Software Engineer understands the problem domain fairly well. Of course, building a good understanding of the Problem Domain often requires a lot of experimentation, and iteration. This is why it’s good to make a few initial attempts at testing a design before building an entire Production system to solve a problem like indexing Shakespeare.

Failure Domains
Like problem domains, failure domains just describe the complexity of a system. Except, instead of describing the various problems a system tries to solve, failure domains describe various sub-systems which may fail. Using the Shakespeare example again, if one of your systems is responsible for managing the full text of the works of Shakespeare (a content server), that might be a single failure domain. If another system is responsible for actually searching that content and counting the words (an indexer), that is a separate failure domain. Some failure domains can be within other failure domains. For example, if an indexer fails, the content server may not fail. But if a content server fails, the indexer will probably also fail.

So why do we care about any of this? Well, Problem Domains drive system complexity. Complex systems often have many failure domains. The key to preventing future breakage is to identify, and manage the scope and severity of a failure domain. This may mean redesigning the system in a way that has many smaller failure domains, instead of few large ones. 

As another example It’s better to have a video streaming service slow down instead of failing entirely. This kind of graceful degradation can be attributed to isolated failure domains.

This topic can be a bit complex, but there are several community articles on the idea of identifying and managing failure domains. Consolidating and completely eliminating possible failure domains is the key to preventing future breakage. If anything, managing failure domains should keep the scope of a break as small as possible.

### More info here : 

<ul><li><p><a href="https://simpleprogrammer.com/understanding-the-problem-domain-is-the-hardest-part-of-programming/" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://simpleprogrammer.com/understanding-the-problem-domain-is-the-hardest-part-of-programming/</u></a></p></li><li><p><a href="https://blog.turbonomic.com/blog/on-technology/thinking-like-an-architect-understanding-failure-domains" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://blog.turbonomic.com/blog/on-technology/thinking-like-an-architect-understanding-failure-domains</u></a></p></li><li><p><a href="https://landing.google.com/sre/sre-book/chapters/effective-troubleshooting/" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://landing.google.com/sre/sre-book/chapters/effective-troubleshooting/</u></a></p></li></ul>

Note : `failure domain` is a logical or physical component of a system that might fail.