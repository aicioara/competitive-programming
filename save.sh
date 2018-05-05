#!/bin/bash

FILES_TO_SAVE=( a.cpp a.py )
SAVE_FOLDER="submissions"

GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

for file in "${FILES_TO_SAVE[@]}"; do
    latest_copy=$( ls -t ${SAVE_FOLDER} | grep ${file} | head -n 1)
    if [ ! -z ${latest_copy} ]; then
        cmp --silent "${file}" "${latest_copy}"
        rc=$?
        if [ $rc -ne 0 ]; then
            printf "${YELLOW}SKIPPED${NC}: ${file} == ${latest_copy}\n"
            continue
        fi
    fi

    DATE=`date '+%Y_%m_%d_%H_%M_%S'`
    new_file_name="${SAVE_FOLDER}/${DATE}_${file}"
    printf "${GREEN}SUCCESS${NC}: Copied ${file}\n"
    cp "${file}" "${new_file_name}"
done
