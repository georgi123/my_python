#!/bin/bash

###Created by GD
###script have to deploy movere agent

ps -o command 1|grep systemd >/dev/null

for servers in $(</usr2/local/dimitrge/asure_list)
 do
  if [ $? -eq 0 ]
   then
    salt $servers state.sls asure
    ssh root@$servers 'hostname'
   else
   scp LinuxBot.zip root@$servers:/root
   
   ssh root@$servers 'unzip /root/LinuxBot.zip'
   scp /srv/salt/files/asure/asure_agent.sh  root@$servers:/root/LinuxBot
   ssh root@$servers 'chmod +x /root/LinuxBot/*'
   ssh root@$servers '/root/LinuxBot/./asure_agent.sh' 

 fi
done
