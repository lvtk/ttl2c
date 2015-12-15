#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2012 Michael Fisher <mfisher31@gmail.com>

''' This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public Licence as published by
the Free Software Foundation, either version 3 of the Licence, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
file COPYING for more details. '''

def options (opt):
    opt.load ('compiler_c compiler_cxx')

def configure (conf):
    conf.load ('compiler_c compiler_cxx')

def build (bld):
    glob = bld.path.ant_glob
    bld.program (
        includes = ['src'],
        source   = glob ('src/*.cpp'),
        name     = 'ttl2c',
        target   = 'bin/ttl2c'
    )
