# Testing


## Code validation
Following resources were used for code validation
  - [Closing Tag Checker for HTML5](https://www.aliciaramirez.com/closing-tags-checker/) was using to validate all tags  
  - [W3C Markup Validation Service](https://validator.w3.org/) was using on this project.
  - [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was using on this project.
  - [JavaScript JSHINT Service](https://jshint.com/) was using for code warning & error check
  - [Python Syntax Checker](https://extendsclass.com/python-tester.html) was using to validate app.py file's code syntax error
  - [Python PEP8 requirements](http://pep8online.com/) was using to validate app.py file's code for PEP8 requirements


### HTML

- Ran HTML code through [W3C Markup Validation Service](https://validator.w3.org/) for code warning & error check.
  - One Warning message were received:
    - **Warning**: Section lacks heading. Consider using h2-h6 elements to add identifying headings to all sections.

- [Closing Tag Checker for HTML5](https://www.aliciaramirez.com/closing-tags-checker/) was using to validate all tags
  - No unclosed tags detected.

### CSS
- Ran CSS code through [W3C CSS Validation Service](https://validator.w3.org/) for code warning & error check.
  - No errors found.
  - Relevant logos are placed on homepage footer

### JavaScript
- Ran JavaScript code through [JavaScript JSHINT Service](https://jshint.com/) for code warning & error check.
The website is used a small amount of direct Javascript coding
  - The following (general) Warning messages were received:
    - Undefined variables

- All variables were fixed or ignored, as code is working properly

### Python
- [Python Syntax Checker](https://extendsclass.com/python-tester.html) was using to validate app.py file's code syntax error
  - No syntax errors detected 

- [Python PEP8 requirements](http://pep8online.com/) was using to validate app.py file for PEP8 requirements.
  - The following warning messages were received:
    - E125 continuation line with same indent as next logical line
    - E128 continuation line under-indented for visual indent
    - E303 too many blank lines
    - W291 trailing whitespace
    - W292 no newline at end of file
- All errors were fixed


## GENERAL (Manual testing)

**Homepage Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on Recipes navigation element, it goes to the relevant page.
  - Clicked on Stats navigation element, it goes to the relevant page.
  - Clicked on Partners navigation element, it goes to the relevant page.
  - Clicked on Log In navigation element, it goes to the relevant page.
  - Clicked on Register navigation element, it goes to the relevant page.
  - Clicked on Read More Button in Each Grid element, all of them goes to the relevant page.
  - Clicked on Social links icons in the footer, each icon goes to the relevant page.

**Recipes Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.
  - Added text to search box, it works properly
  - Added not searchable text, Result not found sign is displayed
  - Clicked on Full Recipe Button in Each Grid element, all of them goes to the relevant page.


**Stats Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.
  - Clicked on Read more Button it goes to the relevant page.


**Partners Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.
  - Clicked on Visit Shop Button in Each Grid element, all of them goes to the relevant page.

**Register Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.
  - Filled up form and submitted, it goes to user profile page.

**Log In Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.
  - Filled up form and submitted, it goes to user profile page.

**After login:**
**Profile Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.
  - Clicked on Full Recipe Button in Each Grid element, all of them goes to the relevant page.
  - Clicked on Manage Category Button it goes to the relevant page.
  - Clicked on Manage Cuisine Button it goes to the relevant page.

**Single Recipe Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.
  - Clicked on Edit Button it goes to the relevant page.
  - Clicked on Remove Recipe Button it goes to the relevant page.

**Add Recipe Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.
  - After adding content to all fields and Clicked on Add Recipe Button it goes to the relevant page.
  - Clicked on Clear Button it clears all fields.

**Manage Category Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.
  - Clicked on Add Category Button it goes to the relevant page.
  - Clicked on Edit Button on every category card it goes to the relevant page.
  - Clicked on Delete Button on every category card it goes to the relevant page and delete category.

**Add Category Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.
  - After adding content to the field and Clicked on Add Category Button it goes to the relevant page.
  - Clicked on Clear Button it clears the field.

**Manage Cuisine Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.
  - Clicked on Add Cuisine Button it goes to the relevant page.
  - Clicked on Edit Button on every cuisine card it goes to the relevant page.
  - Clicked on Delete Button on every cuisine card it goes to the relevant page and delete cuisine.

**Add Cuisine Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.
  - After adding content to the field and Clicked on Add Cuisine Button it goes to the relevant page.
  - Clicked on Clear Button it clears the field.

### Cross Browser and Cross Device Testing

Testing was done for the following devices:

| TOOL / Device  |  BROWSER |  OS |  SCREEN WIDTH |
|---|---|---|---|
| Desktop  | Edge  | windows 10  |  1920 x 1080 |
| Desktop  | Chrome | windows 10  |  1920 x 1080 |
|  Desktop | Opera  |  windows 10 | 1920 x 1080  |
|  Desktop | Firefox  |  windows 10 | 1920 x 1080  |
| Desktop  | IE  | windows 10  |  1920 x 1080 |
| Laptop  | Edge | windows 10  |  1366 x 768 |
| Laptop | Chrome  |  windows 10 | 1366 x 768  |
| Laptop  | Opera  | windows 10  |  1366 x 768 |
| Laptop  | Firefox  | windows 10  |  1366 x 768 |
| Laptop  | IE | windows 10  |  1366 x 768 |
|  MP Samsung S10+ | Chrome  |  android | 1440 x 3040  |
|  MP Samsung S10+ | Samsung  |  android | 1440 x 3040  |
|  ipad | Chrome  |  iOs | 1024 x 768  |
|  ipad | Safari  |  iOs | 1024 x 768  |


## Responsiveness
- Below is a picture of site that shows it in responsive states. 
[link to check a website to be responsive](http://ami.responsivedesign.is)
![picture of site](assets/images/responsive.png)


