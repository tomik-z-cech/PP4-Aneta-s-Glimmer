# **5.1. Validation**

## **5.1.1 Table of Content - Validation**
- [5.1.2. PEP8 Validation]()
- [5.1.3. HTML Validation]()
- [5.1.4. CSS Validation]()
- [5.1.5. JS Validation]()
- [5.1.6. WAVE Validation]()

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

## **5.1.3. HTML Validation**

- **Task :** To ensure source code generated from all `*.html` templates is compliant with W3C standards.
- **Tools :** 
  - [W3C HTML Validator](https://validator.w3.org/) - HTML Validator
- **Method :** 
   - Open each page of the project
   - In Chrome : Right click on page background and select `View Page Source`
   - Copy and Paste the generated code from browser to validator
   - See results *( Appendix 54 )*
   - Please not this needs to be done for all states of the template (i.e. Logged In / Logged Out, etc.)
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

## **5.1.4 CSS Validation**

- **Task :** To ensure the code in `style.css` compliant with W3C standards.
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

## **5.1.5 JS Validation**

## **5.1.6 WAVE Validation**