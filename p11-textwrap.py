import textwrap

sample_text = '''
The textwrap module can be used to format text for output in situations where pretty-printing is desired. It offers
10 Text
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''


dedentd_text = textwrap.dedent(sample_text).strip()
for width in [45, 70]:
    print('%d Columns: \n' % width)
    print(textwrap.fill(dedentd_text, width=width))
    print()
