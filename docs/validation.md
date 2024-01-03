# **5.1. Validation**

## **5.1.1. Table of Content - Validation**
- [5.1.1. Table of Content - Validation](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/docs/validation.md#511-table-of-content---validation)
- [5.1.2. PEP8 Validation](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/docs/validation.md#512-pep8-validation)
- [5.1.3. HTML Validation](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/docs/validation.md#513-html-validation)
- [5.1.4. CSS Validation](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/docs/validation.md#514-css-validation)
- [5.1.5. JS Validation](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/docs/validation.md#515-js-validation)
- [5.1.6. WAVE Validation](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/docs/validation.md#516-wave-validation)
- [5.1.7. Lighthouse](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/docs/validation.md#517-lighthouse)

## **5.1.2. PEP8 Validation**

- **Task :** To ensure `*.py` files are compliant with PEP8 standards.
- **Tools :** 
  - [Black](https://black.readthedocs.io/en/stable/) - PY linter and formatter
  - [CI Python Linter](https://pep8ci.herokuapp.com/) - Visualizing PY linter
- **Method :** 
   - Install `Black` using `pip install black` in terminal
   - Use command `black --line-length 79 DIRECTORY_NAME/` to format `*.py` files in the selected directory or use `black --line-length 79 .` to format all files
   - See in the terminal window result of this operation *( Appendix 51 )*
   - Double check the results in `CI Python Linter` by copying and pasting the Python code as black doesn't wrap lines of comments. See result on the right hand side of the input field *( Appendix 52 )*
- **Results :**
The only file failing the PEP8 standard is `glimmer/settings.py` due length of lines of module names.

| Directory      | File            | Result                                                   |
| -------------- | --------------- | -------------------------------------------------------- |
| administrator  | \`admin.py\`    | <span style="color:green;">PASS</span>                   |
| administrator  | \`urls.py\`     | <span style="color:green;">PASS</span>                   |
| administrator  | \`views.py\`    | <span style="color:green;">PASS</span>                   |
| artists        | \`admin.py\`    | <span style="color:green;">PASS</span>                   |
| artists        | \`models.py\`   | <span style="color:green;">PASS</span>                   |
| artists        | \`urls.py\`     | <span style="color:green;">PASS</span>                   |
| artists        | \`views.py\`    | <span style="color:green;">PASS</span>                   |
| bookings       | \`admin.py\`    | <span style="color:green;">PASS</span>                   |
| bookings       | \`forms.py\`    | <span style="color:green;">PASS</span>                   |
| bookings       | \`models.py\`   | <span style="color:green;">PASS</span>                   |
| bookings       | \`urls.py\`     | <span style="color:green;">PASS</span>                   |
| bookings       | \`views.py\`    | <span style="color:green;">PASS</span>                   |
| landing        | \`admin.py\`    | <span style="color:green;">PASS</span>                   |
| landing        | \`forms.py\`    | <span style="color:green;">PASS</span>                   |
| landing        | \`urls.py\`     | <span style="color:green;">PASS</span>                   |
| landing        | \`views.py\`    | <span style="color:green;">PASS</span>                   |
| news           | \`admin.py\`    | <span style="color:green;">PASS</span>                   |
| news           | \`forms.py\`    | <span style="color:green;">PASS</span>                   |
| news           | \`models.py\`   | <span style="color:green;">PASS</span>                   |
| news           | \`urls.py\`     | <span style="color:green;">PASS</span>                   |
| news           | \`views.py\`    | <span style="color:green;">PASS</span>                   |
| profilemanager | \`admin.py\`    | <span style="color:green;">PASS</span>                   |
| profilemanager | \`forms.py\`    | <span style="color:green;">PASS</span>                   |
| profilemanager | \`models.py\`   | <span style="color:green;">PASS</span>                   |
| profilemanager | \`urls.py\`     | <span style="color:green;">PASS</span>                   |
| profilemanager | \`views.py\`    | <span style="color:green;">PASS</span>                   |
| styles         | \`admin.py\`    | <span style="color:green;">PASS</span>                   |
| styles         | \`forms.py\`    | <span style="color:green;">PASS</span>                   |
| styles         | \`models.py\`   | <span style="color:green;">PASS</span>                   |
| styles         | \`urls.py\`     | <span style="color:green;">PASS</span>                   |
| styles         | \`views.py\`    | <span style="color:green;">PASS</span>                   |
| glimmer        | \`asgi.py\`     | <span style="color:green;">PASS</span>                   |
| glimmer        | \`settings.py\` | <span style="color:red;">FAIL</span> *( Appendix 53 )* |
| glimmer        | \`urls.py\`     | <span style="color:green;">PASS</span>                   |
| glimmer        | \`wsgi.py\`     | <span style="color:green;">PASS</span>                   |

*Appendix 51 - Black result message*

![Black result message](/docs/validation/black.png)

*Appendix 52 - CI Python Linter result message*

![CI Python Linter result message](/docs/validation/ci_linter.png)

*Appendix 53 - `glimmer/settings.py`*

![`glimmer/settings.py`](/docs/validation/settings_pep8.png)

[Back to top](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/docs/validation.md#51-validation)
[Back to README.md](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/tree/main#1-key-project-information)

---

## **5.1.3. HTML Validation**

- **Task :** To ensure source code generated from all `*.html` templates is compliant with W3C standards.
- **Tools :** 
  - [W3C HTML Validator](https://validator.w3.org/) - HTML Validator
- **Method :** 
   - Open each page of the project
   - In Chrome : Right click on page background and select `View Page Source`
   - Copy and Paste the generated code from browser to validator
   - See results *( Appendix 54 )*
   - Please note this needs to be done for all states of the templates (i.e. Logged In / Logged Out, etc.)
- **Results :**
Two files (`all_news.html` and `news_detail.html`) are failing this validation due SummerNote that inserts inline variables that this validator isn't able to parse and comes up with `Parse error`.


| Directory      | File                            | State                   | Result                                                                 |
| -------------- | ------------------------------- | ----------------------- | ---------------------------------------------------------------------- |
| administrator  | \`admin_menu.html\`             | Only Logged in as admin | <span style="color:green;">PASS</span>                                 |
| artists        | \`artist_detail.html\`          | Not Applicable          | <span style="color:green;">PASS</span>                                 |
| artists        | \`artists.html\`                | Not Applicable          | <span style="color:green;">PASS</span>                                 |
| bookings       | \`booking_cancel_confirm.html\` | Only Logged in          | <span style="color:green;">PASS</span>                                 |
| bookings       | \`bookings.html\`               | Only Logged in          | <span style="color:green;">PASS</span>                                 |
| bookings       | \`edit_booking.html\`           | Only Logged in          | <span style="color:green;">PASS</span>                                 |
| bookings       | \`new_booking.html\`            | Only Logged in          | <span style="color:green;">PASS</span>                                 |
| landing        | \`index.html\`                  | Not Applicable          | <span style="color:green;">PASS</span>                                 |
| landing        | \`search_results.html\`         | Not Applicable          | <span style="color:green;">PASS</span>                                 |
| news           | \`all_news.html\`               | Not Applicable          | <span style="color:red;">FAIL 1000 + errors</span> *( Appendix 55 )* |
| news           | \`news_detail.html\`            | Logged In               | <span style="color:red;">FAIL 400 + errors</span> *( Appendix 55 )*  |
| news           | \`news_detail.html\`            | Logged Out              | <span style="color:red;">FAIL 400 + errors</span> *( Appendix 55 )*  |
| profilemanager | \`my_details.html\`             | Only Logged In          | <span style="color:green;">PASS</span>                                 |
| styles         | \`style_detail.html\`           | Logged In               | <span style="color:green;">PASS</span>                                 |
| styles         | \`style_detail.html\`           | Logged Out              | <span style="color:green;">PASS</span>                                 |
| styles         | \`styles.html\`                 | Not Applicable          | <span style="color:green;">PASS</span>                                 |
| templates      | \`403.html\`                    | Not Applicable          | <span style="color:green;">PASS</span>                                 |
| templates      | \`404.html\`                    | Not Applicable          | <span style="color:green;">PASS</span>                                 |
| templates      | \`500.html\`                    | Not Applicable          | <span style="color:green;">PASS</span>                                 |
| templates      | \`base.html\`                   | Not Applicable          | <span style="color:green;">PASS</span>                                 |
| templates      | \`footer.html\`                 | Not Applicable          | <span style="color:green;">PASS</span>                                 |
| templates      | \`header.html\`                 | Logged In               | <span style="color:green;">PASS</span>                                 |
| templates      | \`header.html\`                 | Logged Out              | <span style="color:green;">PASS</span>                                 |
| account        | \`\*.html\`                     | Logged In               | <span style="color:green;">PASS</span>                                 |
| account        | \`\*.html\`                     | Logged Out              | <span style="color:green;">PASS</span>                                 |


*Appendix 54 - W3C HTML Validator*

![W3C HTML Validator](/docs/validation/w3c_html.png)

*Appendix 55 - SummerNote errors*

![SummerNote Errors](/docs/validation/sum_err.png)

[Back to top](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/docs/validation.md#51-validation)
[Back to README.md](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/tree/main#1-key-project-information)

---

## **5.1.4. CSS Validation**

- **Task :** To ensure the code in `style.css` is compliant with W3C standards.
- **Tools :** 
  - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - CSS Validator
- **Method :** 
   - Open the `style.css` file
   - Copy and Paste the code from IDE to validator
   - See results
- **Results :**

My `style.css` file did pass with <span style="color:green;">NO ERRORS</span> *( Appendix 56 )* and <span style="color:yellow;">24 WARNINGS</span> *( Appendix 57 )*.

Reasons for this result : 
- Validator isn't able to check imports - *Imported style sheets are not checked in direct input and file upload modes*
- Validator isn't able to check vendor pseudo elements - *`::-webkit-scrollbar` is a vendor extended pseudo-element*
- Validator isn't able to check dynamic states of elements - *Due to their dynamic nature, CSS variables are currently not statically checked*

*Appendix 56 - CSS Validation - errors*

![CSS Validation - errors](/docs/validation/css_err.png)

*Appendix 57 - CSS Validation - warnings*

![CSS Validation - warnings](/docs/validation/css_war.png)

[Back to top](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/docs/validation.md#51-validation)
[Back to README.md](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/tree/main#1-key-project-information)

---

## **5.1.5. JS Validation**

- **Task :** To ensure the code in `*.js` has no errors.
- **Tools :** 
  - [JSHint](https://jshint.com/) - JS Validator
- **Method :** 
   - Open the `*.js*` files
   - Copy and Paste the code from IDE to validator
   - See results
- **Results :**
All `*.js` files passed without errors *( Appendix 58 )*.

| File                   | Result                                 |
| ---------------------- | -------------------------------------- |
| \`comments_news.js\`   | <span style="color:green;">PASS</span> |
| \`comments_styles.js\` | <span style="color:green;">PASS</span> |
| \`edit_booking.js\`    | <span style="color:green;">PASS</span> |
| \`messages.js\`        | <span style="color:green;">PASS</span> |
| \`new_booking.js\`     | <span style="color:green;">PASS</span> |

*Appendix 58 - JS Validation*

![CSS Validation](/docs/validation/jshint.png)

[Back to top](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/docs/validation.md#51-validation)
[Back to README.md](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/tree/main#1-key-project-information)

---

## **5.1.6. WAVE Validation**

- **Task :** To ensure all pages are within accessibility standards and are suitable for screen-readers.
- **Tools :** 
  - [WAVE Accessibility](https://wave.webaim.org/) - WAVE Validator
- **Method :** 
   - Install WAVE Chrome extension 
   - Browse each page and click on `WAVE Icon` *( Appendix 59 )*
   - See results on the left hand panel *( Appendix 60 )*
   - Please note this needs to be done for all states of the pages (i.e. Logged In / Logged Out, etc.)
- **Results :**
In the project, I have got no Alert's or Contrast Errors, each page got multiple warnings due to Redundant links.

| Directory      | File                            | State                   | Errors | Alerts | Nature of problem | Result                                 |
| -------------- | ------------------------------- | ----------------------- | ------ | ------ | ----------------- | -------------------------------------- |
| administrator  | \`admin_menu.html\`             | Only Logged in as admin | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| artists        | \`artist_detail.html\`          | Not Applicable          | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| artists        | \`artists.html\`                | Not Applicable          | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| bookings       | \`booking_cancel_confirm.html\` | Only Logged in          | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| bookings       | \`bookings.html\`               | Only Logged in          | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| bookings       | \`edit_booking.html\`           | Only Logged in          | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| bookings       | \`new_booking.html\`            | Only Logged in          | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| landing        | \`index.html\`                  | Not Applicable          | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| landing        | \`search_results.html\`         | Not Applicable          | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| news           | \`all_news.html\`               | Not Applicable          | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| news           | \`news_detail.html\`            | Logged In               | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| news           | \`news_detail.html\`            | Logged Out              | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| profilemanager | \`my_details.html\`             | Only Logged In          | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| styles         | \`style_detail.html\`           | Logged In               | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| styles         | \`style_detail.html\`           | Logged Out              | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| styles         | \`styles.html\`                 | Not Applicable          | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| templates      | \`403.html\`                    | Not Applicable          | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| templates      | \`404.html\`                    | Not Applicable          | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| templates      | \`500.html\`                    | Not Applicable          | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| templates      | \`base.html\`                   | Not Applicable          | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| templates      | \`footer.html\`                 | Not Applicable          | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| templates      | \`header.html\`                 | Logged In               | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| templates      | \`header.html\`                 | Logged Out              | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| account        | \`\*.html\`                     | Logged In               | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |
| account        | \`\*.html\`                     | Logged Out              | No     | Yes    | Redundant links   | <span style="color:green;">PASS</span> |

*Appendix 59 - WAVE Extension*

![WAVE Extension](/docs/validation/wave_icon.png)

*Appendix 60 - WAVE Results*

![WAVE Results](/docs/validation/wave.png)

[Back to top](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/docs/validation.md#51-validation)
[Back to README.md](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/tree/main#1-key-project-information)

---

## **5.1.7. Lighthouse**

- **Task :** To ensure that speeds of project loading are viable.
- **Tools :** 
  - [Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) - Chrome Lighthouse documentation
- **Method :** 
   - Browse each page and click on `More Tools > Developer Tools > Lighthouse > Analyze Page Load` *( Appendix 61 )*
   - See results on the right hand panel *( Appendix 62 )*
- **Results :**
Suggestion was made on pages `News`, `Styles` and `Artists` to use `webp` image format instead of current `jpg` format. This can be achieved by auto-converting files in database Cloudinary fields (recorded as future feature).

*Appendix 61 - Lighthouse*

![Lighthouse](/docs/validation/lighthouse.png)

*Appendix 60 - Lighthouse Results*

![Lighthouse Results](/docs/validation/lighhouse_result.png)

[Back to top](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/docs/validation.md#51-validation)
[Back to README.md](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/tree/main#1-key-project-information)

---
