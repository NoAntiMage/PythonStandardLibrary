try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

output = StringIO()
output.write('This goes into the buffer.')
print >>output , 'And so does this.'

print output.getvalue()
output.close()

input = StringIO('inital value for read buffer.')
print(input.read())
