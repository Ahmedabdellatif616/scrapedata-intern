import requests
from bs4 import BeautifulSoup
import re
import time 
import schedule 
def scrape_twitter(url,ticker_pattern) -> int:
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    tweets=soup.find_all('div',{'data-testid':'tweet'})
    mentions=0
    for tweet in tweets:
        text=tweet.get_text()
        mentions+=len(re.findall(r'\$'+re.escape(ticker_pattern),text)) 
        return mentions
    return 0
def main(twitter_accounts, interval):
    ticker_pattern = r'\$\b[A-Za-z]{3,4}\b'  # Pattern for $ followed by 3 or 4 letters
    while True:
        total_mentions = 0
        for account in twitter_accounts:
            mentions = scrape_twitter(account, ticker_pattern)
            total_mentions += mentions
            print(f"Ticker symbols were mentioned {mentions} times on {account}.")
        
        print(f"Total mentions of ticker symbols in the last {interval} minutes: {total_mentions}")
        time.sleep(interval * 60)

twitter_accounts= [
    "https://twitter.com/Mr_Derivatives", 
    "https://twitter.com/warrior_0719",
    "https://twitter.com/ChartingProdigy",
    "https://twitter.com/allstarcharts",
    "https://twitter.com/yuriymatso",
    "https://twitter.com/TriggerTrades",
    "https://twitter.com/AdamMancini4",
    "https://twitter.com/CordovaTrades", 
    "https://twitter.com/Barchart",
 ]
    


interval=30
if __name__=="__main__":
    main(twitter_accounts,interval)
