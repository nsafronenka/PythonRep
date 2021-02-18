from datetime import datetime
# Create a class Content
class Content:
    # Creation of a constructor of the class Content
    def __init__(self):
        # Dictionary of peace of content
        self.record = {}

    # Creation of publish method
    def publish(self, file):
        for _key in self.record.keys():
            # Put parameter to file
            file.write(_key + ":\t" + self.record[_key] + "\n")
        file.write("\n")


# Creation of the new inherited class News from Content
class News(Content):
    # Creation of a constructor with attributes
    def __init__(self, news, news_city):
        # Get current time
        self.pub_time = datetime.now()
        # Put values to dictionary
        self.record = {"Type": "News", "Body": news, "City": news_city, "Publish time": self.pub_time.strftime("%d/%m/%Y %H.%M")}


# Creation of the new inherited class PrivateAd from Content
class PrivateAd(Content):
    # Creation of a constructor with attributes
    def __init__(self, ads, expiration_date):
        # Put values to dictionary
        self.record = {"Type": "Private Ad", "Body": ads, "Expiration date": expiration_date}

    # Method to define expiration date for private ads
    def time_to_expire(self):
        # Get expiration date, strptime function converts string to datetime format with the mask date/month/year
        self.exp_date = datetime.strptime(self.record["Expiration date"], "%d/%m/%Y")
        # The method returns the number of days to expire of the private ad
        return str((self.exp_date - datetime.now()).days)

    # Publish method redefinition
    def publish(self, file):
        for _key in self.record.keys():
            # Put parameter to file
            file.write(_key + ":\t" + str(self.record[_key]) + "\n")
        # Put days to expire to file
        file.write("Days to expire:\t" + self.time_to_expire() + "\n")
        file.write("\n")


# Creation of the new inherited class Tip from Content
class Tip(Content):
    # Creation of a constructor with attribute
    def __init__(self, tip):
        # Put values to dictionary
        self.record = {"Type": "Tip of the day", "Body": tip}

