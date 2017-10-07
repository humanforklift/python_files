#! /usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage:./mcb.pyw save <keyword> - Saves clipboard to keyword
#       ./mcb.pyw <keyword> - Loads keyword to clipboard
#       ./mcb.pyw list - Loads all keywords to clipboard
#       ./mcb.pyw delete <keyword> - Deletes a keyword from the shelf
#       ./mcb.pyw deleteAll - Deletes all keywords

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# Delete keyword from shelf
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1] == 'deleteAll':
        for i in mcbShelf:
            del mcbShelf[i]
mcbShelf.close()
