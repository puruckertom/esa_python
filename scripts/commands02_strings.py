#accessing documentation
import sys
dir(sys)
help(sys)
help(sys.argv)
help(str)
dir(str)
help(len)

#dunder
3 + 5
"Hello " + "world"

#object v call
help(len)
len('Geospiza magnirostris')

#quotes
aint = "ain't"
aint = 'ain"t'

#strings
darwins_finch = 'Geospiza magnirostris'
darwins_finch

darwin_quote ="'Great is the power of steady misrepresentation'"
darwin_quote
darwin_quote.lower()
darwin_quote[13:18]
darwin_quote[0] #Python is zero-based

#slicing
darwin_quote[0:1] 
darwin_quote[0:6]
darwin_quote[:12]
darwin_quote[12:]
darwin_quote[:12] + darwin_quote[12:]

#long quotes
long_darwin_quote = '''There is grandeur in this view
of life, with its several powers, having been originally 
breathed into a few forms or into one; and that, whilst 
this planet has gone cycling on according to the fixed 
law of gravity, from so simple a beginning endless 
forms most beautiful and most wonderful have been, and 
are being, evolved.'''
long_darwin_quote
print(long_darwin_quote)
len(long_darwin_quote)

#Hello Portland
"%s %s" % ('Hello','Portland')

