from boto.manage.server import Server
from boto.manage.volume import Volume
from six import print_
import time

print_('--> Creating New Volume')
volume = Volume.create()
print_(volume)

print_('--> Creating New Server')
server_list = Server.create()
server = server_list[0]
print_(server)

print_('----> Waiting for Server to start up')
while server.status != 'running':
    print_('*')
    time.sleep(10)
print_('----> Server is running')

print_('--> Run "df -k" on Server')
status = server.run('df -k')
print_(status[1])

print_('--> Now run volume.make_ready to make the volume ready '\
    'to use on server')
volume.make_ready(server)

print_('--> Run "df -k" on Server')
status = server.run('df -k')
print_(status[1])

print_('--> Do an "ls -al" on the new filesystem')
status = server.run('ls -al %s' % volume.mount_point)
print_(status[1])

