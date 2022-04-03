<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Managing Collaboration <hr/>
> If you are project mantainer, it's important that you reply promptly to pull requests and don't let them stagnate. The longer you are, the outdated it will be.

Be careful which patches to reject, make sure you understand.

Old way, they use Mailing List and IRC.<br>
Now they use Slack channels or Telegram groups. <br>

<br>

`Issue Tracker` / `Bug Tracker`
- Tasks need to be done
- State they're in
- Who's working on them
- Add comments to show details, how to solve, how to test it
- Report bugs

There's a bug tracker called BugZilla. But GITHUB already have it baked in.

### Creating Issue
Click `New Issue` button, specify the heading and description.

Each issues and pull request have a distinct #ID.<br>
You can refference the pull request when creating issue with #[number]

If you are fixing an issue through pull request,<br>
You can close issue automatically once the code is merged!<br>
In order to do that, you need to append `Closes #4` in the commit header/descriptions.

To solve an issue #1
1. Assign yourself
2. Fix the issue
3. Add `Closes #1`
4. Push and Done!

## Continous Integration <hr/>
Sometimes we forget to test...<br>
Well? We can write __Automated Tests__ to test the code for us,<br>
and then use Continous Integration to run those test automatically.

`Continous Integration System (CI)` : Build and test our code everytime there's a change. It can also run when any changes through pull requests.

Once our code automatically built and tested, next step is

`Continous Deployment/Delivery (CD)` : The new code is deployed often. To avoid roll outs, with a lot of changes between two versions of a project. <br>
Instead, do incremental updates with only a few canges at a time.

To do a CI/CD, you can use Jenkins. GitLab has their own infrastructure for continous integration. GitHub doesn't so use [Travis](https://www.travis-ci.com/). 

### Known Concepts :
`Pipelines` : Specify the step that need to run to get the result you want.<br>
>For Simple Python project, the pipeline could be to just run the automated tests.<br>
>For GO, it could be to compile the program, run unit tests, and integration tests, then deploy the code to a test instance.<br>

`Artifacts` : The name used to describe any files that are generated as part of the pipeline. 
>Usually compiled codes and other generated files like PDF/Logs.

### Things to Consider CI/CD
- Sometimes you need to give access to the software to the test server.<br>
We can exchange SSH Keys, or using API tokens app, 
- Make sure authorized entities for the test server is not the same with entities authorized to deploy on the production server.
- Always have a plan to recover your access in case the pipeline gets compromised
- If you want to add CI to GitHub, use travis. Then, create configuration using YAML file. 


