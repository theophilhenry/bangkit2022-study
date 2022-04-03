<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Spinning up VMs in the cloud <hr/>
`Reference Images` : Store the content of a machine in a reusable format.

`Templating` : Process of capturing all of the system configuration to let us create VMs in a repeatable way.

`Disk Image` : Snapshot of a virtual machine's disk at a given point in time.

You can copy CLI from the machine you've created at the bottom of GCS

## Customizing VMs in GCP <hr/>
we'll use the instance that we configured as the base for our `reference image`<br>
`systemd` : The initializing system used by most modern Linux Distributions.

This is hello_cloud.service file
```systemd
[Unit]
After=network.target

[Service]
ExecStart=/usr/local/bin/helo_cloud.py 89

[Install]
WantedBy=default.target
```
After this, copy the hello_cloud.py to `/usr/local/bin/`, and hello_cloud.service `/etc/systemd/system`.
It’s important to know where to copy our systemd service file on Linux in order to configure our scripts as services

```shell
~$ sudo systemctl enable hello_cloud
```

We need to think how we'll upgrade when we want to make changes to it :
- Create a different `refference image` each new version
- Add configuration management system

<br>

## Templating a Customized VM <hr/>
`snapshot` : Full copy

`image` : Template based on it

First create an image, then create instance template.

Manual work is long, but you can automate it using `gcloud` command.

```shell
~$ gcloud init # Set up authentication
Select project to use : 1
Select default region : 45 (asia-east2-b)
~$ gcloud compute instances create ---source-instance-template webserver-template ws1 ws2 ws3 ws4 ws5
```
`compute` : Manage VM resources
`instances` : deal with individual VMs
<br>

### Managing VMs in GCP
<ul><li><p><a href="https://cloud.google.com/compute/docs/quickstart-linux" title="" target="_blank" rel="noopener nofollow" aria-label=""><em><u>https://cloud.google.com/compute/docs/quickstart-linux</u></em></a></p></li><li><p><a href="https://cloud.google.com/compute/docs/instances/create-vm-from-instance-template" title="" target="_blank" rel="noopener nofollow" aria-label=""><em><u>https://cloud.google.com/compute/docs/instances/create-vm-from-instance-template</u></em></a></p></li><li><p><a href="https://cloud.google.com/sdk/docs" title="" target="_blank" rel="noopener nofollow" aria-label=""><em><u>https://cloud.google.com/sdk/docs</u></em></a></p></li></ul>


