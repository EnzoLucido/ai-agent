import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

def search(query):
    """
    Perform a Google search for the given query and return formatted search results.

    Args:
        query (str): The search query.

    Returns:
        str: Formatted search results or an error message.
    """
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(f'https://www.google.com/search?q={query}', headers=headers)
        response.raise_for_status()  # Check if the request was successful

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the main search results container
        results = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')

        if not results:
            print("No search results found")
            return 'No results found'

        # Collect the details of all results
        all_results = []
        for result in results:
            title = result.find_previous('div', class_='BNeawe vvjwJb AP7Wnd UwRFLe').text if result.find_previous('div', class_='BNeawe vvjwJb AP7Wnd UwRFLe') else 'No title found'
            snippet = result.text if result else 'No snippet found'
            link = result.find_previous('a')['href'] if result.find_previous('a') else 'No link found'
            
            # Combine the details into a single string for each result
            result_text = f"Title: {title}\nSnippet: {snippet}\nLink: {link}\n"
            all_results.append(result_text)

        # Join all results into one giant string
        giant_string = "\n".join(all_results)
        
        return giant_string
    except requests.exceptions.RequestException as e:
        return f'Error during request: {e}'


def sanitize_search_term(search_term):
    """
    Ensure the search term is safe by removing special characters.

    Args:
        search_term (str): The search term to sanitize.

    Returns:
        str: The sanitized search term.
    """
    
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', search_term)
    return sanitized 

def date():
    """
    Get the current date and format it for instructions.

    Returns:
        str: Formatted current date string.
    """
    
    date_and_time = datetime.now()
    date = date_and_time.strftime("%B %d, %Y")
    date_instruction = f'You know that the date is {date},'
    
    return date_instruction 
