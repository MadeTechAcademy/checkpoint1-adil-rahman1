import os

duties = [
    "Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage.",
    "Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members.",
    "Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review.",
    "Duty 4 Work as part of an agile team, and explore new ways of working, rapidly responding to changing user needs and with a relentless focus on the user experience. Understand the importance of continual improvement within a blameless culture.",
    "Duty 5 Build and operate a Continuous Integration (CI) capability, employing version control of source code and related artefacts.",
    "Duty 6 Implement and improve release automation & orchestration, often using Application Programming Interfaces (API), as part of a continuous delivery and continuous deployment pipeline, ensuring that team(s) are able to deploy new code rapidly and safely.",
    "Duty 7 Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers).",
    "Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance.",
    "Duty 9 Apply leading security practices throughout the Software Development Lifecycle (SDLC).",
    "Duty 10 Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable.",
    "Duty 11 Keep up with cutting edge by committing to continual training and development - utilise web resources for self-learning; horizon scanning; active membership of professional bodies such as Meetup Groups; subscribe to relevant publications.",
    "Duty 12 Look to automate any manual tasks that are repeated, often using APIs.",
    "Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience."
]

all_themes = {
    "Bootcamp": [1,2,3,4,13],
    "Automate!": [5,7,10],
    'Houston, Prepare to Launch': [6,7,10,12],
    "Going Deeper": [11],
    "Assemble!": [8],
    "Call Security": [9]
}

def display_duties_in_terminal():
    for duty in duties:
        print("{0}\n".format(duty))
    
def save_duties_to_html():
    f = open("duties.html", "w")
    
    f.write("<!DOCTYPE html>\n <html lang=\"en\">\n <head>\n    <title>DevOps Apprenticeship</title>\n </head>\n <body>\n    <h1>Level 4 DevOps Engineer Apprenticeship</h1>\n    <h2>Duties</h2>\n        <ul>\n")
    
    for duty in duties:
        f.write(f"            <li>{duty}</li>\n")
    
    f.write(f"        </ul>\n")
    f.write("</body>\n</html>")
    f.close()

def delete_html_duties_file():
    if os.path.exists("duties.html"):
        os.remove("duties.html")
    else:
        print("The file does not exist")

def save_themes_to_html(theme):
    f = open("themes.html", "w")
    f.write(f"<!DOCTYPE html>\n <html lang=\"en\">\n <head>\n    <title>DevOps Apprenticeship</title>\n </head>\n <body>\n    <h1>Level 4 DevOps Engineer Apprenticeship</h1>\n    <h2>{theme}</h2>\n        <ul>\n")

    for duty_no in all_themes[theme]:
        f.write(f"            <li>{duties[duty_no - 1]}</li>\n")

    f.write(f"        </ul>\n")
    f.write("</body>\n</html>")
    f.close()

if __name__== "__main__":
    x = input("""
    Welcome to apprentice themes!\n
    Press (1) to list all the duties on the terminal\n
    Press (2) to list all the duties in HTML\n
    Press (3) to delete the HTML file of all duties\n
    To see a theme and it's associated duties, press\n
        (4) to choose 'Bootcamp'\n
        (5) to choose 'Automate!'\n
        (6) to choose 'Houston, Prepare to Launch'\n
        (7) to choose 'Going Deeper'\n
        (8) to choose 'Assemble!'\n
        (9) to choose 'Call Security'\n
    Enter your choice: 
    """)
    if x == '1':
        display_duties_in_terminal()
    elif x == '2':
        save_duties_to_html()
    elif x == '3':
        delete_html_duties_file()
    elif x == '4':
        save_themes_to_html('Bootcamp')
    elif x == '5':
        save_themes_to_html('Automate!')
    elif x == '6':
        save_themes_to_html('Houston, Prepare to Launch')
    elif x == '7':
        save_themes_to_html('Going Deeper')
    elif x == '8':
        save_themes_to_html('Assesmble!')
    elif x == '9':
        save_themes_to_html('Call Security')