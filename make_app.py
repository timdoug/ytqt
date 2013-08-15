#!/usr/bin/python

import os
import shutil
import urllib2
import tempfile
import subprocess

from bs4 import BeautifulSoup

youtube_dl_dir = tempfile.mkdtemp()
youtube_dl_path = youtube_dl_dir + '/youtube-dl'

print 'Getting latest youtube-dl version...'
soup = BeautifulSoup(urllib2.urlopen('http://rg3.github.io/youtube-dl/download.html').read())
youtube_dl_url = soup.findAll('a')[2]['href']
print 'Found', youtube_dl_url.split('/')[-2]

print 'Downloading youtube-dl...'
with open(youtube_dl_path, 'w') as f:
    f.write(urllib2.urlopen(youtube_dl_url).read())
os.chmod(youtube_dl_path, 0755)

print 'Making Ytqt.app...'
subprocess.Popen(' '.join([
    '/usr/local/bin/platypus',
    '-a Ytqt',
    '-o "Text Window"',
    '-p /bin/bash',
    '-i assets/ytqt.icns',
    '-u timdoug',
    '-V `cat VERSION`',
    '-I com.timdoug.ytqt',
    '-R',
    '-n "Helvetica 18"',
    '-f get_url.scpt',
    '-f ' + youtube_dl_path,
    '-f VERSION',
    '-l',
    '-y',
    'ytqt.sh',
    'Ytqt.app',
]), shell=True).communicate()

shutil.rmtree(youtube_dl_dir)
