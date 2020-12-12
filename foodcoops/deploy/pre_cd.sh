#!/usr/bin/env bash

mkdir -p ~/.ssh

echo "${SSH_DEPLOY_KEY}" > ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_rsa
chmod 700 ~/.ssh

if [ -f known_hosts ]; then
    mv known_hosts ~/.ssh/known_hosts
fi
if [ ! -f ~/.ssh/known_hosts ]; then
    ssh-keyscan -H "${DESTINATION_SERVER}" >> ~/.ssh/known_hosts
fi
