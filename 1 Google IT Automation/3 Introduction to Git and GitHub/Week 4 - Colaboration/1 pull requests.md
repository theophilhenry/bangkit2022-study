<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

# Interact with Others Project 
We'll learn how to interact with others code :)

<br>

## Simple Pull Requests   <hr/>

`Pull Request` : 
A commit or series of commits that you send to the owner of the repository, so that they incorporate it into their tree.

> This is a common way of working because most project have small contributor.
__Anybody__ can suggest patches, bug fixes, or even new features!<br>
They can review to check if the license is __valid__, or follows the __guidelines__.

Before we could do Pull Request, we should **Fork** the repo

`Forking` : A way of creating a copy of the given repository to us. <br>
Our changes will be pushed to the forked copy.

Typical workflow :
- First create a fork, then work on that local fork.
- Fork is the same as normal repo, except github know which repo it forked from.
- So we can eventually merge our changes back into the main repo, by creating pull requests.

On github forked repo, there's a lot information.
You can create pull request from there.

<br>

## Advanced Pull Request  <hr/>

To make larger changes. Not only from the web GUI.
<br>For example :

```bash
~$ git clone [forked_url]
~$ git log # See info
~$ git checkout -b add-readme
~$ nano README.md
~$ git add README.md
~$ git commit -m "Add simple README"
```
Now, to push the current change to forked repo,
We need to create the corresponding branch
```bash
~$ git push -u origin add-readme # This pushes the branch and file 
```
If our changes cannot be automatically merged, <br>
then REBASE our changes to the current branch of the original repo. <br>
That way, it can be merged.

<br>

## Updating Pull Requests  <hr/>

```bash
~$ nano README.md
~$ git commit -a -m "Changing old Pull"
```
Our commits will be a part of the same pull requests. <br>
If you want to create a separate pull request, <br>
You need a new BRANCH

> In short, Pull Requests created per BRANCH

Some projects may ask to have only 1 commit.
Other project may need you to rebase to the master branch.

<br>

## Squashing Changes to Single Commits  <hr/>

Because you are the only one worked in this repo, <br>
you can rewrite history :3

We can do that by using interactive rebase
```bash
~$ git rebase -i master
```
The command will open most recent commit to oldest. (top -> bottom)
```bash
squash : meld with previous commit, and the message, you can modify too
fixup : same with squash, but the message is deleted
```
Now, the old repo has 2 commit, but our local has 1 commit. <br>
To merge it, use
```bash
~$ git push -f # Force Push!
```
