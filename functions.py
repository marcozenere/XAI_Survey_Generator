import nbformat as nbf
import ipywidgets as widgets
import os

def question1RadioButtons():

    return widgets.RadioButtons(
        options=[('Qualitative Evaluation', '1'), ('Quantitative Evaluation', '2')],
        value=None,
        disabled=False
        )

def question2RadioButtons():
    return widgets.RadioButtons(
        options=[('Verification Task', '1'), ('Forced Choice', '2'), ('Forward Simulation', '3'), ('Counterfactual Simulation Task', '4')],
        value=None,
        disabled=False
        )

def question3RadioButtons():
    return widgets.RadioButtons(
        options=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),('5','5')],
        value=None,
        disabled=False
    )

    
def verificationTaskTemplate(evaluation_type): 
    code = """"""
    
    if evaluation_type == '1':
        code += """\
def questionWebPage():
    output.clear_output()
    with output:
        question_number = questions_numbers.pop(0)
        display(widgets.HTML(value = '''<h2>Question %s</h2>'''%(str(question_number + 1))))
        
        # Question Details
        # The verification task methodology requires an input, output, and explanation. 
        # The goal is to ask the user its satisfaction with the given explanation with respect to the input and output.
        
        # Input
        display(widgets.HTML(value='''<p>Input of the sample</p>'''))
        
        # Output
        display(widgets.HTML(value='''<p>Output with respect to the sample</p>'''))
        
        # Explanation
        display(widgets.HTML(value = '''<p>Explanation of the output</p>'''))
        
        display(widgets.HTML(value = '''<h3>How much are you satisfied with the explanation?</h3>'''))
        display(questions_selection[question_number])
        display(next_button)
    
    # Datetime question displayed to the participant
    questions_datetime.append(datetime.now())"""
    else:
        code += """\
def questionWebPage():
    output.clear_output()
    with output:
        question_number = questions_numbers.pop(0)
        display(widgets.HTML(value = '''<h2>Question %s</h2>'''%(str(question_number + 1))))
        
        # Question Details
        # The verification task methodology requires an input, output, and explanation. 
        # The goal is to ask the user its satisfaction with the given explanation with respect to the input and output.
        
        # Input
        display(widgets.HTML(value='''<p>Input of the sample</p>'''))
        
        # Output
        display(widgets.HTML(value='''<p>Output with respect to the sample</p>'''))
        
        # Explanation
        display(widgets.HTML(value = '''<p>Explanation of the output</p>'''))
        # 5 points-Likert Scale satisfaction
        display(widgets.HTML(value = '''<h3>How much are you satisfied with the explanation? (1 = not satisfied at all, 5 = definitely satisfied)</h3>'''))
        display(questions_selection[question_number])
        display(next_button)
    
    # Datetime question displayed to the participant
    questions_datetime.append(datetime.now())"""

    return code

def forcedChoiceTemplate():
    code = """\
def questionWebPage():
    output.clear_output()
    with output:
        question_number = questions_numbers.pop(0)
        display(widgets.HTML(value = '''<h2>Question %s</h2>'''%(str(question_number + 1))))
        
        # Question Details
        # The forced choice methodology requires an input, output, and several explanations. 
        # The goal is to ask the user to choose among the explanations provided the one it preferers with respect to the input and output.
        
        # Input
        display(widgets.HTML(value='''<p>Input of the sample</p>'''))
        
        # Output
        display(widgets.HTML(value='''<p>Output with respect to the sample</p>'''))
        
        # Explanations
        display(widgets.HTML(value = '''<p>First explanation of the output</p>'''))
        display(widgets.HTML(value = '''<p>Second explanation of the output</p>'''))
        display(widgets.HTML(value = '''<p>Third Explanation of the output</p>'''))
        
        display(widgets.HTML(value = '''<h3>Which of the following explanations do you prefer the most?</h3>'''))
        display(questions_selection[question_number])
        display(next_button)
    
    # Datetime question displayed to the participant
    questions_datetime.append(datetime.now())"""
    
    return code

