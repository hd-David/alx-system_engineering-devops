# Kill the process named killmenow
exec { 'killmenow_process':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
}
