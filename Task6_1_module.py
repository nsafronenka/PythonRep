from datetime import datetime

class Content:                          # Create a class Content
    def __init__(self):                 # Creation of a constructor of the class Content
        self.record = {}                # Dictionary of peace of content

    def publish(self, file):            # Creation of publish method
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

    def publish(self, file):                                            # Publish method redefinition
        for _key in self.record.keys():
            file.write(_key + ":\t" + str(self.record[_key]) + "\n")    # Put parameter to file
        file.write("Days to expire:\t" + self.time_to_expire() + "\n")  # Put days to expire to file
        file.write("\n")


class Tip(Content):                                                     # Creation of the new inherited class Tip from Content
    def __init__(self, tip):                                            # Creation of a constructor with attribute
        self.record = {"Type": "Tip of the day", "Body": tip}           # Put values to dictionary

