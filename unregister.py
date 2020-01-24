#!/usr/bin/env python
#Created by GD
#####use the script when have to revert from sles12 to sles11#######
impoer os
##unregister server from APX#####
if os.path.exists("/opt/apxpccp/pccprel") || os.path.exists("/opt/apxpccc/pccCrel"):
    os.system('/opt/apxpccp/pccprel exec,DCM/DCM_DEREG_$(hostname).scp')
    os.system('/opt/apxpccc/pccCrel exec,DCM/DCM_DEREG_$(hostname).scp')
if os.path.exists("/etc/machine-id"):
   os.remove("/etc/machine-id")
   os.system('dbus-uuidgen --ensure=/etc/machine-id')
##unregister server from HPSA##
if os.path,exists("/opt/opsware/agent/bin/agent_uninstall.sh"):
   os.system('/opt/opsware/agent/bin/agent_uninstall.sh --no_deactiva te --force')
   os.system('rm -r /opt/opsware');
