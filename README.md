# SSH Proxy

SSH Proxy is a simple wrapper written in Python 3 for creating SOCKS5 compatible proxies that connect via SSH tunnels.

SSH Proxy is useful for situations when you need to browse websites that are behind a corporate firewall, such as internal tools, test and staging servers etc.

## Installation

* Clone this repo and cd into the directory
* Run `pip install -r requirements.txt`
* `chmod +x ./ssh-proxy`
* Edit `config.ini.default` and rename to `config.ini`
* Create a symlink into your system path so you can call ssh-proxy globally

## Usage

### Starting SSH Proxy

`ssh-proxy --start`

This will start one or more SSH proxies on localhost at the ports specified in the config.ini.

Use with a browser proxy like [FoxyProxy](https://getfoxyproxy.org/) by setting the proxy host to `localhost`, port `8080 (or whatever defined in config.ini)` and type `Socks 5`. You can have multiple proxies running at any time.

### Configuration

You will need to set the following in the config.ini file:

* [config_name] - this can be anything you want
* `Host=ssh_host_or_ip`
* `User=you_ssh_username`
* `Port=8080` - this is the port that you will specify in your proxy settings

### Other Options

* `--stop` - Stop proxy service
* `--restart` - Restart proxy service
* `--status` - Get connection status
* `--help` - Get usage information

## Contributions

Pull requests welcome for any improvements or feel free to fork and tailor to your own needs.

## Author

Adam Williams - <https://github.com/adam-rw>