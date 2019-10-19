import zipfile

for filename in ['README.txt', 'exmaple.zip', 'bad_example.zip', 'notthere.zip']:
    print '%15s %s' % (filename, zipfile.is_zipfile(filename))
