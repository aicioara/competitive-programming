#!/bin/bash

set -e

FILES_TO_SAVE=( a.cpp a.py data.in )
SAVE_FOLDER="submissions"

#############################

GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

THIS_DIR=$(dirname "$0")
cd ${THIS_DIR}

for file in "${FILES_TO_SAVE[@]}"; do
    git update-index --assume-unchanged "${file}"
done

for file in "${FILES_TO_SAVE[@]}"; do
    latest_copy=$( ls -t ${SAVE_FOLDER} | grep ${file} | head -n 1)
    latest_copy="${SAVE_FOLDER}/${latest_copy}"
    if [ ! -z ${latest_copy} ]; then
        set +e
        cmp --silent "${file}" "${latest_copy}"
        rc=$?
        set -e
        if [ $rc -eq 0 ]; then
            printf "${YELLOW}SKIPPED${NC}: ${file} == ${latest_copy}\n"
            continue
        fi
    fi

    DATE=`date '+%Y_%m_%d_%H_%M_%S'`
    new_file_name="${SAVE_FOLDER}/${DATE}_${file}"
    cp "${file}" "${new_file_name}"
    printf "${GREEN}SUCCESS${NC}: Copied ${file}\n"
done
