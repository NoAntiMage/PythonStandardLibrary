from ConfigParser import SafeConfigParser

config_dir = './config.ini'

config = SafeConfigParser()
config.read(config_dir)

print(config.get('redis', 'password'))
