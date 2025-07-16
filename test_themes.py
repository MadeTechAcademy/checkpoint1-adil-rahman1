from themes import duties
import re

def test_13_duties_exist():
    assert len(duties) == 13

def test_13_list_items_display_in_html():
    with open('duties.html', 'r') as html_file:
        file_content = html_file.read()
    
    matches = re.findall("<li>.*</li>", file_content) 
    assert len(matches) == 13

def test_each_duty_exists_in_html():
    with open('duties.html', 'r') as html_file:
        file_content = html_file.read()
    
    matches = re.findall("<li>.*</li>", file_content) 

    for duty in duties:
        assert f"<li>{duty}</li>" in matches
    