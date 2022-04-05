import nbformat as nbf
import ipywidgets as widgets

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

    
def verificationTaskTemplate(evaluation_type): 
    code = """"""
    
    if evaluation_type.value == '1':
        code += """\
def questionWebPage():
    output.clear_output()
    with output:
        question_number = questions_numbers.pop(0)
        display(widgets.HTML(value = '''<h2>Question %s</h2>'''%(str(question_number + 1))))
        
        # Question Details
        # The forced choice methodology requires an input, output, and explanation. 
        # The goal is to ask the user its satisfaction with the given explanation with respect to the input and output.
        
        # Input
        display(widgets.HTML(value='''<p>Input of the sample</p>'''))
        
        # Output
        display(widgets.HTML(value='''<p>Output with respect to the sample</p>'''))
        
        # Explanation
        display(widgets.HTML(value = '''<p>Explanation of the output</p>'''))
        
        display(widgets.HTML(value = '''<p>How much are you satisfied with the explanation?</p>'''))
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
        display(widgets.HTML(value = '''<p>How much are you satisfied with the explanation? (1 = not satisfied at all, 5 = definitely satisfied)</p>'''))
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
        
        display(widgets.HTML(value = '''<p>Which of the following explanations do you prefer the most?</p>'''))
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
        # The forward simulation methodology requires an input and an explanations. 
        # The goal is to ask the user to predict the system's output given the input and the explanation of the system's output.
        
        # Input
        display(widgets.HTML(value='''<p>Input of the sample</p>'''))
        
        # Explanation
        display(widgets.HTML(value = '''<p>Explanation of the system's output</p>'''))
        
        display(widgets.HTML(value = '''<p>Which is the output of the system given the input and the explanation?</p>'''))
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
        
        display(widgets.HTML(value = '''<p>How the input should change to get the output of the sample 2?</p>'''))
        display(questions_selection[question_number])
        display(next_button)
    
    # Datetime question displayed to the participant
    questions_datetime.append(datetime.now())"""

    return code

def templateGenerator(evaluation_type, methodology):
    nb = nbf.v4.new_notebook()
    
    code_0 = '''\
import pandas as pd
import numpy as np
import ipywidgets as widgets
from datetime import datetime'''
    
    code_1 = """\
# Definition of the buttons in the questionnaire

next_button = widgets.Button(
    description='Next'
)

submit_button = widgets.Button(
    description='Submit'
)

output = widgets.Output()"""

    code_2 = """\
# Warm-Up Section elements definition (radio buttons, dropdowns, etc)"""
    
    code_3 = """\
#define N, the number of questions in the questionnaire
N = 1
questions_numbers = [n for n in range(N)] 
questions_datetime = []
questions_representation = []"""

    code_4 = """"""

    if evaluation_type.value == '1':
        code_4 += """\
# Preparation of the Questions section of the survey

questions_selection = []
for x in range(N):
    questions_selection.append(widgets.Textarea(
        value='',
        disabled=False
    ))
# Select the samples you want to use in your evaluation"""
    elif evaluation_type.value == '2' and methodology.value == '1':
        code_4 += """\
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

# Select the samples you want to use in your evaluation"""
    else:
        code_4 += """\
questions_selection = []
for x in range(N):
    questions_selection.append(widgets.RadioButtons(
        options=[('Label 1', '1'), ('Label 2', '2'), ('Label 3', '3')],
        value=None,
        disabled=False
    ))
# Select the samples you want to use in your evaluation"""
    
    code_5 = """\
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
    
    code_6 = """\
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
    
    code_7 = """\
def introductionWebPage():
    
    output.clear_output()
    with output:
        display(widgets.HTML(value = '''<h2>Introduction</h2>'''))
        display(widgets.HTML(value = '''<p>Description of the domain of interest</p>'''))
        display(widgets.HTML(value = '''<h3>XAI Explanation Section</h3>'''))
        display(widgets.HTML(value = '''<p>Description of the XAI explanation</p>'''))
        display(next_button)"""
    
    code_8 = """\
def exampleWebPage():
    output.clear_output()
    with output:
        display(widgets.HTML(value = '''<h2>Example</h2>'''))
        # Provide an example in order to improve the user's understanding of the XAI explanation
        display(next_button)"""
    
    code_9 = """\
def warmUpWebPage():
    output.clear_output()
    with output:
        display(widgets.HTML(value = '''<h2>Warm-Up</h2>'''))
        # Test the user's mental model by asking some questions regarding the XAI explanation/domain of interest
        display(next_button)"""
    
    code_10 = """\
def questionnaireInstructionWebPage():
    output.clear_output()
    with output:
        display(widgets.HTML(value = '''<h2>Survey Instruction</h2>'''))
        display(widgets.HTML(value = '''<p>Provide details on how the survey will be conducted</p>'''))
        display(next_button)"""
    
    code_11 = """"""
    
    if methodology.value == '1':
        code_11 += verificationTaskTemplate(evaluation_type)
    elif methodology.value == '2':
        code_11 += forcedChoiceTemplate()
    elif methodology.value == '3':
        code_11 += forwardSimulationTemplate()
    else:
        code_11 += counterfactualSimulationTask()
    
    """\
def questionWebPage():
    output.clear_output()
    with output:
        question_number = questions_numbers.pop(0)
        display(widgets.HTML(value = '''<h2>Question %s</h2>'''%(str(question_number + 1))))
        # Question Details
        display(next_button)
    
    # Datetime question displayed to the participant
    questions_datetime.append(datetime.now())"""
    
    code_12 = """\
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
    
    code_13 = """\
