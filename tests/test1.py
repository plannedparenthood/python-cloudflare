#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from CloudFlare.cloudflare import Cloudflare

import pytest

def test_ips():
    cf = CloudFlare()
    ips = cf.ips.get()
    assert ips

