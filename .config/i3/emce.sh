#!/usr/bin/env bash

# sleep 1
emacsclient -c -e "(counsel-recentf)" -a ""
i3-msg "[instance=emacs] move right"
# emacsclient -c -a "" && i3-msg "[instance=emacs] mark edit, move scratchpad"
# sleep 1
# i3-msg "move right"
# emacsclient -c -a ""; i3-msg "mark edit, move scratchpad"
# i3-msg "mark \"edit\", move scratchpad"


# exec --no-startup-id "sleep 1; i3-msg '[instance=urxvt] mark term, move scratchpad'"
