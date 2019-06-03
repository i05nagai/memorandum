---
title: sshd
---

## sshd


## CLI

```
sshd [-46DdeiqTt] [-C connection_spec] [-c	host_certificate_file]
[-E log_file]	[-f config_file] [-g login_grace_time]
[-h host_key_file] [-o option] [-p port] [-u len]
```


* -4
    * Forces sshd to use	IPv4 addresses only.
* -6
    * Forces sshd to use	IPv6 addresses only.
* -C
    * connection_spec
     Specify the connection parameters to use for the -T extended test
     mode.  If provided, any Match directives in the configuration
     file that would apply are applied before the configuration	is
     written to	standard output.  The connection parameters are	sup-
     plied as keyword=value pairs and may be supplied in any order,
     either with multiple -C options or	as a comma-separated list.
     The keywords are ``addr,''	``user'', ``host'', ``laddr'',
     ``lport'',	and ``rdomain''	and correspond to source address,
     user, resolved source host	name, local address, local port	number
     and routing domain	respectively.

* -c	host_certificate_file
     Specifies a path to a certificate file to identify	sshd during
     key exchange.  The	certificate file must match a host key file
     specified using the -h option or the HostKey configuration	direc-
     tive.

* `-D`
    * When this option is specified, sshd will not detach and does not become a daemon.  This allows easy monitoring of sshd.

* `-d`
    * Debug mode. 
    * The server sends verbose debug output to standard error, and does not put itself in the background. The server also will not fork and will only process one connection.  This option is only intended for debugging for the server.  Multiple -d options increase the debugging level.  Maximum is 3.

 -E	log_file
     Append debug logs to log_file instead of the system log.

 -e	     Write debug logs to standard error	instead	of the system log.

 -f	config_file
     Specifies the name	of the configuration file.  The	default	is
     /etc/ssh/sshd_config.  sshd refuses to start if there is no con-
     figuration	file.

 -g	login_grace_time
     Gives the grace time for clients to authenticate themselves
     (default 120 seconds).  If	the client fails to authenticate the
     user within this many seconds, the	server disconnects and exits.
     A value of	zero indicates no limit.

 -h	host_key_file
     Specifies a file from which a host	key is read.  This option must
     be	given if sshd is not run as root (as the normal	host key files
     are normally not readable by anyone but root).  The default is
     /etc/ssh/ssh_host_ecdsa_key, /etc/ssh/ssh_host_ed25519_key	and
     /etc/ssh/ssh_host_rsa_key.	 It is possible	to have	multiple host
     key files for the different host key algorithms.

 -i	     Specifies that sshd is being run from inetd(8).

 -o	option
     Can be used to give options in the	format used in the configura-
     tion file.	 This is useful	for specifying options for which there
     is	no separate command-line flag.	For full details of the
     options, and their	values,	see sshd_config(5).

 -p	port
     Specifies the port	on which the server listens for	connections
     (default 22).  Multiple port options are permitted.  Ports	speci-
     fied in the configuration file with the Port option are ignored
     when a command-line port is specified.  Ports specified using the
     ListenAddress option override command-line	ports.

 -q	     Quiet mode.  Nothing is sent to the system	log.  Normally the
     beginning,	authentication,	and termination	of each	connection is
     logged.

 -T	     Extended test mode.  Check	the validity of	the configuration
     file, output the effective	configuration to stdout	and then exit.
     Optionally, Match rules may be applied by specifying the connec-
     tion parameters using one or more -C options.

 -t	     Test mode.	 Only check the	validity of the	configuration file and
     sanity of the keys.  This is useful for updating sshd reliably as
     configuration options may change.

 -u	len  This option is used to specify the	size of	the field in the utmp
     structure that holds the remote host name.	 If the	resolved host
     name is longer than len, the dotted decimal value will be used
     instead.  This allows hosts with very long	host names that	over-
     flow this field to	still be uniquely identified.  Specifying -u0
     indicates that only dotted	decimal	addresses should be put	into
     the utmp file.  -u0 may also be used to prevent sshd from making
     DNS requests unless the authentication mechanism or configuration
     requires it.  Authentication mechanisms that may require DNS
     include HostbasedAuthentication and using a from="pattern-list"
     option in a key file.  Configuration options that require DNS
     include using a USER@HOST pattern in AllowUsers or	DenyUsers.

## Usage

## Reference
- [sshd\(8\)](https://www.freebsd.org/cgi/man.cgi?sshd(8))
