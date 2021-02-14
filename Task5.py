from datetime import datetime

class Content:                          # Create a class Content
    def __init__(self):                 # Creation of a constructor of the class Content
        self.record = {}                # Dictionary of peace of content

    def publish(self):                  # Creation of publish method
        for _key in self.record.keys():
            file.write(_key + ":\t" + self.record[_key] + "\n")     # Put parameter to file
        file.write("\n")


class News(Content):                                # Creation of the new inherited class News from Content
    def __init__(self, news, news_city):            # Creation of a constructor with attributes
        self.pub_time = datetime.now()              # Get current time
        self.record = {"Type": "News", "Body": news, "City": news_city, "Publish time": self.pub_time.strftime("%d/%m/%Y %H.%M")}   # Put values to dictionary


class PrivateAd(Content):                           # Creation of the new inherited class PrivateAd from Content
    def __init__(self, ads, expiration_date):       # Creation of a constructor with attributes
        self.record = {"Type": "Private Ad", "Body": ads, "Expiration date": expiration_date}       # Put values to dictionary

    def time_to_expire(self):                       # Method to define expiration date for private ads
        self.exp_date = datetime.strptime(self.record["Expiration date"], "%d/%m/%Y")   # Get expiration date, strptime function converts string to datetime format with the mask date/month/year
        return str((self.exp_date - datetime.now()).days)                               # The method returns the number of days to expire of the private ad

    def publish(self):                                                  # Publish method redefinition
        for _key in self.record.keys():
            file.write(_key + ":\t" + str(self.record[_key]) + "\n")    # Put parameter to file
        file.write("Days to expire:\t" + self.time_to_expire() + "\n")  # Put days to expire to file
        file.write("\n")


class Tip(Content):                                                     # Creation of the new inherited class Tip from Content
    def __init__(self, tip):                                            # Creation of a constructor with attribute
        self.record = {"Type": "Tip of the day", "Body": tip}           # Put values to dictionary


# Define filename
timestamp = datetime.now()                                      # Get current time
filename = timestamp.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"     # Define file name, strftime() method converts datetime to string
file = open(filename, "x")                                      # Create new file
file.write("NEWS FEED:\n\n")                                    # Put header to file

# Make input until the mode is set to zero
mode = -1

while mode != 0:
    # Define what to do. In the section below lists the user's options, he/she selects the desired mode - 0,1,2,3.
    # Based of the selected value she/he should provide the information.
    mode = int(input("Select content type:\n1 - news\n2 - ads\n3 - tip of the day\n0 - exit"))

    if mode == 0:
        continue
    elif mode == 1:
        text = input("News text:\t")
        city = input("City:\t")
        record = News(text, city)               # Create new peace of news
        record.publish()
    elif mode == 2:
        text = input("Ads text:\t")
        exp_date = input("Expiration date DD/MM/YYYY:\t")
        record = PrivateAd(text, exp_date)      # Create new peace of private ad
        record.publish()
    elif mode == 3:
        text = input("Tip text:\t")
        record = Tip(text)                      # Create new peace of tip
        record.publish()
    else:
        input("Options are limited to 0-3 range.\nPress enter to continue...")

file.close()
