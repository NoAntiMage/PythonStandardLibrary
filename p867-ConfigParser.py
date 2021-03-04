from ConfigParser import SafeConfigParser

config_dir = './config.ini'

config = SafeConfigParser()
config.read(config_dir)

print('Integers:')
string_value = config.get('redis', 'password')
value = config.getint('redis', 'port')


print(string_value)
print(type(string_value))

print(value)
print(type(value))
