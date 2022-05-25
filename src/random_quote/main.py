import requests


QUOTE_URL = 'https://quotes.rest/qod'

def get_quote():
    """Get a random quote."""
    resp = requests.get(QUOTE_URL)
    quote = resp.json()['contents']['quotes'][0]['quote']
    return quote

def display_quote():
    print(f'Quote of the day is :- {get_quote()}')


if __name__ == '__main__':
    display_quote()
