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
 - Everything is coded properly. Few Warning message were received:
 - **Warning**, there was an unnecessary type attribute for JavaScript resources (the attribute was removed)
 - **Warning**, there was an empty headings for h2 id="confirmation-title" and h3 id="confirmation-title-email". As they are used to display confirmation message on form submit, they are left empty.
 - **Error**, there was empty value for attribute src on element img. As it is used as a placeholder for the Gallery light box image, everything is left as it is.

- [Closing Tag Checker for HTML5](https://www.aliciaramirez.com/closing-tags-checker/) was using to validate all tags 


### CSS
 - Ran CSS code through [W3C CSS Validation Service](https://validator.w3.org/) for code warning & error check.
   - Everything is coded properly. Few Warning message were received:
   - Warning, for imported fonts, their style sheets are not checked in direct input and file upload modes. This warning is ignored.
   -  Warning, for color variables as an unknown vendor extension. This warning is ignored
   - No errors found.
   - Relevant logos are placed on homepage footer

### JavaScript
- Ran JavaScript code through [JavaScript JSHINT Service](https://jshint.com/) for code warning & error check.
   - The following (general) Warning messages were received:
   - Missing semicolon
   - Undefined variables such as google, toggleBounce, initMap.
   - The body of a for in should be wrapped in an if statement to filter unwanted properties from the prototype.

 - All semicolon were added. All variables were fixed or ignored, as code is working properly
For loop was not wrapped into if statement, because it was not necessary by functionality.

### Python
  - [Python Syntax Checker](https://extendsclass.com/python-tester.html) was using to validate app.py file's code syntax error
  - [Python PEP8 requirements](http://pep8online.com/) was using to validate app.py file's code syntax error


## GENERAL (Manual testing)

**Homepage Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on Recipes navigation element, it goes to the relevant page.
  - Clicked on Stats navigation element, it goes to the relevant page.
  - Clicked on Partners navigation element, it goes to the relevant page.
  - Clicked on Log In navigation element, it goes to the relevant page.
  - Clicked on Log In navigation element, it goes to the relevant page.
  - Clicked on View More Button in Each Grid element, all of them goes to the relevant page.
  - Added email to Newsletter sign up field and Clicked on Sign Up Button, the page is connected to dummy Code Institute mail service.
  - Clicked on Social links icons in the footer, each icon goes to the relevant page.   - Clicked on Social links icons in the footer, each icon goes to the relevant page.

**Recipes Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.


**Stats Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.


**Partners Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.


**Log In Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.

**Register Page**
  - Clicked on header Logo icon, it goes to Home page.
  - Clicked on every header navigation elements, all of them goes to the relevant page.

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

### Testing stories from UX perspectives:

- As a user, I have:
  1. Ability to easily find out what or who the site is for.
  2. Ability to easily navigate the website.
  3. Ability to find recipes.
  4. Ability to get recipe's full details.
  5. Ability to create account.
  6. Ability to update account.
  7. Ability to login into account.
  8. Ability to add new recipe.
  9. Ability to edit my recipe.
  10. Ability to get in touch with website admin or owner.
