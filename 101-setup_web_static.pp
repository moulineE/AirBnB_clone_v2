# using Puppet, sets up my web servers for the deployment of web_static.

exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
  before  => Package['nginx'],
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get update'],
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
  require => Exec['add test dir']
  before  => Service['nginx'],
}

exec { 'add shared dir':
  command => '/usr/bin/env mkdir -p /data/web_static/shared/',
  require  => Package['nginx'],
  before  => Service['nginx'],
}

exec { 'add test dir':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
  require  => Package['nginx'],
  before  => Service['nginx'],
}

exec { 'add symbolic link':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test/ /data/web_static/current',
  require  => Exec['add test dir'],
  before  => Service['nginx'],
}

exec { 'change /data dir owner':
  command => '/usr/bin/env sudo chown -R ubuntu:ubuntu /data',
  require  => Package['nginx'],
  before  => Service['nginx'],

exec { 'setup nginx site':
  command => '/usr/bin/env sed -i '/listen 80 default_server;/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default',
  require  => Package['nginx'],
  require  => Exec['add test dir'],
  before  => Service['nginx'],
}

service { 'nginx':
  restart,
  require => Package['nginx'],
  require  => Exec['setup nginx site']
}
