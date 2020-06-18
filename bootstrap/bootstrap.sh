#! /bin/bash

scriptDir=${BASH_SOURCE%/*}/

ansible-playbook --ask-vault-pass -v $scriptDir/bootstrap.yml
