#! /bin/bash

scriptDir=${BASH_SOURCE%/*}/

ansible-playbook -v $scriptDir/bootstrap.yml
