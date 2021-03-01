# Content classes
from Task6_1_module import Tip, News, PrivateAd
# Paragraph normalization
from Task6_2_module import Paragraph
import json


class Newspaper:
    def __init__(self):
        self.content = []

    def parse_newspaper(self, input_filename='.\\input\\input.txt'):

        # Read source newspaper
        input_file = open(input_filename, "r")
        input_text = input_file.read()
        input_file.close()

        # Split content to paragraphs
        paragraphs = input_text.split("\n")

        # Parse content
        str_num = 0
        while str_num < len(paragraphs):
            current_str = paragraphs[str_num]
            if current_str[:5] == 'Type:':
                if current_str[6:] == 'Tip of the day':
                    body = paragraphs[str_num + 1]
                    body = Paragraph(body[6:]).normalized
                    self.content.append(Tip(body))
                    str_num += 2
                elif current_str[6:] == 'News':
                    body = paragraphs[str_num + 1]
                    body = Paragraph(body[6:]).normalized
                    city = paragraphs[str_num + 2]
                    self.content.append(News(body, city[6:]))
                    str_num += 4
                elif current_str[6:] == 'Private Ad':
                    body = paragraphs[str_num + 1]
                    body = Paragraph(body[6:]).normalized
                    expiration_time = paragraphs[str_num + 2]
                    self.content.append(PrivateAd(body, expiration_time[17:]))
                    str_num += 4
                else:
                    print("Format error: Unknown or missing content type")
            str_num += 1

    def publish_newspaper(self, output_filename='output.txt'):
        # Publish content
        file = open(output_filename, "x")
        file.write("NEWS FEED:\n\n")

        for cur_content in self.content:
            cur_content.publish(file)
        file.close()

    def read_content(self, input_filename='.\\input\\input.json'):
        self.content = []
        # Read source content
        _file = open(input_filename, "r")
        input_text = _file.read()
        json_content = json.loads(input_text)
        for _record in json_content:
            if _record['Type'] == 'News':
                self.content.append(News(_record['Body'], _record['City']))
            elif _record['Type'] == 'Tip of the day':
                self.content.append(Tip(_record['Body']))
            elif _record['Type'] == 'Private Ad':
                self.content.append(PrivateAd(_record['Body'], _record['Expiration date']))
        _file.close()

    def save_content(self, output_filename='output.json'):
        # Save content in JSON format
        _file = open(output_filename, "x")

        # Collect JSONs to the list
        _records = []
        for _record in self.content:
            _records.append(_record.record)

        # Save JSONs to file
        _file.write(json.dumps(_records))
        _file.close()
