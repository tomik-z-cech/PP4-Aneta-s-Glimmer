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
   - Use command `black --linelength 79 DIRECTORY_NAME/` to format `*.py` files in the selected directory or use `black --linelength 79 .` to format all files
   - See in the terminal window result of this operation *( Appendix 51 )*
   - Double check the results in `CI Python Linter` by copying and pasting the Python code as black doesn't wrap lines of comments. See result on the right hand side of the input field *( Appendix 52 )*
- **Results :**
The only file failing the PEP8 standard is `glimmer/settings.py` due length of lines of module names.

| Directory      | File            | Errors | Warnings | Result                                                   |
| -------------- | --------------- | ------ | -------- | -------------------------------------------------------- |
| administrator  | \`admin.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| administrator  | \`urls.py\`     | 0      | 0        | <span style="color:green;">PASS</span>                   |
| administrator  | \`views.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| artists        | \`admin.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| artists        | \`models.py\`   | 0      | 0        | <span style="color:green;">PASS</span>                   |
| artists        | \`urls.py\`     | 0      | 0        | <span style="color:green;">PASS</span>                   |
| artists        | \`views.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| bookings       | \`admin.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| bookings       | \`forms.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| bookings       | \`models.py\`   | 0      | 0        | <span style="color:green;">PASS</span>                   |
| bookings       | \`urls.py\`     | 0      | 0        | <span style="color:green;">PASS</span>                   |
| bookings       | \`views.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| landing        | \`admin.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| landing        | \`forms.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| landing        | \`urls.py\`     | 0      | 0        | <span style="color:green;">PASS</span>                   |
| landing        | \`views.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| news           | \`admin.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| news           | \`forms.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| news           | \`models.py\`   | 0      | 0        | <span style="color:green;">PASS</span>                   |
| news           | \`urls.py\`     | 0      | 0        | <span style="color:green;">PASS</span>                   |
| news           | \`views.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| profilemanager | \`admin.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| profilemanager | \`forms.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| profilemanager | \`models.py\`   | 0      | 0        | <span style="color:green;">PASS</span>                   |
| profilemanager | \`urls.py\`     | 0      | 0        | <span style="color:green;">PASS</span>                   |
| profilemanager | \`views.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| styles         | \`admin.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| styles         | \`forms.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| styles         | \`models.py\`   | 0      | 0        | <span style="color:green;">PASS</span>                   |
| styles         | \`urls.py\`     | 0      | 0        | <span style="color:green;">PASS</span>                   |
| styles         | \`views.py\`    | 0      | 0        | <span style="color:green;">PASS</span>                   |
| glimmer        | \`asgi.py\`     | 0      | 0        | <span style="color:green;">PASS</span>                   |
| glimmer        | \`settings.py\` | 6      | 0        | <span style="color:red;">FAIL</span> \*( Appendix 53 )\* |
| glimmer        | \`urls.py\`     | 0      | 0        | <span style="color:green;">PASS</span>                   |
| glimmer        | \`wsgi.py\`     | 0      | 0        | <span style="color:green;">PASS</span>                   |

*Appendix 51 - Black result message*

![Black result message](/docs/validation/black.png)

*Appendix 52 - CI Python Linter result message*

![CI Python Linter result message](/docs/validation/ci_linter.png)

*Appendix 53 - `glimmer/settings.py`*

![`glimmer/settings.py`](/docs/validation/settings_pep8.png)

## **5.1.3. HTML Validation**

## **5.1.4 CSS Validation**

## **5.1.5 JS Validation**

## **5.1.6 WAVE Validation**