def forwardSimulationTemplate():
    code = """\
def questionWebPage():
    output.clear_output()
    with output:
        question_number = questions_numbers.pop(0)
        display(widgets.HTML(value = '''<h2>Question %s</h2>'''%(str(question_number + 1))))
        
        # Question Details
        # The forward simulation methodology requires an input and an explanation. 
        # The goal is to ask the user to predict the system's output given the input and the explanation of the system's output.
        
        # Input
        display(widgets.HTML(value='''<p>Input of the sample</p>'''))
        
        # Explanation
        display(widgets.HTML(value = '''<p>Explanation of the system's output</p>'''))
        
        display(widgets.HTML(value = '''<h3>Which is the output of the system given the input and the explanation?</h3>'''))
        display(questions_selection[question_number])
        display(next_button)
    
    # Datetime question displayed to the participant
    questions_datetime.append(datetime.now())"""

    return code

def counterfactualSimulationTask():
    code = """\
def questionWebPage():
    output.clear_output()
    with output:
        question_number = questions_numbers.pop(0)
        display(widgets.HTML(value = '''<h2>Question %s</h2>'''%(str(question_number + 1))))
        
        # Question Details
        # The counterfactual simulation task methodology requires two samples and the following information of the two: the input, output, and explanation of the first sample and the output of the second one. 
        # The goal is to ask the user the input changes to get the output of the sample 2.
        
        # Input sample 1
        display(widgets.HTML(value='''<p>Input of the sample 1</p>'''))
        
        # Output sample 1
        display(widgets.HTML(value='''<p>Output with respect to the sample 1</p>'''))
        
        
        # Explanation sample 1
        display(widgets.HTML(value = '''<p>Explanation of the system's output 1</p>'''))
        
        # Output sample 2
        display(widgets.HTML(value = '''<p>Considering the output with respect to the sample 2</p>'''))
        
        display(widgets.HTML(value = '''<h3>How the input should change to get the output of the sample 2?</h3>'''))
        display(questions_selection[question_number])
        display(next_button)
    
    # Datetime question displayed to the participant
    questions_datetime.append(datetime.now())"""

    return code

def templateDownloader():
    from google.colab import files
    !zip -r ./XAI_Questionnaire.zip XAI_Questionnaire
    files.download('XAI_Questionnaire.zip')

