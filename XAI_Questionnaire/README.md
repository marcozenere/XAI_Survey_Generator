# README

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