#!/usr/bin/env python
#Created by GD
#created by GD
#created
###$1-old root VG name
###adding check function######

import os
import sys
import time

#######vars#####
CONF='etc'
OLDSLES='mnt'
LOG='set_configuration.log'
COMMAND='systemctl'
OPSPACKAGE='./opsware-agent-60.0.71639.1-linux-SLES-12-X86_64'

#TIME=$(date +"%T:%m-%d-%y")

##set mountpoint from old sles11 server
os.system('mount /dev/$1/root /OLDSLES/')
os.system('mount /dev/$1/opt /OLDSLES/opt/')
os.system('mount /dev/$1/tmp /$OLDSLES/tmp/')
os.system('mount /dev/$1/home /$OLDSLES/usr2/local/')



###passwd and shadow

os.system('pwconv')


######apx agent install task######

cd  /opt/apxpccp/
tar -xvf  apxpccp_lin64_create_pks_after_move.tar
./recreate_pccp_pks_after_move.sh
./apxcntl restart
check >> $LOGFILE
####install DP agent####
if os.path.exists("rpm -Uvh /mnt/tmp/backup/omni_packages/"):

    os.system('rpm -Uvh /mnt/tmp/backup/omni_packages/*.rpm')

####post checkes######
if os.path.exists("/root/scripts/migration/post_migration_checks):
     os.system('/root/scripts/migration/./post_migration_checks')
