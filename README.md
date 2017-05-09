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

This will start SSH Proxy on localhost port 8080

### Other Options

* `--stop` - Stop proxy service
* `--restart` - Restart proxy service
* `--status` - Get connection status
* `--help` - Get usage information

## Contributions

Pull Requests welcome for any improvements or feel free to fork to tailor to your own needs.

## Author

Adam Williams - <https://github.com/adam-rw>