def endquestionnaireWebPage():
    output.clear_output()
    with output:
        display(widgets.HTML(value = '''<h2>The questionnaire is ended</h2>'''))
        display(widgets.HTML(value = '''<p>The questionnaire was submitted correctly and you can now close the browser tab. <br>
        Thank you very much for the partecipation.</p>'''))"""
    
    code_14 = """\
web_pages_order = [introductionWebPage, exampleWebPage, warmUpWebPage, questionnaireInstructionWebPage, participatInfoWebPage, endquestionnaireWebPage]

index_element = web_pages_order.index(questionnaireInstructionWebPage)

for x in range(N):
    web_pages_order.insert(index_element + 1, questionWebPage)"""
    
    code_15 = """\
web_pages = ['welcomeWebPage', 'introductionWebPage', 'exampleWebPage', 'warmUpWebPage', 'questionnaireInstructionWebPage', 'participatInfoWebPage', 'endquestionnaireWebPage']

index_element = web_pages.index('questionnaireInstructionWebPage')

for x in range(N):
    web_pages.insert(index_element + 1, 'questionWebPage')"""
    
    code_16 = """\
def next_clicked(b):
    current_web_page = web_pages[0]

    if current_web_page == 'warmUpWebPage':
        # The Warm-Up section will have questions for measuring the user's mental mental
        # Check if the questions are answered before continuing with the questionnaire
        pass
    elif current_web_page == 'questionWebPage':
        # Each question section will have some questions that the user must answers 
        # Before continuing with the next questions section, check if the user answers all of the questions in the current section
        pass
        
    web_pages.pop(0)
    web_page = web_pages_order.pop(0)
    web_page()

def submit_clicked(b):
    current_web_page = web_pages[0]
    
    if current_web_page == 'participatInfoWebPage':
        if gender_selection.value == None or age_selection.value == None or education_selection.value == None or english_level_selection.value == None:
            return
    
    # Store/Send the answers of the user
    
    web_pages.pop(0)
    web_page = web_pages_order.pop(0)
    web_page()
    
next_button.on_click(next_clicked)
submit_button.on_click(submit_clicked)"""
    
    code_17 = """\
welcomeWebPage()"""
    
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
               nbf.v4.new_code_cell(code_17)
    ]
    
    nbf.write(nb,'./Output/Questionnaire_Template.ipynb')