#!/bin/bash

nc -z 8.8.8.8 53  >/dev/null 2>&1
online=$?
if [ $online -eq 0 ]; then
    echo "%{F#9fc59f}%{F-}"
else
    echo "%{F#ff0505}%{F-}"
fi
