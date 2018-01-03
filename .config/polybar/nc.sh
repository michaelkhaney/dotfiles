#!/bin/bash

wget -q --tries=10 --timeout=20 --spider http://google.com
if [[ $? -eq 0 ]]; then
    echo "%{F#9fc59f}%{F-}"
else
    echo "%{F#ff0505}%{F-}"
fi
