# SSH Proxy

SSH Proxy is a simple wrapper written in Python for creating a SOCKS5 compatible proxy to connect via an SSH tunnel.

SSH Proxy is useful for situations when you need to browse websites that are behind a corporate firewall, such as internal tools, test and staging servers etc.

## Installation

* Clone this repo and cd into the directory
* Run pip install -r requirements.txt
* chmod +x ./ssh-proxy

## Usage

### Starting SSH Proxy

`./ssh-proxy --start`

This will start SSH Proxy on localhost port 8080.

Use with a browser proxy like [FoxyProxy](https://getfoxyproxy.org/) by setting the proxy host to `localhost`, port `8080` and type `Socks 5`.

### Configuration

You will need to set the following in the config.ini file:

* `Host=ssh_host_or_ip
* `User=you_ssh_username`

### Other Options

* `--stop` - Stop proxy service
* `--restart` - Restart proxy service
* `--status` - Get connection status
* `--help` - Get usage information

## Contributions

Pull requests welcome for any improvements or feel free to fork and tailor to your own needs.

## Author

Adam Williams - <https://github.com/adam-rw>