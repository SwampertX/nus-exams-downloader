import subprocess
import sys
import getpass
import examdownloader

module = raw_input("Which module? ").lower().split()
username = 'E0325774'
yearsem = raw_input("What AY and sem is it now? eg. y1s1\n").strip()

def startDownload(args):

    global module, username
    password = ''

    if len(args) > 0:
        module = args[0]
        username = args[1]

    password = getpass.getpass('Enter password for ' + username + ': ')
    ed = examdownloader.examdownloader('CLI')


    def updateStatus(msg, type='normal'):
        print msg

    def downloadCallback(status, lastfile='', numFiles=0):
        if status:
            updateStatus(str(numFiles) + ' papers downloaded successfully!', 'success')
        else:
            updateStatus('Paper not released by Department', 'error')
    for mod in module:
        destination = '/home/titanx/nus/pyp/' + yearsem + '/' + mod + '/'
        ed.getContents(mod, username, password, destination, downloadCallback, updateStatus)

if __name__ == '__main__':
    startDownload(sys.argv[1:])
