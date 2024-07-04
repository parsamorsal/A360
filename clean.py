from lxml import html
import csv

def clean_html_content(html_content):
    tree = html.fromstring(html_content)
    text_content = tree.xpath('string(.)')

    return text_content


def clean_csv(input_csv, output_csv):
    with open(input_csv, 'r', newline='', encoding='utf-8') as input_file:
        dict_reader = csv.DictReader(input_file)
        rows = list(dict_reader)

    for row in rows:
        row['encoded'] = clean_html_content(row['encoded'])
        row['description'] = clean_html_content(row['description'])

    with open(output_csv, 'w', newline='', encoding='utf-8') as output_file:
        fieldnames = dict_reader.fieldnames
        dict_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        dict_writer.writeheader()
        dict_writer.writerows(rows)


input_csv = 'output.csv' 
output_csv = 'cleaned_output.csv' 
clean_csv(input_csv, output_csv)
