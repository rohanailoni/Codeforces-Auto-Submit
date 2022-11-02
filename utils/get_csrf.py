from bs4 import BeautifulSoup
def get_csrf(response):
    
    soup = BeautifulSoup(response.text, 'html.parser')
    if soup.input['type']=="hidden" and soup.input['name']=="csrf_token":
        return soup.input['value']
    return None