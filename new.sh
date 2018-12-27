#!/bin/bash

language="$1"
dir="$(date +%m-%d-%Y)"

mkdir -p ${dir}
touch ${dir}/README.md
cp -R templates/${language}/* ${dir}/
cd ${dir}
pip install -r requirements.txt
