# using Puppet, sets up my web servers for the deployment of web_static.

$nginx_site_config = "server {
        listen 80 default_server;
        location /hbnb_static {
                alias /data/web_static/current/;
        }
        add_header X-Served-By ${hostname};
        error_page 404 /custom_404.html;
        location = /custom_404.html {
                root /usr/share/nginx/html;
                internal;
        }
        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        listen [::]:80 default_server;
        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                try_files $uri $uri/ =404;
        }

}"

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
  <head>\n</head>\n<body>\nHolberton School\n</body>\n</html>',
  require => Exec['add test dir'],
  before  => Exec['nginx restart'],
}

exec { 'add shared dir':
  command => '/usr/bin/env mkdir -p /data/web_static/shared/',
  require => Package['nginx'],
  before  => Exec['nginx restart'],
}

exec { 'add test dir':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
  require => Package['nginx'],
  before  => Exec['nginx restart'],
}

exec { 'add symbolic link':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test/ /data/web_static/current',
  require => Exec['add test dir'],
  before  => Exec['nginx restart'],
}

exec { 'change /data dir owner':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
  require => Package['nginx'],
  before  => Exec['nginx restart'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_site_config,
  require => Exec['add test dir'],
  before  => Exec['nginx restart'],
}

exec { 'nginx restart':
  command => '/usr/bin/env service nginx restart',
  require => File['/etc/nginx/sites-available/default'],
}
