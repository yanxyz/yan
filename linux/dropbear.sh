#!/bin/bash
#20121106

function install_xinetd {
    if [ ! -f /usr/sbin/xinetd ]
	then
        apt-get -y install xinetd
	fi
}

function install_dropbear {
    apt-get -y install dropbear

    # Disable SSH
	if [ -f /etc/init.d/ssh ]
	then
       touch /etc/ssh/sshd_not_to_be_run
       invoke-rc.d ssh stop
	fi

	# xinetd
	if [ "$1" == "n" ]
	then
	    if [ ! -f /usr/sbin/xinetd ]
	    then
            apt-get -y install xinetd
	    fi

    	invoke-rc.d dropbear stop
		update-rc.d dropbear disable
		cat > /etc/xinetd.d/dropbear <<END
service ssh
{
    disable         = no
    user            = root
    socket_type     = stream
    only_from       = 0.0.0.0
    wait            = no
    protocol        = tcp
    server          = /usr/sbin/dropbear
    server_args     = -i -s
    port            = 12345
    type            = unlisted
}
END
        invoke-rc.d xinetd restart
	fi
}

install_dropbear $1
echo -e  "\033[31mwell done!\033[0m"
