# Pyperclip
```pyperclip``` can be used to copy and paste from the clipboard.
```python
import pyperclip
pyperclip.copy('''Hi <recipient>,

Thank you for you hard work on this.

I'm pleased to report that this matter has...
''')
pyperclip.paste()
```
```
Hi <recipient>,

Thank you for you hard work on this.

I'm pleased to report that this matter has...
```
Using ```pyperclip.paste()``` in the console will paste the result. 
```pyperclip.copy()``` allows for pasting outside of the console (i.e. into an email).
