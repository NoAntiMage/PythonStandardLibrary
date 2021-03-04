from ConfigParser import SafeConfigParser

config_dir = './config.ini'

config = SafeConfigParser()
config.read(config_dir)

for section in config.sections():
    print(section)
    for name, value in config.items(section):
        print(' %s = %r' % (name, value))

config.remove_option('tmp_section', 'name')
config.remove_section('temp_section')
