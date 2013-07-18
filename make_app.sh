#!/bin/sh

rm -rf Ytqt.app

/usr/local/bin/platypus \
-a Ytqt \
-o 'Text Window' \
-p /bin/bash \
-u timdoug \
-V `cat VERSION` \
-I com.timdoug.ytqt \
-R \
-n 'Helvetica 18' \
-f get_url.scpt \
-f contrib/youtube-dl \
-l \
ytqt.sh \
Ytqt.app
