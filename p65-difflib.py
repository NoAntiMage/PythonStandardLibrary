from difflib import SequenceMatcher


def show_result(s, a, b):
    i, j, k = s.find_longest_match(0, 5, 0, 9)
    print(' i = %d' %i)
    print(' j = %d' %j)
    print(' k = %d' %k)
    print('A[i:i+k] = %r' %a[i:i+k])
    print('B[j:j+k] = %r' %b[j:j+k])

A = 'abcd'
B = 'abcd abcd'

print('A = %r ' % A)
print('B = %r ' % B)

print('\n Without junk detection: ')
show_result(SequenceMatcher(None, A, B), A, B)

print('\n Treat spaces as junk:')
show_result((SequenceMatcher(lambda x: x =="", A, B)),A,B)

