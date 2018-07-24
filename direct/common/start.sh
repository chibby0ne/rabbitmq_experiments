#!/bin/bash

GREEN='\033[32m'
RED='\033[31m'
NC='\033[0m'


function log() {
    echo -e "$GREEN[r]$NC$RED $1 $NC"
}

if [[ -n "$WATCHEXEC_WRITTEN_PATH" ]]; then
    log "File: $WATCHEXEC_WRITTEN_PATH changed, reloading"
fi

log "Starting: $*"
"$@"
log "Exit $?"
