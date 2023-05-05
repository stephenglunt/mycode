#!/usr/bin/env python3

import json
import requests
from pprint import pprint
from flask import Flask, redirect, url_for, render_template, request

URL = "http://127.0.0.1:2224/random"

resp = requests.get(URL).json()

pprint(resp)
