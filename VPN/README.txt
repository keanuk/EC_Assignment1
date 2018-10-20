The following configuration files will pass respectively all traffic,
some selected Informatics subnets, or all of EdLAN through the tunnel,
to either the Appleton Tower or Forum endpoint.  They use your DICE
username and password for authentication:

        Informatics-all-AT.ovpn
        Informatics-all-Forum.ovpn
        Informatics-only-AT.ovpn
        Informatics-only-Forum.ovpn
        Informatics-via-AT.ovpn
        Informatics-via-Forum.ovpn

We recommend that you normally use one of the -via- configurations.  The
others (-all- and -only-) are useful as workarounds in some circumstances
(explained on the computing.help.inf.ed.ac.uk site), but are generally not
as robust or as efficient.

The configuration files listed above will authenticate you using your
DICE username and password.  Alternatively, if you have Kerberos installed
you may be able to use that in conjunction with the files below.

The following configuration files will pass respectively all traffic
or all EdLAN traffic through the tunnel to either the Appleton Tower or
Forum endpoint.  As written they will probably only work on Windows at
the moment.  They use KX509 authentication:

        kx509-all-AT.ovpn
        kx509-all-Forum.ovpn
        kx509-via-AT.ovpn
        kx509-via-Forum.ovpn

Note that any other configuration files in these directories are for test
or development purposes.  They are NOT guaranteed to work, or indeed do
anything useful at all.

There is no need for you to download any of the RCS directories, unless you
are particularly interested in the configurations' change-histories.

$Id: README,v 1.7 2015/07/31 12:32:16 gdmr Exp $
