import xml.etree.ElementTree as ET
import csv

def parse_xml_to_dict(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    items = []

    for item in root.findall('.//item'):
        item_data = {}
        for child in item:
            if child.text:
                text_content = child.text.strip()
            else:
                text_content = ''
            tag_name = child.tag.split('}')[-1]
            item_data[tag_name] = text_content

            for attr, value in child.attrib.items():
                item_data[f'{tag_name}_{attr}'] = value

        items.append(item_data)

    return items

def write_to_csv(items, csv_file):
    if not items:
        return

    keys = set()
    for item in items:
        keys.update(item.keys())
    keys = sorted(keys)  

    with open(csv_file, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(items)

def xml_to_csv(xml_file, csv_file):
    items = parse_xml_to_dict(xml_file)
    write_to_csv(items, csv_file)


xml_file = 'datatonic-posts.rss'  
csv_file = 'output.csv'  
xml_to_csv(xml_file, csv_file)
