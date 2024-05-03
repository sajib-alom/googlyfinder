# GooglyFinder

- "**GooglyFinder**" is a pentest tool that allows you to automate advanced Google queries from a domain name.
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

- The results obtained are saved in a text file, in the same path where the script is located.
- Google's "Custom Search API" is used. This API is limited to 100 free queries per day.
- For most queries, the first page of results is returned. Only for some queries, the first two or three pages of results are returned.
- Due to the nature of Google searches, it is possible to obtain unwanted, repetitive, or false positive results.

For this tool to work you must generate and obtain an API Key for "Custom Search API" and create a Programmable Search Engine. The steps are described below.




This tool uses the Google Custom Search API to find specific information related to a given domain. It can search for subdomains, files, error messages, software versions, and more.

1. Generate API Key for [Custom Search API](https://developers.google.com/custom-search/v1/introduction)

2. Create a Programmable Search Engine and get the [Search Engine ID CX](https://programmablesearchengine.google.com/controlpanel/create)

3. Insert your API Key and search engine ID into the variables indicated in the source code of the script (API_KEY and CX) 

4. Additionally, you can use the [Google console](https://console.cloud.google.com/apis/dashboard) to control enabled APIs, credentials, queries, usage and so on 


## Installation

To install the tool, clone this repository and run the installation script:

```bash
git clone https://github.com/sajib-alom/googlyfinder.git
cd googlyfinder


# Step 1: Install dependencies
pip install google-api-python-client colorama

# Step 2: Run the code using python
python3 googlyfinder.py
```
## Demo
Some screenshots showing how the tool works are attached below.

![t1](https://github.com/sajib-alom/googlyfinder/assets/92325515/5fcba16e-4f6b-4d15-bd88-b89c6cf8501d)
![t2](https://github.com/sajib-alom/googlyfinder/assets/92325515/72fe13c8-ab6e-48ab-8bb2-643d8bdb2721)
![t3](https://github.com/sajib-alom/googlyfinder/assets/92325515/52cee712-ffd4-4555-b2fb-843fface236b)



[MIT](https://choosealicense.com/licenses/mit/)
