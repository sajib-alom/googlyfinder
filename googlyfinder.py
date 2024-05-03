# Required Libraries
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from colorama import Fore, Back, Style, init
import re

# Initialize colorama
init(autoreset=True)

# Google API credentials (replace with your own credentials)
API_KEY = "AIzaSyBiQc7wHnj0w-Pfu8BsnUgqnUsWDJU3YFI"
CX = "81e1fe94b402f4e93"

# Build Google Custom Search API resource
resource = build("customsearch", "v1", developerKey=API_KEY).cse()

# Function to display menu options
def showOptions():
    showHeader()
    print("\n")
    print("  1.  Subdomains")
    print("  2.  Directory Listing")
    print("  3.  Login and registration pages")
    print("  4.  Files")
    print("  5.  Keywords")
    print("  6.  Default pages")
    print("  7.  Software versions")
    print("  8.  Error messages")
    print("  9.  Databases")
    print("  10. Email addresses and phone numbers")
    print("  11. Employees")
    print("  0.  Exit")
    
    showInput()

# Function to display the header
def showHeader():
    print("\n")
    print(Fore.YELLOW + Style.BRIGHT + 
          "  ======================================================================================================================================================")

    banner = """
  .oooooo.                                   oooo              oooooooooooo  o8o                    .o8                                             .o        .oooo.             
 d8P'  `Y8b                                  `888              `888'     `8  `"'                   "888                                           o888       d8P'`Y8b            
888            .ooooo.   .ooooo.   .oooooooo  888  oooo    ooo  888         oooo  ooo. .oo.    .oooo888   .ooooo.  oooo d8b           oooo    ooo  888      888    888           
888           d88' `88b d88' `88b 888' `88b   888   `88.  .8'   888oooo8    `888  `888P"Y88b  d88' `888  d88' `88b `888""8P            `88.  .8'   888      888    888           
888     ooooo 888   888 888   888 888   888   888    `88..8'    888    "     888   888   888  888   888  888ooo888  888                 `88..8'    888      888    888           
`88.    .88'  888   888 888   888 `88bod8P'   888     `888'     888          888   888   888  888   888  888    .o  888                  `888'     888  .o. `88b  d88'           
 `Y8bood8P'   `Y8bod8P' `Y8bod8P' `8oooooo.  o888o     .8'     o888o        o888o o888o o888o `Y8bod88P" `Y8bod8P' d888b                  `8'     o888o Y8P  `Y8bd8P'            
                                  d"     YD        .o..P'                                                                                                                        
                                  "Y88888P'        `Y8P'                                                                                                                         
"""
    
    print(banner)
    print(Fore.YELLOW + Style.BRIGHT + 
          "  							          By Error404       							                   ")
    print(Fore.YELLOW + Style.BRIGHT + 
          "  ======================================================================================================================================================")

# Function to process user input and execute search
def showInput():
    while True:
        try:
            domain = input("\n  Type a domain name: ").strip()
            if not domain:
                print(Fore.RED + "Domain name cannot be empty.")
                continue

            option = int(input("  Select an option (0 to 11): "))
            
            if option == 0:
                print("Exiting...")
                break
            elif 1 <= option <= 11:
                search(domain, option)
            else:
                print(Fore.RED + "Invalid option. Please choose between 1 and 11.")
            
            if input("  Do you want to try another option? (Y/N): ").lower() != 'y':
                break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number for the option.")
        except Exception as e:
            print(Fore.RED + "An error occurred:", e)

