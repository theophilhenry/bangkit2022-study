

```shell
~$ cd /etc/puppet/code/environments/production/modules/profile/manifests
~$ cat init.pp
```
This rule is creating a script under /etc/profile.d/. Scripts in this path will perform startup tasks, including setting up a user's own environment variables. The files under /etc/profile.d/ should only be editable by root.

```puppet
class profile {
        file { '/etc/profile.d/append-path.sh':
                owner   => 'root',
                group   => 'root',
                mode    => '0644', # First said no special permission
                content => "PATH=\$PATH:/java/bin\n",
        }
}
```

