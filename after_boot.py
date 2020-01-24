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
OLD_VG=str(input("Provide OLD VG name: "))
CONF='etc'
OLDSLES='mnt'
LOG='set_configuration.log'
COMMAND='systemctl'
OPSPACKAGE='./opsware-agent-60.0.71639.1-linux-SLES-12-X86_64'

#TIME=$(date +"%T:%m-%d-%y")

##set mountpoint from old sles11 server
os.system('mount /dev/OLD_VG/root /OLDSLES/')
os.system('mount /dev/OLD_VG/opt /OLDSLES/opt/')
os.system('mount /dev/OLD_VG/tmp /OLDSLES/tmp/')
os.system('mount /dev/OLD_VG/home /OLDSLES/usr2/local/')



###passwd and shadow

os.system('pwconv')


######apx agent install task######
if os.path.exists("/opt/apxpccp/"):
   os.system('tar -xvf  /opt/apxpccp/apxpccp_lin64_create_pks_after_move.tar')
   os.system('/opt/apxpccp/./recreate_pccp_pks_after_move.sh')
   os.system('/opt/apxpccp/./apxcntl restart')

####install DP agent####
if os.path.exists("rpm -Uvh /mnt/tmp/backup/omni_packages/"):

    os.system('rpm -Uvh /mnt/tmp/backup/omni_packages/*.rpm')

####post checkes######
if os.path.exists("/root/scripts/migration/post_migration_checks"):
                  
     os.system('/root/scripts/migration/./post_migration_checks')
