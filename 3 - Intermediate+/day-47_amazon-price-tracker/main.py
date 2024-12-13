import amazon_scrapper
import email_manager

scrapper = amazon_scrapper.Amazon_Scrapper()
email_manager = email_manager.Email_Manager()

item_price = scrapper.getPrice()
item_name = scrapper.getItemName()
item_link = scrapper.getItemLink()

target_price = 200

if item_price < target_price:
    print(f"{item_name}, {item_price}, {item_link}")
    email_manager.send_email(item_name, item_price, item_link)




