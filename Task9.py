# Content classes
from Task6_1_module import Tip, News, PrivateAd
from Task8_1 import Newspaper
from datetime import datetime
import os


newspaper = Newspaper()
# Define what to do. In the section below lists the user's options, he/she selects the desired mode - 0,1,2,3.
# Based of the selected value she/he should provide the information.
input_format = -1
while input_format != 0:
    input_format = int(input("What is your input mode?\n0 - exit,\n1 - manual,\n2 - TXT,\n3 - JSON\n4 - XML\n"))
    if input_format == 0:
        break
    elif input_format == 1:
        # Make input until the mode is set to zero
        mode = -1

        while mode != 0:
            mode = int(input("Select content type:\n1 - news\n2 - ads\n3 - tip of the day\n0 - exit\n"))

            if mode == 0:
                continue
            elif mode == -1:
                # Define filename
                timestamp = datetime.now()
                filename = timestamp.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
            elif mode == 1:
                text = input("News text:\t")
                city = input("City:\t")
                newspaper.content.append(News(text, city))
            elif mode == 2:
                text = input("Ads text:\t")
                exp_date = input("Expiration date DD/MM/YYYY:\t")
                newspaper.content.append(PrivateAd(text, exp_date))  # Create new peace of private ad
            elif mode == 3:
                text = input("Tip text:\t")
                newspaper.content.append(Tip(text))  # Create new peace of tip
            else:
                input("Options are limited to 0-3 range.\nPress enter to continue...")
        break
    elif input_format == 2:
        input_filename = input("Enter input filename or press Enter to use .\input\input.txt:")
        if input_filename == "":
            newspaper.parse_newspaper()
        else:
            newspaper.parse_newspaper(input_filename)
        break
    elif input_format == 3:
        input_filename = input("Enter input filename or press Enter to use .\input\input.json:")
        if input_filename == "":
            newspaper.read_content()
        else:
            newspaper.read_content(input_filename)
        break
    elif input_format == 4:
        input_filename = input("Enter input filename or press Enter to use .\input\input.xml:")
        if input_filename == "":
            newspaper.ReadXML()
        else:
            newspaper.ReadXML(input_filename)
        break
    else:
        print("You've selected a wrong option")

output_format = -1
while output_format != 0:
    output_format = int(input("What output format do you want?\n0 - exit,\n1 - newspaper (TXT),\n2 - JSON\n3 - XML\n"))
    if output_format == 0:
        break
    elif output_format == 1:
        output_filename = input("Enter output filename or press Enter to use .\output.txt:")
        if output_filename == "":
            newspaper.publish_newspaper()
        else:
            newspaper.publish_newspaper(output_filename)
        break
    elif output_format == 2:
        output_filename = input("Enter output filename or press Enter to use .\output.json:")
        if output_filename == "":
            newspaper.save_content()
        else:
            newspaper.save_content(output_filename)
        break
    elif output_format == 3:
        output_filename = input("Enter output filename or press Enter to use .\output.xml:")
        if output_filename == "":
            newspaper.PublishXML()
        else:
            newspaper.PublishXML(output_filename)
        break
    else:
        print("You've selected a wrong option")

# Commented for testing needs
# os.remove(input_filename)
