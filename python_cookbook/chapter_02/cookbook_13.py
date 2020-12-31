

# 2.13 Aligning text strings

def printt(s):
    print("'"+s+"'")


text = 'Hello World'
printt(text.ljust(20))
printt(text.rjust(20))
printt(text.center(20))

printt(text.rjust(20, '='))
printt(text.center(20, '*'))

printt(format(text, '>20'))
printt(format(text, '<20'))
printt(format(text, '^20'))

printt(format(text, '=>20'))
printt(format(text, '*^20'))

printt('{:>10s} {:>10s}'.format('Hello', 'World'))


x = 1.2345
printt(format(x, '>10'))
printt(format(x, '^10.2f'))


printt('%-20s' % text)
printt('%20s' % text)
