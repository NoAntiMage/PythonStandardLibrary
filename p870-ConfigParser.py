from ConfigParser import SafeConfigParser
import sys

config_dir = './config.ini'

config = SafeConfigParser()
config.read(config_dir)

# All options must be set as strings.
config.add_section('tmp_section')
config.set('tmp_section', 'name', 'wujimaster')
config.set('tmp_section', 'job', 'devops')

for section in config.sections():
    print(section)
    for name, value in config.items(section):
        print(' %s = %r' % (name, value))

