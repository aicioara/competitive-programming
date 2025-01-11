#!/bin/bash

set -e

FILES_TO_RESTORE=( a.cpp a.py )
SAVE_FOLDER="submissions"

#############################

GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

THIS_DIR=$(dirname "$0")
cd ${THIS_DIR}

restore_commands=()

for file in "${FILES_TO_RESTORE[@]}"; do
    latest_copy=$( ls -t ${SAVE_FOLDER} | grep ${file} | head -n 1)
    latest_copy="${SAVE_FOLDER}/${latest_copy}"
    if [ ! -z ${latest_copy} ]; then
        restore_point=()
        restore_commands+=( "cp '${latest_copy}' '${file}'" )
    fi
done

./save.sh

for restore_command in "${restore_commands[@]}"; do
    echo "${restore_command}"
    eval ${restore_command}
done

printf "${GREEN}Restore successful!${NC}\n"
