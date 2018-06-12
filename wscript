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

VERSION = '1.0.1'

def options (opt):
    opt.load ('compiler_c compiler_cxx')

def configure (conf):
    conf.load ('compiler_c compiler_cxx')

    conf.define('VERSION', VERSION)

    conf.check(lib='boost_system', uselib_store='BOOST', mandatory=False)
    conf.check(header_name='boost/spirit/home/classic/utility/chset.hpp',
               uselib_store='BOOST', mandatory=True)
    conf.check(header_name='boost/spirit/include/classic_dynamic.hpp',
               uselib_store='BOOST', mandatory=True)
    conf.check(header_name='boost/spirit/include/classic_core.hpp',
               uselib_store='BOOST', mandatory=True)
    conf.check(header_name='boost/spirit/include/classic_parse_tree.hpp',
               uselib_store='BOOST', mandatory=True)
    conf.check(header_name='boost/spirit/include/classic_utility.hpp',
               uselib_store='BOOST', mandatory=False)
    conf.check(header_name='boost/spirit/include/classic_ast.hpp',
               uselib_store='BOOST', mandatory=True)

def build (bld):
    glob = bld.path.ant_glob
    bld.program (
        includes = ['src'],
        source   = glob ('src/*.cpp'),
        name     = 'ttl2c',
        target   = 'bin/ttl2c',
        use      = ['BOOST']
    )
