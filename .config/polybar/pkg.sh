#!/bin/bash
pac=$(checkupdates 2> /dev/null | wc -l)
aur=$(cower -u 2> /dev/null | wc -l)

echo "$pac %{F#6f6f6f}%{F-} $aur"
