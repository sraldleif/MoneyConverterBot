import praw
import time
import requests
from bs4 import BeautifulSoup
 
r = praw.Reddit(user_agent = "Currency converter by Thorium")
r.login()
 
 
cache = []
rates = []
aud_list = []
cad_list = []
gbp_list = []
eur_list = []
 
gbp_sym = u'\u00A3'
eur_sym = u'\u20AC'
 
def run_bot():
        subreddit = r.get_subreddit("bottestingenvironment")
        comments = subreddit.get_comments(limit=25)
        for comment in comments:
                comment_text = comment.body
                money = []
                #Set 'money' to word starting with '$'
                money = [i[1:] for i in comment_text.split() if i.startswith('$')]
                money_float = float(money[0])
                money_string = str(money[0])
                if comment.id not in cache and money:
                        cache.append(comment.id)
                       
                        #------------------------------------------------------------------------------------------------------------------------------
                        #AUD Exchange Rate
                        aud_url = "http://www.xe.com/currencyconverter/convert/?From=USD&To=AUD"
                        aud_req = requests.get(aud_url)
                        aud_soup = BeautifulSoup(aud_req.content)
                        aud_raw = aud_soup.find_all("td", {"class": "rightCol"})
                        for item in aud_raw:
                                aud_item_contents = item.text
                                aud_list.append(aud_item_contents)
                        rates.append(aud_list[0])
                        #Gets exact conversion (as a number) from the text stored in aud_raw_rate
                        aud_raw_rate = rates[0]
                        aud_full_rate = aud_raw_rate[:6]
                        #Changes conversion rate to a float.
                        new_aud_full_rate = float(aud_full_rate)
                        # Gets final converted amount
                        aud_converted_value = (money_float * new_aud_full_rate)
                        aud_final_string = str(aud_converted_value)
                        #------------------------------------------------------------------------------------------------------------------------------
                        #CAD Exchange Rate
                        cad_url = "http://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=CAD"
                        cad_req = requests.get(cad_url)
                        cad_soup = BeautifulSoup(cad_req.content)
                        cad_raw = cad_soup.find_all("td", {"class": "rightCol"})
                        for item in cad_raw:
                                cad_item_contents = item.text
                                cad_list.append(cad_item_contents)
                        rates.append(cad_list[0])
                        #Gets exact conversion (as a number) from the text stored in cad_raw_rate
                        cad_raw_rate = rates[1]
                        cad_full_rate = cad_raw_rate[:6]
                        #Changes conversion rate to a float.
                        new_cad_full_rate = float(cad_full_rate)
                        # Gets final converted amount
                        cad_converted_value = (money_float * new_cad_full_rate)
                        cad_final_string = str(cad_converted_value)
                        #------------------------------------------------------------------------------------------------------------------------------
                        #GBP Exchange Rate
                        gbp_url = "http://www.xe.com/currencyconverter/convert/?From=USD&To=GBP"
                        gbp_req = requests.get(gbp_url)
                        gbp_soup = BeautifulSoup(gbp_req.content)
                        gbp_raw = gbp_soup.find_all("td", {"class": "rightCol"})
                        for item in gbp_raw:
                                gbp_item_contents = item.text
                                gbp_list.append(gbp_item_contents)
                        rates.append(gbp_list[0])
                        #Gets exact conversion (as a number) from the text stored in gbp_raw_rate
                        gbp_raw_rate = rates[2]
                        gbp_full_rate = gbp_raw_rate[:6]
                        #Changes conversion rate to a float.
                        new_gbp_full_rate = float(gbp_full_rate)
                        # Gets final converted amount
                        gbp_converted_value = (money_float * new_gbp_full_rate)
                        gbp_final_string = str(gbp_converted_value)
                        #------------------------------------------------------------------------------------------------------------------------------
                        #EUR Exchange Rate
                        eur_url = "http://www.xe.com/currencyconverter/convert/?From=USD&To=EUR"
                        eur_req = requests.get(eur_url)
                        eur_soup = BeautifulSoup(eur_req.content)
                        eur_raw = eur_soup.find_all("td", {"class": "rightCol"})
                        for item in eur_raw:
                                eur_item_contents = item.text
                                eur_list.append(eur_item_contents)
                        rates.append(eur_list[0])
                        #Gets exact conversion (as a number) from the text stored in eur_raw_rate
                        eur_raw_rate = rates[3]
                        eur_full_rate = eur_raw_rate[:6]
                        #Changes conversion rate to a float.
                        new_eur_full_rate = float(eur_full_rate)
                        # Gets final converted amount
                        eur_converted_value = (money_float * new_eur_full_rate)
                        eur_final_string = str(eur_converted_value)
                        #------------------------------------------------------------------------------------------------------------------------------
                       
                        final_reply = "**$%s USD Converts to:**\n\n***\n\nCurrency|Converted\n:--|:--\nAUD|$%s\nCAD|$%s\nGBP|%s%s\nEUR|%s%s\n\n***\n^^I ^^am ^^a ^^bot!  ^^You ^^can ^^see ^^how ^^I ^^work ^^[here](http://www.github.com/sraldleif/MoneyConverterBot)." % (money_string, aud_final_string, cad_final_string, gbp_sym, gbp_final_string, eur_sym, eur_final_string)
                        comment.reply(final_reply)
                               
while True:
        run_bot()
        time.sleep(10)
