#!/bin/bash
#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

echo 'Working directory' `pwd`
cd unload-service

make tests
exit_status=$?
if [ $exit_status -ne 0 ]; then
    echo "make tests failed with exit status: $exit_status"
    make clean
    exit $exit_status
fi
make clean