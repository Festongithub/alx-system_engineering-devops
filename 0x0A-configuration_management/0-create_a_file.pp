# creates file in /tmp

file { '/tmp/school':
  content => 'I love Puppet\n',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}

