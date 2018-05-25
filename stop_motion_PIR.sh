#!/bin/sh
ps -ef | grep motion_PIR | awk '{print $2}' | xargs   kill
