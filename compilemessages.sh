#!/usr/bin/env bash
# Generate all .mo files from the corresponding .po files for i18n
# By Fabien Batteix

# Current directory
readonly here=`pwd`

# Compile messages in root locale/ directory
echo Compile .mo in root
python "$here/manage_prod.py" compilemessages

# Compile messages in all apps locale/ directories
for d in apps/*/ ; do

    # Avoid the __pychache__ directory (not an apps)
    if [[ "$d" != *"__pycache__"* ]]
    then
        echo Compile .mo in "$d"
        (cd "$d" && python "$here/manage_prod.py" compilemessages)
    fi
done
