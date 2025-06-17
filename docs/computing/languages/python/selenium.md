# Selenium
Selenium enables web browser automation.

```python
from selenium import webdriver

# Open a firefox web browser.
options = webdriver.FirefoxOptions()
service = webdriver.FirefoxService(executable_path="/snap/bin/geckodriver")
browser = webdriver.Firefox(options=options, service=service)

# Navigate to a webpage, allow the page to load before reading the page source code. 
browser.get('https://inventwithpython.com')
browser.implicitly_wait(90)
source = browser.page_source
print(source)
```
