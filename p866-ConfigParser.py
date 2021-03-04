from ConfigParser import SafeConfigParser

config_dir = './config.ini'

config = SafeConfigParser()
config.read(config_dir)

SECTIONS = ['redis']
OPTIONS = ['port', 'password']

for section in SECTIONS:
    has_section = config.has_section(section)
    print('%s section exists: %s' %(section, has_section))
    for candidate in OPTIONS:
        has_option = config.has_option(section,candidate)
        print('%s.%-12s :%s' %(section, candidate, has_option,))