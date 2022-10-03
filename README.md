# Table of Contents 

1. [**Introduction**](#Introduction)
2. [**User Experience (UX)**](#User-Experience-(UX))
    * [Project goals](#Project-goals)
    * [Target audience](#Target-audience)
    * [User stories](#User-stories)
    * [Structure](#Structure)
    * [Design](#Design)

3. [**Features**](#Features)
    * [Existing Features](#Existing-Features)
    * [Features to be implemented in the future](#Features-to-be-implemented-in-the-future)

4. [**Technologies used**](#Technologies-used)

5. [**Deployment**](#Deployment)
    * [Deploying to Heroku](#Deploying-to-Heroku)
    * [Forking to GitHub Repository](#Forking-to-GitHub-Repository)
    * [Making a local clone](#Making-a-local-clone)

6. [**Testing**](#Testing)
    * [Testing Approach](#Testing-Approach)
    * [User stories testing from the UX section](#User-stories-testing-from-the-UX-section)
    * [Validator Testing](#Validator-Testing)
    * [Issues and Bugs](#Issues-and-Bugs)

7. [**Credits**](#Credits)

8. [**Acknowledgments**](#Acknowledgments)

9. [**Disclaimer**](#Disclaimer)

<br>

# Hush Daisies

[Live site](https://hush-daisies.herokuapp.com/)

![HushDaisies image](docs/responsive-site.png)


## Introduction
---

Hush Daisies 


## User Experience (UX)
---
### Project goals  

* 

*


### Target audience

* 

  

### User stories:

**Agile methodology:**

  The development of this project was managed with the principles of agile methodology in mind. 
  Planned features were defined and organised into the following [Epics](https://github.com/renatabiniek/hush-daisies/milestones?with_issues=no) at the start of the project.  
  
  EPIC | View and Navigation  
  EPIC | Account  
  EPIC | User profile  
  EPIC | Admin  
  EPIC | Products  
  EPIC | Orders and payments  
  EPIC | Workshops  
  EPIC | Marketing & SEO  
  EPIC | Contact

  Epics were then broken down into atomic user stories and organised according to the MoSCoW prioritization approach. 
  Around the recommended 60% of user stories are identified as the must-have features. Further user stories were added throughout the development. 
  Only limited number of user stories was worked on, completed and tested in each iteration.

  The user stories were recorded and managed via the Github issues functionality and the Projects board. 
  The list can be viewed [here](https://github.com/users/renatabiniek/projects/3).

**Site User:** [NEEDS UPDATE!]

* As a site user, I can 

**Registered User:**

* 



**Site Admin:**

* 


### Structure:

* Wireframes

  Low fidelity mock-ups were made using [Balsamiq](https://balsamiq.com/wireframes/) to help plan and visualise the navigation design, placement of information, features, relationship between the content and usefulness. They were created for mobile and desktop screen sizes.

  The project was developed from initial wireframes and some modifications were made during the development process to assure better usability, and sufficient content.


  *Final wireframes:* [NEEDS UPDATE!]

  *Mobile:*

  [Mobile - Home](docs/wireframes/mobile/Mobile-Home.png)  
  [Mobile - SignIn](docs/wireframes/mobile/Mobile-SignIn.png)  
  [Mobile - Tools](docs/wireframes/mobile/Mobile-Tools.png)  
  [Mobile - Categories](docs/wireframes/mobile/Mobile-Categories.png)
  [Mobile - Manage](docs/wireframes/mobile/Mobile-Manage.png)  

  [Mobile - All in pdf](docs/wireframes/mobile/Mobile-MoodBox.pdf) 
  
  *Desktop:*

  [Desktop - Home](docs/wireframes/desktop/Desktop-Home.png)  
  [Desktop - SignIn](docs/wireframes/desktop/Desktop-Signin.png)  
  [Desktop - Tools](docs/wireframes/desktop/Desktop-Tools.png)  
  [Desktop - Categories](docs/wireframes/desktop/Desktop-Categories.png)
  [Desktop - Manage](docs/wireframes/desktop/Desktop-Manage.png)  

  [Desktop - All in pdf](docs/wireframes/desktop/Desktop-MoodBox.pdf) 

  
* Database Schema

  A relational database was used for this project. The database consists of the following models: User (Django built-in model), UserProfileOrder, Product, Category, Order, OrderLineItem, Workshop, WorkshopTestimonials, WorkshopFavourites and Request. 
  Django AllAuth was used for user authentication. The database schema has been prepared using drawSQL. Limitations of the tool prevented accurate choice of field types (e.g. EmailField, URLField).

  **Hush Daisies database schema:**  

  ![Database diagram image](docs/database/database-schema.png)


### Design: 

* **Colour scheme**

[NEEDS UPDATE!]


* **Typography**

  [NEEDS UPDATE!]
 

* **Imagery**

  [NEEDS UPDATE!]


## Features
---

[NEEDS UPDATE!]
 

### Existing Features

* Navigation  [NEEDS UPDATE!]

  * 
  * 

* Footer  [NEEDS UPDATE!]

  *  
  
* Home Page  [NEEDS UPDATE!]

  *  
  * [NEEDS UPDATE!]
  
* Sign Up

  * [NEEDS UPDATE!]

  
* Log In  

  * [NEEDS UPDATE!]
  
* Log Out  

  * [NEEDS UPDATE!]
  
* [NEEDS UPDATE!] 
  
  * 


### Features to be implemented in the future

* [NEEDS UPDATE!]

## Technologies used
---

### Languages 

* HTML
* CSS
* JavaScript
* Python (with Django framework)
* Django templating language 


### Frameworks, Libraries, Programmes and Tools 
 
* [Django web framework](https://www.djangoproject.com/) - used to build the project
* [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - for responsiveness, layout, modals, and general frontend style
* [AWS](https://aws.amazon.com/) - to host media and static files 
* [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html) - for user registration and authentication
* [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template) - to display and run the command line terminal in the browser
* [drawSQL](https://drawsql.app/) - to create the database diagram model
* [Balsamiq](https://balsamiq.com/) - to create wireframes for the site as part of the preparation work for the project
* [Google Fonts](https://fonts.google.com/) - to import Courgette and Montserrat fonts into the HTML file which were then used throughout the site
* [Coolors](https://coolors.co/ ) - to create cohesive colour scheme for the site
* [Eye Dropper](https://eyedropper.org/) - to pick specific colours from images 
* [Favicon.io](https://favicon.io/) - to create a favicon for the site
* [NEEDS UPDATE!] - to edit and resize images
* [Chrome DevTools](https://developer.chrome.com/docs/devtools/) - to inspect and debug the code through all stages of the development
* [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) - to inspect the site for overflow 
* [Lighthouse](https://developers.google.com/web/tools/lighthouse) - to audit the site for performance, accessibility, SEO and best practices
* [Am I Responsive](http://ami.responsivedesign.is/) - to produce a preview of the site on different devices
* [W3C HTML Validator](https://validator.w3.org/) - to validate HTML code
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - to validate CSS code
* [PEP8 Online Validation Service](http://pep8online.com/) - to validate the code
* [Color Contrast Accessibility Validator](https://color.a11y.com/Contrast/) - to test the contrast and readability of colours used 
* [Heroku](https://heroku.com/) - for presenting the deployed project
* [Heroku Postgres](https://www.heroku.com/postgres) - the database for the deployed project
* [GitHub](https://github.com/) - for hosting the project code and version control 
* [GitHub issues](https://github.com/) - used as Agile tools in the planning and implementation of the project
* [Gitpod](https://gitpod.io/) - to write the code and push it to GitHub
* [Online-Spellcheck](https://www.online-spellcheck.com/) - to spellcheck the README


## Deployment [NEEDS UPDATE!]
---
### Deploying to Heroku

[Deployed program on Heroku](https://hush-daisies.herokuapp.com/)

The project was developed in GitPod, committed to Git and pushed to GitHub. 
The site was deployed to Heroku with the following steps:

  **Initial setup:**

  1. In GitPod, install Django and supporting libraries.
  2. Import the required dependencies to the requirements.txt file, using ```pip3 freeze --local > requirements.txt```
  3. Create the Django project and app.
  4. Add the app name to ```INSTALLED_APPS``` list in ```settings.py```.
  5. Migrate initial migrations created by typing in the command line ```python3 manage.py migrate```.
  6. Git add, commit and push the saved changes to GitHub. Heroku will use this file to import the dependencies that are required.

  **Deployment to Heroku:**

  1. Sign up and log in to [Heroku](https://heroku.com).
  2. On the dashboard, click **New** in the top right-hand corner and select **Create New App**.
  3. Select a *unique* name for your application and choose your region (Europe in my case).
  4. Click **Create App**.
  5. Attach the Postgres database: 
  * In the **Resources** tab, under Add-ons, type in **Postgres** and select the **Heroku Postgres** option.
  6. Navigate to the **Settings** tab (must be done before deploying code)
  7. Go to section **Config Vars**, click button **Reveal Config Vars** and press **Add** button.
  8. Add the below variables to the list: 

  * DATABASE_URL (added automatically)
  * SECRET_KEY
  * CLOUDINARY_URL

  9. Back in your code, update the ```settings.py``` file to import the env file and add the SECRET_KEY and DATABASE_URL file paths.
  10. Also in the ```settings.py``` add the following:

      Cloudinary to the INSTALLED_APPS list  

      STATICFILE_STORAGE  
      STATICFILES_DIRS  
      STATIC_ROOT  
      MEDIA_URL  
      DEFAULT_FILE_STORAGE  
      TEMPLATES_DIR  
      Update DIRS in TEMPLATES with TEMPLATES_DIR  
      Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']
  
  11. Store static and media files in Cloudinary:
  * Create 3 folders in the main directory; media, static and templates.
  * Create **Procfile** and add: ```web: gunicorn PROJ_NAME.wsgi```
  12. Add and commit the changes and push to GitHub.
  12. Navigate to the Deploy tab and scroll down to **Deployment Method**.
  15. Select GitHub as deployment method.
  16. Enter the name of the repository you want to connect to and click **Connect**.
  17. Select one of the deployment options - Automatic Deployments or Manual - to deploy the app.
  18. Once successfully deployed, a **View** button will appear and take you to a mock terminal.

  **Final deployment to Heroku**

  1. Ensure all files are up to date in Gitpod.
  2. Ensure DEBUG is set to FALSE in settings.py.
  3. Add "X_FRAME_OPTIONS= 'SAME ORIGIN'" to settings.py, to ensure that Summernote editor works in deployed project.
  4. Add, commit and push deployment commit to GitHub.
  5. In Heroku, go to Settings tab and click Reveal config vars. Remove DISABLE_COLLECTSTATIC variable.
  6. Go to Deploy tab and scroll down to Deploy Branch. 
  7. Run deployment and wait for confirmation that application has deployed.


  ### Forking to GitHub Repository [NEEDS UPDATE!]

  You can create a fork (copy) of the repository. This allows you to experiment with the code without affecting the original project.

  To fork the repository:

  1. Log in to your [GitHub](https://github.com/) account.
  2. On GitHub, navigate to the repository you want to fork.
  3. In the top right corner of the page, underneath your profile avatar, click **Fork**.
  4. You should now have a copy of the original repository in your GitHub account.

  ### Making a local clone

  You can clone your repository to create a local copy on your computer. Any changes made to the local copy will not affect the original project. To clone the **Hush Daisies** project, follow the steps below:

  1. Log in to your [GitHub](https://github.com/) account and locate the [Hush Daisies repository](https://github.com/renatabiniek/hush-daisies).
  2. In the repository, click on **Code** button located above all the project files.
  3. Under HTTPS, copy the link generated (https://github.com/renatabiniek/hush-daisies.git).
  4. Open the terminal you're using, e.g. Gitpod.
  5. Change the current working directory to the location where you want the cloned directory created.
  6. Type ```git clone``` and then paste the URL you copied earlier:  
  ```git clone https://github.com/renatabiniek/hush-daisies.git``` 
  7. Press **Enter** to create your local clone.

You can also refer to this [GitHub documentation](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) for detailed instructions. 

## Testing
---

### Testing Approach [NEEDS UPDATE!]

The site was tested manually. 
[NEEDS UPDATE!]

* **Manual testing:**

[NEEDS UPDATE!]

### User stories testing from the UX section

I tested the program considering the user stories from the UX section as well.

* [NEEDS UPDATE!]

  

### Validator Testing

* **PEP8 online**

[NEEDS UPDATE!]


* **W3C HTML Validator**

[NEEDS UPDATE!]


* **W3C CSS Validator**

[NEEDS UPDATE!]

* **JSHint**

[NEEDS UPDATE!]

* **Lighthouse**

[NEEDS UPDATE!]


* **Color contrast:**

[NEEDS UPDATE!]

* **Content:**

[NEEDS UPDATE!]

### Issues and Bugs

* **[NEEDS UPDATE!]**


### Devices and browsers tested

[NEEDS UPDATE!]


### Credits

* [NEEDS UPDATE!]

* 

### Acknowledgments

Thank you to:

* [NEEDS UPDATE!]

### Disclaimer

This website is ficiotnal and has been created for educational purposes only, as part of Code Institute’s Portfolio Project 5, E-commerce Application. The requirements are to build a Full-stack site based on business logic used to control a centrally-owned dataset.

[Back to top](#Table-of-Contents)