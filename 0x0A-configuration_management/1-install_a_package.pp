# Install Flask 2.1.0 with compatible Werkzeug version

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0 werkzeug==2.0.2',
  path    => ['/usr/bin', '/usr/local/bin'],
}

