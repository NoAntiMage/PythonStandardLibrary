# coding: UTF-8

from ConfigParser import SafeConfigParser

config_dir = './config.ini'

config = SafeConfigParser()
config.read(config_dir)

for section_name in config.sections():
    print 'Section:', section_name
    print ' Options:', config.options(section_name)
    for name, value in config.items(section_name):
        print ' %s = %s' % (name, value)
    print
