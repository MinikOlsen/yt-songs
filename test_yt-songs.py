# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from subprocess import check_output
from tempfile import gettempdir


def test_free_songs():
    '''Tries to download a list of free songs'''
    result = run_cmd('yt-songs test_songs ' + gettempdir())
    assert 'successfully' in result


def run_cmd(cmd):
    '''Run a shell command `cmd` and return its output.'''
    return check_output(cmd, shell=True).decode('utf-8')
