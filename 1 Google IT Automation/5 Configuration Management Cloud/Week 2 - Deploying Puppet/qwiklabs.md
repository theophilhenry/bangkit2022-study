```puppet
class packages {

    package { 'python-requests':
        ensure => installed,
    }
}

```

Connecting to linux-instance using external IP address
```shell
~$ gcloud compute instances describe linux-instance --zone=us-central1-a --format='get(networkInterfaces[0].accessConfigs[0].natIP)'
```

For the machine info, change from this
```puppet
class machine_info {
   file { '/tmp/machine_info.txt':
       content => template('machine_info/info.erb'),
   }
   if $facts[kernel] == "windows" {
       $info_path = "C:\Windows\Temp\Machine_Info.txt"
   } else {
       $info_path = "/tmp/machine_info.txt"
   }
}
```

to this
```puppet
class machine_info {
  if $facts[kernel] == "windows" {
       $info_path = "C:\Windows\Temp\Machine_Info.txt"
   } else {
       $info_path = "/tmp/machine_info.txt"
   }
 file { 'machine_info':
       path => $info_path,
       content => template('machine_info/info.erb'),
   }
}
```

## Puppet Templates

Templates are documents that combine code, data, and literal text to produce a final rendered output. The goal of a template is to manage a complicated piece of text with simple inputs.

In Puppet, you'll usually use templates to manage the content of configuration files (via the content attribute of the file resource type).

Templates are written in a templating language, which is specialized for generating text from data. Puppet supports two templating languages:

- Embedded Puppet (EPP) uses Puppet expressions in special tags. It's easy for any Puppet user to read, but only works with newer Puppet versions. (≥ 4.0, or late 3.x versions with future parser enabled.)

- Embedded Ruby (ERB) uses Ruby code in tags. You need to know a small bit of Ruby to read it, but it works with all Puppet versions.

cat templates/info.erb outputs :
```template
Machine Information
-------------------
Disks: <%= @disks %>
Memory: <%= @memory %>
Processors: <%= @processors %>
}
```

### Rebooting after 30 Days
```puppet
class reboot {
  if $facts[kernel] == "windows" {
    $cmd = "shutdown /r"
  } elsif $facts[kernel] == "Darwin" {
    $cmd = "shutdown -r now"
  } else {
    $cmd = "reboot"
  }
  if $facts[uptime_days] > 30 {
    exec { 'reboot':
      command => $cmd,
     }
   }
}
```

