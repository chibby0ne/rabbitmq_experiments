#!/bin/bash


INSTALL_DIR=/bin

####################################################
#
# Wait for RabbitMQ service to be up
#
####################################################
WF_URL=https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
WF_BIN=wait-for-it.sh
RABBITMQ_HOST_PORT=rabbitmq_host:5672

if  [[ ! -x $INSTALL_DIR/$WF_BIN ]]; then
    curl -Ls $WF_URL --output $INSTALL_DIR/$WF_BIN
    chmod +x $INSTALL_DIR/$WF_BIN
fi

$WF_BIN  -t 0 $RABBITMQ_HOST_PORT -- echo "RabbitMQ is up"


####################################################
#
# Download/Run Watchexec to reload with every change
#
####################################################
WE_VERSION=1.8.6
WE_GZ=watchexec-$WE_VERSION-x86_64-unknown-linux-gnu.tar.gz
WE_URL=https://github.com/mattgreen/watchexec/releases/download/$WE_VERSION/$WE_GZ
WE_BIN=watchexec

# Download and install watchexec to restart containers main program, whenever
# there's a change in the code
if [[ ! -x $INSTALL_DIR/$WE_BIN ]]; then
    curl -Ls $WE_URL | tar -C $INSTALL_DIR --strip-components=1 -xzf - 
fi

# Extensions to watch for changes
FILES_TO_WATCH=py,txt

# Get this script's path
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Run watchexec to restart the containers
watchexec -n -r -e $FILES_TO_WATCH $SCRIPT_DIR/start.sh -- "$@"
