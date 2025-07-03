from themes import duties_list
import re

def test_13_duties_exist():
    assert len(duties_list) == 13

def test_13_list_items_display_in_html():
    no_of_list_items = 0

    with open('duties.html', 'r') as html_file:
        lines_in_html_file = html_file.readlines()
    
    for line in lines_in_html_file:
        if re.search("<li>.*</li>", line):
            no_of_list_items += 1

    assert no_of_list_items == 13

def test_each_duty_exists_in_html():
    with open('duties.html', 'r') as html_file:
        file_content = html_file.read()
    
    matches = re.findall("<li>.*</li>", file_content) 
    assert len(matches) == 13

    for duty in duties_list:
        assert f"<li>{duty}</li>" in matches
    