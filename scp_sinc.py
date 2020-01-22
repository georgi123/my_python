#!/usr/bin/env python3
###Created by GD


import os
import sys
###variable
option=str(input())

###function

def copy():
   os.system('while read p; do scp /usr2/local/dimitrge/migration/after_boot.sh      root@$p:/root/scripts; done < /infra/linux/SUSE-Manager/sap_list')
   os.system('while read p; do scp /usr2/local/dimitrge/migration/sles11to12     root@$p:/root/scripts; done < /infra/linux/SUSE-Manager/sap_list')
   os.system('while read p; do scp /usr2/local/dimitrge/migration/unregister.pl     root@$p:/root/scripts; done < /infra/linux/SUSE-Manager/sap_list')
   os.system('while read p; do scp /usr2/local/dimitrge/migration/HPOA_12.06_Linux_64_v1.tar.gz      root@$p:/tmp ; done < /infra/linux/SUSE-Manager/sap_list')
   os.system('while read p; do scp -r /usr2/local/dimitrge/migration/backup      root@$p:/tmp ; done < /infra/linux/SUSE-Manager/sap_list')

if option == 'help':
   print('use help for posible option')
   print('copy files from suse-mgr to nodes')

elif option == 'copy':
   copy()
else:
   print('USE CORRECT OPTION')
