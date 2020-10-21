# Work in Progress

# Milestone Project 4 with *Code Institute*


# Table of Content

  * [UX](#ux)
  * [User Stories](#user-stories)
  * [Wireframes](#wireframes)
    + [Planned Layout](#planned-layout)
    + [Final Layout](#final-layout)
    + [Explanation for differences](#explanation-for-differences)
    + [Color Scheme](#color-scheme)
  * [Data Model](#data-model)
    + [Gear Collection](#gear-collection)
    + [Categories Collection](#categories-collection)
    + [Users Collection](#users-collection)
  * [Features](#features)
    + [Exisiting Features](#exisiting-features)
    + [Features Left to Implement](#features-left-to-implement)
  * [Technologies Used](#technologies-used)
  * [Testing](#testing)
    + [Test Cycle](#test-cycle)
    + [Validator Checks, Audits & Tools](#validator-checks--audits---tools)
    + [Known Bugs & Issues](#known-bugs---issues)
  * [Deployment](#deployment)
    + [Local Deployment](#local-deployment)
      - [Prerequisites to work with this Site](#prerequisites-to-work-with-this-site)
      - [Step-by-Step Instructions](#step-by-step-instructions)
    + [Deployment to Heroku](#deployment-to-heroku)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Acknowledgements](#acknowledgements)
      - [References](#references)

## UX


## User Stories

## Wireframes

### Planned Layout

#### Logo


#### Components


#### Wireframes


### Final Layout




### Explanation for differences


### Color Scheme


## Data Model
 

## Features


### Exisiting Features



### Features Left to Implement


## Technologies Used

## Testing

### Validator Checks, Audits & Tools

### Known Bugs & Issues

### Issues handled via development

- Templates not pulled from apps folder
-> make sure to have the following in settings.py
```
import os
DIRNAME = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'site-templates/'),
)
```

## Deployment

This site is deployed to heroku and the versioning was done with git and the Repository is hosted on Github.

### Local Deployment

#### Prerequisites to work with this Site


#### Step-by-Step Instructions



### Deployment to Heroku

## Credits

### Content

### Media

### Acknowledgements

### References 
* read up on making drop down full width https://stackoverflow.com/questions/49659305/how-to-make-a-bootstrap-4-full-width-dropdown-in-navbar
* horzizontal line readup https://stackoverflow.com/questions/16073323/horizontal-rule-line-beneath-each-h1-heading-in-css
* tutorial on how to animate scrollbar https://www.youtube.com/watch?v=vE4UuSzR5T0
* hear animation https://designmodo.com/shopping-cart-ui/
* how to custome style navbar https://medium.com/coder-grrl/the-guide-to-customising-the-bootstrap-4-navbar-i-wish-id-had-6-months-ago-7bc6ce0e3c71
* starting point for carousel https://startbootstrap.com/snippets/full-slider/
* inspiration for a mega menu https://www.w3schools.com/howto/howto_css_mega_menu.asp
