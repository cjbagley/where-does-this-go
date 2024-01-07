# where-does-this-go
Find out where that marketing URL actually goes, rather than hoping it's not malicious!

I sometimes get emails with links to follow, but if you hover over them, you get something like:

https://clickymail.drop.io/25s23523w1235qt/as325q2wtgasgasgwat

I'm never sure about clicking those - it's *probably* okay, but who knows.

To this end, I just want to know where the actual end url behind the mail url is, for example it might just go to:

https://bobski.com/great-offer

I built this little CLI tool so you can pass in a url, and Python will follow the headers only to see where it goes.
