#!/usr/bin/pup
# installs flask version 2.10

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