# Function to perform specific searches
def search(domain, option):
    site_query = 'site:' + domain
    resultsQueries = []
    results = []

    try:
        if option == 1:  # Subdomains
            query = site_query + ' -inurl:www.' + domain
            resultsQueries.append(resource.list(q=query, cx=CX).execute())

        elif option == 2:  # Directory Listing
            query = site_query + ' intitle:"Index of"'
            resultsQueries.append(resource.list(q=query, cx=CX).execute())

        elif option == 3:  # Login and Registration Pages
            query = site_query + ' (Login | "Sign in" | "Sign up" | Portal)'
            resultsQueries.append(resource.list(q=query, cx=CX).execute())
        
        elif option == 4:  # Files
            file_exts = ["pdf", "doc", "docx", "txt", "xls", "xml", "ini", "config", "cfg"]
            for ext in file_exts:
                query = site_query + f" ext:{ext}"
                resultsQueries.append(resource.list(q=query, cx=CX).execute())

        elif option == 5:  # Keywords
            keywords = input("  Enter keywords to search for (comma-separated): ").split(',')
            for keyword in keywords:
                query = site_query + f" intext:{keyword.strip()}"
                resultsQueries.append(resource.list(q=query, cx=CX).execute())

        elif option == 6:  # Default Pages
            query = site_query + ' ("Welcome to" | Default)'
            resultsQueries.append(resource.list(q=query, cx=CX).execute())

        elif option == 7:  # Software Versions
            # Google Dorking for software versions and technologies
            advanced_queries = [
                'powered by', 'built with', 'version', 'Index of', 'index of'
            ]
            for aq in advanced_queries:
                query = site_query + f' "{aq}"'
                resultsQueries.append(resource.list(q=query, cx=CX).execute())

        elif option == 8:  # Error Messages (404, 403, etc.)
            # Queries for common HTTP error responses
            error_queries = [
                '404 Not Found', 'Page Not Found', 'Error 404',
                '403 Forbidden', 'Access Denied', 'Forbidden',
                '500 Internal Server Error', '502 Bad Gateway', '503 Service Unavailable'
            ]
            for eq in error_queries:
                query = site_query + f' "{eq}"'
                resultsQueries.append(resource.list(q=query, cx=CX).execute())

        elif option == 9:  # Databases/SQL Files
            # Search for SQL-related terms
            db_queries = ['SQL', 'MySQL', 'Database', 'Table', 'Schema', 'Dump']
            for dq in db_queries:
                query = site_query + f" intext:{dq}"
                resultsQueries.append(resource.list(q=query, cx=CX).execute())

        elif option == 10:  # Email Addresses and Phone Numbers
            query = site_query + ' (Email | Phone)'
            resultsQueries.append(resource.list(q=query, cx=CX).execute())

        elif option == 11:  # Employees
            query = 'site:linkedin.com/in intitle:' + domain.split('.')[0]
            resultsQueries.append(resource.list(q=query, cx=CX).execute())
    
        results = getResults(resultsQueries)

        if results:
            showResults(results)
            createResultsFile(results, f"Option {option}", domain)
        else:
            print(Fore.RED + Style.BRIGHT + "\n  No results found.")
    
    except HttpError as e:
        print(Fore.RED + "Google API Error:", e)
    except Exception as e:
        print(Fore.RED + "An error occurred:", e)

# Function to show results
def showResults(results):
    print("  =================================================================================================")
    print(Fore.GREEN + Style.BRIGHT + "  Results:", len(results))
    print("  =================================================================================================")
    for item in results:
        if 'title' in item:
            print(Fore.MAGENTA + Style.BRIGHT + "  " + item['title'])
        if 'link' in item:
            print(Fore.GREEN + "  " + item['link'])
        if 'snippet' in item:
            print(Fore.YELLOW + Style.BRIGHT + "  " + item['snippet'])
        print(" ")

# Function to retrieve results from queries
def getResults(resultsQueries):
    results = []
    for resultQuery in resultsQueries:
        if 'items' in resultQuery:
            results.extend(resultQuery['items'])
    return results

# Function to save results to a text file
def createResultsFile(results, title, domain):
    file_name = f"{title} - {domain}.txt"
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(f"{title} - {domain}\n")
        f.write("=================================================================================================\n")
        for item in results:
            if 'title' in item:
                f.write(f"Title: {item['title']}\n")
            if 'link' in item:
                f.write(f"Link: {item['link']}\n")
            if 'snippet' in item:
                f.write(f"Snippet: {item['snippet']}\n")
            f.write("=================================================================================================\n")

# Start the script
showOptions()

