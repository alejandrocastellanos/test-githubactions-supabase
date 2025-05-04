#!/usr/bin/env bash
export $(cat .env | sed -e /^$/d -e /^#/d | xargs -0)

python main.py
