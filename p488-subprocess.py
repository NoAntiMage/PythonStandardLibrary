import subprocess

print 'popen3:'
proc = subprocess.Popen('cat -; echo "to stderr" 1>&2',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )

msg = 'through stdin to stdout'
stdout_value, stderr_value = proc.communicate(msg)
print '\t pass through: ', repr(stdout_value)
print '\t stderr      : ', repr(stderr_value)
