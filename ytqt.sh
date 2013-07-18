#!/bin/bash

RES_PATH="`dirname $0`"
VERSION=`cat "$RES_PATH/VERSION"`
YOUTUBE_DL="$RES_PATH/youtube-dl"
GET_URL="$RES_PATH/get_url.scpt"

echo "     Ytqt $VERSION"

echo -n "Getting URL from Safari..."
YT_URL="`osascript $GET_URL`"
echo "done!"

if [[ $YT_URL != http*youtube*watch*v* ]];
then
    echo "The following foreground page is not a YouTube video:"
    echo $YT_URL
    sleep 3
    exit
fi

echo -n "Getting video URL from YouTube..."
VID_URL="`$YOUTUBE_DL -g -f 38/37/22/18 $YT_URL`"
if [[ $? != 0 ]];
then
    sleep 3
    exit
fi
echo "done!"

echo -n "Opening QuickTime..."
open -a "QuickTime Player" $VID_URL
echo "done!"

sleep 1
