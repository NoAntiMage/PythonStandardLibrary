import textwrap

sample_text = '''
The textwrap module can be used to format text for output in situations where pretty-printing is desired. It offers
10 Text
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''

dedented_text = textwrap.dedent(sample_text)
print(textwrap.fill(dedented_text,
                    initial_indent='',
                    subsequent_indent='' * 4,)

      )
