Automation tool for collecting headers and cookies

I developed this tool using the requests library (Python) as a solution for pentesters. I encountered time constraints on a project where I had just a few days to test a large number of URLs.

This tool helps identify whether a page is active, which headers the host contains (allowing us to check for missing security headers), and the cookies. It achieves in seconds what would take 5 to 10 minutes manually to identify all these parameters.

I used the requests library and added some custom functions to organize the information as much as possible and help save time.