def templateGenerator(evaluation_type, methodology, questions_number):
    nb = nbf.v4.new_notebook()
    
    code_0 = '''\
import pandas as pd
import numpy as np
import ipywidgets as widgets
from datetime import datetime'''
    
    code_1 = """\
# Dataset Load"""
    
    code_2 = """\
# Definition of the buttons in the questionnaire

next_button = widgets.Button(
    description='Next'
)

submit_button = widgets.Button(
    description='Submit'
)

output = widgets.Output()"""
    
    code_3 = """\
%%capture
# Suggested widgets
# Futher information at https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html
'''
# 5 points Likert Scale 
widgets.SelectionSlider(
            options=[' 1', '2', '3', '4', '5'],
            value='3',
            disabled=False,
            continuous_update=False,
            orientation='horizontal',
            readout=True
        )

# Dropdown
widgets.Dropdown(
    options=[('Selection', '*'),('Label 1', '1'), ('Label 2', '2'), ('Label 3', '3')],
    value= '*',
)

# Radio Buttons
widgets.RadioButtons(
        options=[('Label 1', '1'), ('Label 2', '2'), ('Label 3', '3')],
        value=None,
        disabled=False
    )

# Text Area
widgets.Textarea(
        value='',
        disabled=False
    )

# Image Loader
file = open("images/Example.png", "rb")
image = file.read()
widgets.Image(
    value=image,
    format='png',
    width=300,
    height=400,
)
'''"""

    code_4 = """\
# Comprehension Test Section elements definition (radio buttons, dropdowns, etc)
# Example
comprehension_selection_example = widgets.RadioButtons(
                                options=[('Label 1', '1'), ('Label 2', '2'), ('Label 3', '3')],
                                value=None,
                                disabled=False
                      )"""
    
    code_5 = """\
N = %s # Number of questions
questions_numbers = [n for n in range(N)] # Track the question section in which the user is in
questions_datetime = [] # Track the time required to complete each of the question section"""%questions_number

    code_6 = """"""

    if evaluation_type == '1':
        code_6 += """\
# Preparation of the Questions section of the survey

questions_selection = []
for x in range(N):
    questions_selection.append(widgets.Textarea(
        value='',
        disabled=False
    ))
    # Additional widgets can be added below, considering the suggested widgets above
    
# Select the samples you want to use in your evaluation
# TO DO"""
    elif evaluation_type == '2' and methodology == '1':
        code_6 += """\
# Preparation of the Questions section of the survey

questions_selection = []
for x in range(N):
    questions_selection.append(widgets.SelectionSlider(
            options=[' 1', '2', '3', '4', '5'],
            value='3',
            disabled=False,
            continuous_update=False,
            orientation='horizontal',
            readout=True
        ))
    # Additional widgets can be added below, considering the suggested widgets above
# Select the samples you want to use in your evaluation
# TO DO"""
    else:
        code_6 += """\
questions_selection = []
for x in range(N):
    questions_selection.append(widgets.RadioButtons(
        options=[('Label 1', '1'), ('Label 2', '2'), ('Label 3', '3')],
        value=None,
        disabled=False
    ))
    # Additional widgets can be added below, considering the suggested widgets above
# Select the samples you want to use in your evaluation
# TO DO"""
    
    code_7 = """\
# Preparation of the Participant information section

gender_selection = widgets.RadioButtons(
    options=[('Male', '1'), ('Female', '2'), ('Other', '3'), ('Prefer not to say', '4')],
    value=None,
    disabled=False
)

age_selection = widgets.RadioButtons(
    options=[('18-20', '1'), ('21-29', '2'), ('30-39', '3'),('40-49', '4'),('50-59', '5'),('60 or older', '6')],
    value=None,
    disabled=False
)

education_selection = widgets.RadioButtons(
    options=[('Less than high school degree', '1'), ('High school degree or equivalent', '2'), ('Undergraduate', '3'),('Graduate', '4')],
    value=None,
    disabled=False
)

english_level_selection = widgets.RadioButtons(
    options=[('Beginner (A1)', '1'), ('Elementary (A2)', '2'), ('Lower Intermidiate (B1)', '3'), ('Upper Intermidiate (B2)', '4'), ('Advanced (C1)', '5'), ('Proficient (C2)', '6')],
    value=None,
    disabled=False
)"""
    
    code_8 = """\
def welcomeWebPage():
    output.clear_output()
    with output:
        display(widgets.HTML(value = '''<h1>Questionnaire Title</h1>'''))
        display(widgets.HTML(value = '''<p>Description of the Questionnaire</p>'''))
        display(widgets.HTML(value = '''<p>By clicking the next button, you partecipate to the questionnaire and confirm that:<br>
        <ul>
            <li> You have reached the age of majority </li>
            <li> You acknowledge that your participation is completely voluntary </li>
            <li> You acknowledge that your anonymous responses may be used for research purposes in accordance with General Data Protection Regulation </li>
        </ul>
        </p>'''))
        display(next_button)
    display(output)"""
    
    code_9 = """\
def introductionWebPage():
    
    output.clear_output()
    with output:
        display(widgets.HTML(value = '''<h2>Introduction</h2>'''))
        display(widgets.HTML(value = '''<p>Description of the domain of interest</p>'''))
        display(widgets.HTML(value = '''<h3>XAI Explanation Section</h3>'''))
        display(widgets.HTML(value = '''<p>Description of the XAI explanation</p>'''))
        display(next_button)"""
    
    code_10 = """\
def exampleWebPage():
    output.clear_output()
    with output:
        display(widgets.HTML(value = '''<h2>Example</h2>'''))
        # Provide an example in order to improve the user's understanding of the XAI explanation
        display(next_button)"""
    
    code_11 = """\
def comprehensionTestWebPage():
    output.clear_output()
    with output:
        display(widgets.HTML(value = '''<h2>Comprehension Test</h2>'''))
        # Test the user's mental model by asking some questions regarding the XAI explanation/domain of interest
        display(comprehension_selection_example)
        display(next_button)"""
    
    code_12 = """\
def questionnaireInstructionWebPage():
    output.clear_output()
    with output:
        display(widgets.HTML(value = '''<h2>Survey Instruction</h2>'''))
        display(widgets.HTML(value = '''<p>Provide details on how the survey will be conducted</p>'''))
        display(next_button)"""
    
    code_13 = """"""
    
    if methodology == '1':
        code_13 += verificationTaskTemplate(evaluation_type)
    elif methodology == '2':
        code_13 += forcedChoiceTemplate()
    elif methodology == '3':
        code_13 += forwardSimulationTemplate()
    else:
        code_13 += counterfactualSimulationTask()
    
    code_14 = """\
def participatInfoWebPage():
    output.clear_output()
    with output:
        display(widgets.HTML(value = '''<h2>Information about the survey participant</h2>'''))
        display(widgets.HTML(value = '''<p>We would like to collect some information about you to do a demographic analysis of the participants in our questionnaire.</p>'''))
        display(widgets.HTML(value = '''<h3>Gender</h3>'''))
        display(gender_selection)
        display(widgets.HTML(value = '''<h3>Age</h3>'''))
        display(age_selection)
        display(widgets.HTML(value = '''<h3>Education</h3>'''))
        display(education_selection)
        display(widgets.HTML(value = '''<h3>English Level</h3>'''))
        display(english_level_selection)
        display(submit_button)
        display(widgets.HTML(value = '''<p>NB: The sending of the answers could take a few seconds.</p>'''))"""
    
    code_15 = """\
def endquestionnaireWebPage():
    output.clear_output()
    with output:
        display(widgets.HTML(value = '''<h2>The questionnaire is ended</h2>'''))
        display(widgets.HTML(value = '''<p>The questionnaire was submitted correctly and you can now close the browser tab. <br>
        Thank you very much for the partecipation.</p>'''))"""
    
    code_16 = """\
web_pages_order = [introductionWebPage, exampleWebPage, comprehensionTestWebPage, questionnaireInstructionWebPage, participatInfoWebPage, endquestionnaireWebPage]

index_element = web_pages_order.index(questionnaireInstructionWebPage)

for x in range(N):
    web_pages_order.insert(index_element + 1, questionWebPage)"""
    
    code_17 = """\
web_pages = ['welcomeWebPage', 'introductionWebPage', 'exampleWebPage', 'comprehensionTestWebPage', 'questionnaireInstructionWebPage', 'participatInfoWebPage', 'endquestionnaireWebPage']

index_element = web_pages.index('questionnaireInstructionWebPage')

for x in range(N):
    web_pages.insert(index_element + 1, 'questionWebPage')"""
    
    code_18 = """\
def next_clicked(b):
    current_web_page = web_pages[0]

    if current_web_page == 'comprehensionTestWebPage':
        # The Warm-Up section will have questions for measuring the user's mental mental
        # Check if the questions are answered before continuing with the questionnaire
        
        # Example considering the basic template elements/widgets
        if comprehension_selection_example.value == None:
            return
    elif current_web_page == 'questionWebPage':
        # Each question section will have some questions that the user must answers 
        # Before continuing with the next questions section, check if the user answers all of the questions in the current section
        
        # Example considering the basic template elements/widgets
        if (len(questions_numbers) != 0 and questions_selection[questions_numbers[0] - 1].value == None) or (len(questions_numbers) == 0 and questions_selection[N - 1].value == None):
            return
        
    web_pages.pop(0)
    web_page = web_pages_order.pop(0)
    web_page()

def submit_clicked(b):
    current_web_page = web_pages[0]
    
    if current_web_page == 'participatInfoWebPage':
        if gender_selection.value == None or age_selection.value == None or education_selection.value == None or english_level_selection.value == None:
            return
    
    # Store/Send the answers of the user
    # TO DO
    
    web_pages.pop(0)
    web_page = web_pages_order.pop(0)
    web_page()
    
next_button.on_click(next_clicked)
submit_button.on_click(submit_clicked)"""
    
    code_19 = """\
welcomeWebPage()"""
    
    # Directories Creation
    if not os.path.exists('./XAI_Questionnaire'):
        os.mkdir('./XAI_Questionnaire')
    
    # Readme and requirements files creations
    readme_text = '''# README

The following directory and files are generated by the ['XAI Survey Generator software'](https://github.com/marcozenere/XAI_Survey_Generator).

"Questionnaire_Template.ipynb" is a Jupyter notebook containing the questionnaire code with all the details for completing it with your information. 

An example of a questionnaire created using the 'Questionnaire_Template.ipynb' Jupyter notebook can be found [here](https://github.com/marcozenere/XAI_Survey).

The Jupyter notebook has been created and structured to use the [Voilà](https://voila.readthedocs.io/en/stable/index.html) library and [Binder](https://mybinder.org) online service.

Voilà is a library for converting Jupyter notebooks into standalone web applications and dashboards. Binder is an online service for deploying Jupyter notebooks.

## How to Run the Jupyter Notebook in Binder

Instructions extracted from the [Voilà documentation](https://voila.readthedocs.io/en/stable/deploy.html):

- Create a **'requirements.txt'** file and lists all the libraries used in your questionnaire code. The **'requirements.txt'** file contains the libraries needed to run the application in Binder. A basic version of it is provided with the questionnaire template notebook.  If you use additional libraries than the basic ones in your notebook, they must be added to this file.
- Commit the lastest version of the questionnaire in your repository and make sure that the repository where your code is in is publicly available
- Go to [Binder](https://mybinder.org) and enter the URL of your repository
- In the **'Path to a notebook file'** section, click the dropdown menu with the default value **'File'** and select the **'URL'** option and insert the Voilà endopoint voila/render/path/to/notebook.ipynb
- Click the **'Launch'** button. 
  
**NB: The service could take a few minutes to launch the application if it is the first launch.**

## Required Libraries to Run the Questionnaire Template

- pandas
- numpy
- ipywidgets
- datetime
'''

    requirements_text = ['pandas\n', 'numpy\n', 'ipywidgets\n', 'voila\n']

    # Notebook cells
    nb['cells'] = [
               nbf.v4.new_code_cell(code_0),
               nbf.v4.new_code_cell(code_1),
               nbf.v4.new_code_cell(code_2),
               nbf.v4.new_code_cell(code_3),
               nbf.v4.new_code_cell(code_4),
               nbf.v4.new_code_cell(code_5),
               nbf.v4.new_code_cell(code_6),
               nbf.v4.new_code_cell(code_7),
               nbf.v4.new_code_cell(code_8),
               nbf.v4.new_code_cell(code_9),
               nbf.v4.new_code_cell(code_10),
               nbf.v4.new_code_cell(code_11),
               nbf.v4.new_code_cell(code_12),
               nbf.v4.new_code_cell(code_13),
               nbf.v4.new_code_cell(code_14),
               nbf.v4.new_code_cell(code_15),
               nbf.v4.new_code_cell(code_16),
               nbf.v4.new_code_cell(code_17),
               nbf.v4.new_code_cell(code_18),
               nbf.v4.new_code_cell(code_19)
    ]
    
    nbf.write(nb,'./XAI_Questionnaire/Questionnaire_Template.ipynb')
    
    with open('./XAI_Questionnaire/README.md', 'w') as readme:
        readme.write(readme_text)
    
    with open('./XAI_Questionnaire/requirements.txt', 'w') as requirements:
        requirements.writelines(requirements_text)
    
    if 'google.colab' in str(get_ipython()):
        templateDownloader()