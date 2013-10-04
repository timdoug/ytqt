#!/usr/bin/python

import os
import shutil
import urllib2
import datetime
import tempfile
import subprocess

temp_dir = tempfile.mkdtemp()
youtube_dl_path = temp_dir + '/youtube-dl'
version_path = temp_dir + '/VERSION'

print 'Downloading youtube-dl...'
with open(youtube_dl_path, 'w') as f:
    f.write(urllib2.urlopen('https://yt-dl.org/latest/youtube-dl').read())
os.chmod(youtube_dl_path, 0755)

version = datetime.datetime.now().strftime('%Y.%m.%d.%H.%M')
with open(version_path, 'w') as f:
    f.write(version)

print 'Making Ytqt.app...'
subprocess.Popen(' '.join([
    '/usr/local/bin/platypus',
    '-a Ytqt',
    '-o "Text Window"',
    '-p /bin/bash',
    '-i assets/ytqt.icns',
    '-u timdoug',
    '-V ' + version,
    '-I com.timdoug.ytqt',
    '-R',
    '-n "Helvetica 18"',
    '-f get_url.scpt',
    '-f ' + youtube_dl_path,
    '-f ' + version_path,
    '-l',
    '-y',
    'ytqt.sh',
    'Ytqt.app',
]), shell=True).communicate()

shutil.rmtree(temp_dir)
