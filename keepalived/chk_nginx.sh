#!/bin/bash
status=`ps -C nginx --no-heading|wc -l`
if [ $status -eq 0 ]; then
    exit 1
fi

