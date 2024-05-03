# GooglyFinder

- "GooglyFinder" is a pentest tool that allows you to automate advanced Google queries from a domain name.
- It provides 11 different options to search for sensitive information and security vulnerabilities.
  1. Subdomains
  2. Directory Listing
  3. Login and registration pages
  4. Files
  5. Keywords
  6. Default pages
  7. Software versions
  8. Error messages
  9. Databases
  10. Email addresses and phone numbers
  11. Employees

- Queries are executed in Spanish and English.
- The results obtained are saved in a text file, in the same path where the script is located.
- Google's "Custom Search API" is used. This API is limited to 100 free queries per day.
- For most queries the first page of results is returned. Only for some queries the first two or three pages of results are returned.
- Due to the nature of Google searches, it is possible to obtain unwanted, repetitive or false positive results.

For this tool to work you must generate and obtain an API Key for "Custom Search API" and create a Programmable Search Engine. The steps are described below.

