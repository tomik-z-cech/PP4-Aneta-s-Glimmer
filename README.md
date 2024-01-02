# ***Aneta's Glimmer - Portfolio Project 4***
---
# **1. Key project information**

- **Description :** This Portfolio Project 4 website called **Aneta's Glimmer** is a site of imaginary finger nail salon that offers many services, offers news in form of blog from the finger nail art and allows user to manage their own booking. **Aneta's Glimmer** site is presenting to its visitors with variety of details and functions from booking appointment, manage appointments and blog style functions.
- **Key project goal :** To familiarize visitors of this page with **Aneta's Glimmer** salon, give them hint of the menus and ability to manage bookings online.
- **Audience :** There's no age or any other limit to audience of this page. Target audience are adults that are using search engines for finger nail art studios or salons.
- **Live version :** Live version of **Aneta's Glimmer** page can be viewed at [https://anetas-glimmer-05b4a3ceb113.herokuapp.com/](https://anetas-glimmer-05b4a3ceb113.herokuapp.com/).
- **Developer :** [Tomas Kubancik](https://github.com/tomik-z-cech/)

![Mockup](/docs/mockup.png)

---

# **2. Table of content**

- [1. Key project information](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#1key-project-information)
- [2. Table of content](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
- [3. User Experience (UX)](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [3.1. The Strategy Plane](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [3.1.1 The Idea](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [3.1.2 The Ideal User](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [3.1.3 Site Goals](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [3.1.4 Epics](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [3.1.5 User stories](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [3.2. The Scope Plane](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [3.2.1. Features to be implemented](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [3.3. The Structure Plane](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [3.3.1 Site Maps](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [3.3.2 Database Schemas](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [3.4. The Skeleton Plane](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [3.4.1 Wire-frames](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [3.5. The Surface Plane](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [3.5.1 Logo](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [3.5.2 Color pallette](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [3.5.1 Fonts](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)


---

# **3. User Experience (UX)**

## **3.1. The Strategy Plane**

### **3.1.1 The Idea**
- The intention of **Aneta's Glimmer** site is to be friendly booking system, where users can mainly manage their bookings. Besides that, users can browse the News from nail art field, browse available styles, leave likes and comments for both and also read details about team members.

### **3.1.2 The Ideal User**

The target audience are individuals or groups that are seeking inspiration in finger nail modelling, looking for new trends, likes to see opinion of others in the same thread.

- Ideal user likes nail art
- Ideal user visits nail salons
- Ideal user likes to manage own bookings
- Ideal user likes to explore new trends and ideas
- Ideal user likes to share their opinion in form if likes and comments

### **3.1.3 Site Goals**

- Offer users ability of managing their own bookings
- Offer users ability of reading news, liking and commenting
- Create a place where users can share opinions
- Offer users inspiration in nail art field

### **3.1.4 Epics**

As a thought process of the strategy plane, 12 epics were created and utilized. Please see below the detail list of epics with links, or a link to the project's [Kanban Board](https://github.com/users/tomik-z-cech/projects/1/views/1) *(appendix 1)*. Those Epics were further sliced into 49 USER STORIES.

*Appendix 1 - Kanban Board*

![Kanban Board](/docs/kanban.png)

- EPIC 1 : Environment configuration - [issue #4](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/4)
- EPIC 2 : Database models - [issue #12](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/12)
- EPIC 3 : User Authentication and Authorization - [issue #16](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/16)
- EPIC 4 : User Details Change - [issue #20](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/20)
- EPIC 5 : News, News Commenting & Liking - [issue #24](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/24)
- EPIC 6 : Styles Functions - [issue #31](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/31)
- EPIC 7 : Booking Management - [issue #38](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/38)
- EPIC 8 : Search Bar - [issue #51](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/51)
- EPIC 9 : Business owner objectives - [issue #54](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/54)
- EPIC 10 : Styling and design of UI - [issue #70](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/70)
- EPIC 11 : Testing and Validation - [issue #74](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/74)
- EPIC 12 : Custom Admin interface - [issue #79](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/79)

### **3.1.5 User stories**

49 User stories were created based on the Epics. Each user story uses the MoSCoW prioritization technique. Each user story was also estimated for relative effort required to implement satisfactory result of acceptance criteria. My Story points are using a sequence inspired by the Fibonacci numbers (1, 2, 3, 5, 8, 13, etc.). This reflects the uncertainty and variability in estimating larger tasks. The idea was to easy distinguish the initial size of user story using this non-linear sequence. Each user story on the [Kanban Board](https://github.com/users/tomik-z-cech/projects/1/views/1) was given 2 labels (MoSCoW and Story Points).


**MoSCoW prioritization technique stands for**:

**Must-Have**: Critical requirements that must be implemented for the project to be considered successful.

**Should-Have**: Important requirements that are not critical but add significant value.

**Could-Haves**: Desirable features that would be nice to have but are not crucial.

**Won't-Have**: Features that are explicitly excluded from the project scope.

The **total** Story Points in the project is 129.
- **Must-Have** : 78 story points
- **Should-Have** : 28 story points
- **Could-Have** : 10 story points
- **Wont-Have** : 13 story points

### List of user stories sorted by Epic :

<details>
<summary>
View User Stories for EPIC 1 : Environment configuration
</summary>

| Issue                                                               | Title                                  | User Story                                                                                                                 |
| ------------------------------------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [# 1](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/1) | USER STORY : Set up GiHub repository   | As a Developer, I need to set-up a repository on GitHub platform to be able to have control over versions of project.      |
| [# 2](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/2) | USER STORY : Create working Django app | As a Developer, I need to install all dependencies, correctly set settings.py and create working app in local environment. |
| [# 3](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/3) | USER STORY : Deploy to Heroku          | As a Developer I need to create a working Heroku deployment.                                                              |

</details>

<details>
<summary>
View User Stories for EPIC 2 : Database models
</summary>

| Issue                                                                 | Title                                                    | User Story                                                                                                                                                  |
| --------------------------------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [# 13](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/13) | USER STORY : Define Database Schema and create sub apps. | As a Developer, I need to create database schema that fits the purpose of the project and also create all the modular apps that will be used in the project. |
| [# 14](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/14) | USER STORY : Create database relationships               | As a Developer, I need to define relationships between models and import the relationships into working apps models.                                         |
| [# 15](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/15) | USER STORY : Implement Data Validation in Models         | As a Developer, I need implement data validation rules within Glimmer database models.                                                                      |

</details>

<details>
<summary>
View User Stories for EPIC 3 : User Authentication and Authorization
</summary>

| Issue                                                                 | Title                                       | User Story                                                                                       |
| --------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| [# 17](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/17) | USER STORY : Implement user registration    | As a Site User I am able to register to create new account and to select username and password. |
| [# 18](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/18) | USER STORY : Log In                         | As a Site User I am able to Log In to see registered user section.                               |
| [# 19](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/19) | USER-STORY : Reset my password if forgotten | As a Site User I am able to Reset My Password to change my password if forgotten.                |
| [# 48](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/48) | USER STORY : Log out                        | As a Site User, I am able to log out to leave the site functions for registered users.           |

</details>
<details>
<summary>
View User Stories for EPIC 4 : User Details Change
</summary>

| Issue                                                                 | Title                                                          | User Story                                                                                |
| --------------------------------------------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| [# 21](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/21) | USER STORY : Opt In/Out for Newsletter                         | As a Site User I can Opt In/Out for Newsletter to be able to change my preferences.       |
| [# 22](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/22) | USER STORY : Change Details (Phone Number, Email Address, etc.) | As a Site User I can Update My Detail to be able to manage my account in case of changes. |
| [# 23](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/23) | USER STORY : Delete my account                                 | As a Site User I can Delete My Account to be able to opt out from all services.           |

</details>
<details>
<summary>
View User Stories for 5 : News, News Commenting & Liking
</summary>

| Issue                                                                 | Title                                            | User Story                                                                               |
| --------------------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| [# 25](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/25) | USER STORY : See News Highlights on landing page | As a Site User I can See the News Highlights to see three newest news posts.             |
| [# 26](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/26) | USER STORY : See list of all News & Details      | As a Site User I can Visit Page with all News to be able to see all News.                 |
| [# 27](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/27) | USER STORY : Like/Unlike News                    | As a Site User I can Like or Unlike News Post to highlight the News Post as interesting. |
| [# 28](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/28) | USER STORY : Comment on News                     | As a Site User I can Comment on News Post to share my opinion.                           |
| [# 29](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/29) | USER STORY : See other users Comments            | As a Site User I can see other comments on News Posts to read other Users opinions.      |
| [# 30](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/30) | USER STORY : See who else liked                  | As a Site User I can see who else liked News Posts to see who else has the same opinion. |

</details>
<details>
<summary>
View User Stories for EPIC 6 : Styles Functions
</summary>

| Issue                                                                 | Title                                                                  | User Story                                                                                                   |
| --------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| [# 32](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/32) | USER STORY : List of Styles                                            | As a Site User I can See list of available styles to be able to choose one to see details.                   |
| [# 33](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/33) | USER STORY : Styles Details                                            | As a Site User I can See Style details to see description and what artist does this particular style.        |
| [# 34](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/34) | USER STORY : Like / Unlike Styles                                      | As a Site User I can Like / Unlike particular Style to express my opinion.                                   |
| [# 35](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/35) | USER STORY : See who else likes the particular Style                   | As a Site User I can see who else liked the particular style to see who else has same opinion.               |
| [# 36](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/36) | USER STORY : Mark / Un-mark Styles as "Wan't to try"                    | As a Site User I can Mark / Un-mark particular style to express my interest.                                  |
| [# 37](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/37) | USER STORY : See who else marked the particular style as "Want to try" | As a Site User I can see who else marked particular style as "Want to try to see who else has same interests. |

</details>
<details>
<summary>
View User Stories for EPIC 7 : Booking Management
</summary>

| Issue                                                                 | Title                                                      | User Story                                                                                                 |
| --------------------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| [# 39](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/39) | USER STORY : Create a booking                              | As a Site User I can Create new booking and to be able to choose date, time and artist.                    |
| [# 40](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/40) | USER STORY : See my bookings                               | As a Site User I can See all my bookings to be able to keep record of them.                                |
| [# 41](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/41) | USER STORY : Update my bookings                            | As a Site User I can Update any of my future bookings to change details.                                   |
| [# 42](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/42) | USER STORY : Delete my bookings                            | As a Site User I can Delete any of my future bookings to cancel the booking.                               |
| [# 43](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/43) | USER STORY : Leave review after booking finished           | As a Site User I can leave review to let the others know about my satisfaction.                            |
| [# 44](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/44) | USER STORY : Get confirmation of my booking being approved | As a Site User I get confirmation email when my booking is approved to be sure the booking is going ahead. |

</details>
<details>
<summary>
View User Stories for EPIC 8 : Search Bar
</summary>

| Issue                                                                 | Title                                          | User Story                                                                                                              |
| --------------------------------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [# 52](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/52) | USER STORY : Create search bar on landing page | As a Site User I am able to use search function through Artists, Styles and News to quickly find what am I looking for. |
| [# 53](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/53) | USER STORY : Provide search results            | As a Site User I can see search result to easily navigate through them.                                                 |

</details>
<details>
<summary>
View User Stories for EPIC 9 : Business owner objectives
</summary>

| Issue                                                                 | Title                                   | User Story                                                                                                                                 |
| --------------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| [# 55](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/55) | USER STORY : Delete user                | As a Site Admin, I can delete user accounts that are no longer in use to make sure my database of clients is up to date.                   |
| [# 56](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/56) | USER STORY : Manage news                | As a Site Admin, I can add news posts to keep content up to date.                                                                          |
| [# 57](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/57) | USER STORY : Manage available styles    | As a Site Admin, I can add available styles to keep content up to date.                                                                    |
| [# 58](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/58) | USER STORY : Manage artists             | As a Site Admin, I can add nail artists to keep list of employees up to date.                                                              |
| [# 59](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/59) | USER STORY : Approve comments           | As a Site Admin, I can approve comments to ensure no harmful content.                                                                      |
| [# 60](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/60) | USER STORY : Mark bookings as confirmed | As a Site Admin, I can mark bookings as confirmed to inform user of the progress.                                                          |
| [# 61](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/61) | USER STORY : Mark bookings as done      | As a Site Admin, I can mark bookings as done to inform user of the progress and allow user to rate.                                        |
| [# 62](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/62) | USER STORY : Last-minute bookings       | As a Site Admin, I need to provide users with "last-minute" bookings available to let them know how many slots are free the following day. |

</details>
<details>
<summary>
View User Stories for EPIC 10 : Styling and design of UI
</summary>

| Issue                                                                 | Title                             | User Story                                                                                                                 |
| --------------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [# 71](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/71) | USER STORY : Intuitive navigation | As a Site Developer, I need to insure easy navigation throughout the site.                                                 |
| [# 72](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/72) | USER STORY : Color scheme         | As a Site Developer, I need to insure same color scheme throughout the site                                                |
| [# 73](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/73) | USER STORY : WAVE compatibility   | As a Site Developer, I need to insure that site can be easily navigated using page readers, so it doesn't have WAVE issues. |

</details>
<details>
<summary>
View User Stories for EPIC 11 : Testing and Validation
</summary>

| Issue                                                                 | Title                            | User Story                                                                        |
| --------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- |
| [# 75](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/75) | USER STORY : W3C HTML validation | As a Site Developer, I need to ensure \*.html files do pass the W3C validation.   |
| [# 76](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/76) | USER STORY : W3C CSS validation  | As a Site Developer, I need to ensure style.css file do pass the W3C validation.  |
| [# 77](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/77) | USER STORY : JS validation       | As a Site Developer, I need to ensure \*.js files do pass the JS Lint validation. |
| [# 78](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/78) | USER STORY : PEP8 validation     | As a Site Developer, I need to ensure \*.py file do pass the PEP8 validation.     |

</details>
<details>
<summary>
View User Stories for EPIC 12 : Custom Admin interface
</summary>

| Issue                                                                 | Title                                                                    | User Story                                                                                                         |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| [# 80](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/80) | USER STORY : Admin interface that copies functions of Django Admin Suite | As a Site Developer I need to come up with custom admin interface that ensures all functions of Django Admin Suite, |

</details>


---


## **3.2. The Scope Plane**

After decided on the strategy, the scope plane was carefully created.

### 3.2.1. Features to be implemented

- **User Authentication** : Users can Register, Profile pages where users can manage their information and preferences and delete their account (CRUD)

- **News** : Users can see news with titles, content, and images.

- **Styles** : Users can see styles with titles, content, and images.

- **Team** : Users can see team members with names, details, and profile pictures.

- **Liking and Commenting** : Users can Like News Posts and Like/Mark as to Try Available Styles so they can express their interest.Users can also comment on both News Posts and Available Styles to allow them to engage in discussions.

- **Bookings** : Users can create, view, edit or cancel their own bookings (CRUD).

- **Search** : Search bar for users is provided on landing page so users can find specific News Posts, Styles or Team members.

- **Notifications** : Notifications for new , edited and cancelled bookings need to be provided to the user both on screen and via email.

## **3.3. The Structure Plane**

### 3.3.1. Site Maps

The following site-maps show how the site is structured to logged in users *( appendix 2 )* and not logged in users *( appendix 3 )*.

*Appendix 2 - Site Map - Logged In*

![Site Map - Logged In](/docs/sitemap-logged.png)

*Appendix 3 - Site Map - Not Logged In*

![Site Map - Not Logged In](/docs/sitemap-notlogged.png)

### 3.3.2. Database Schemas

Following schemas show intended database structure *( appendix 4 )* and the actual database structure generated by DBeaver *( Appendix 5 )*.

*Appendix 4 - Initial DB schema*

![Site Map - Logged In](/docs/db-schema-sqldraw.png)

*Appendix 5 - DBeaver DB schema and relationships*

![Site Map - Not Logged In](/docs/db-schema-dbeaver.png)

## **3.4. The Skeleton Plane**

### 3.4.1. Wire-frames

- **Header and Footer** : Header and footer is established on every single page. Header is sticky and stays in position. Footer is displayed at the very bottom of each page so it doesn't cover any content *( Appendix 6 )*.

*Appendix 6 - Header and Footer Wire-frame*

![Header and Footer Wire-frame](/docs/wireframes/header-footer.png)

- **Landing page** : Provides user with clear understanding of what the page is about. User is also provided with 3 newest News Post along with statistics of top artists and top styles by like and "try"  *( Appendix 7 )*.

*Appendix 7 - Landing Page Wire-frame*

![Landing Page Wire-frame](/docs/wireframes/landing.png)

- **News page** : Provides user with all News Posts published along with name of creator, date created and a snippet of News Post body. Also information of amount of likes and comments is provided to both logged in and not logged in users *( Appendix 8 )*.

*Appendix 8 - News Page Wire-frame*

![News Page Wire-frame](/docs/wireframes/news.png)

- **News Detail page** : Provides user with selected News Post along with name of creator, date created and full News Post body. User sees likes and amount of comments. Logged in user has ability to comment and like. *( Appendix 9 )*.

*Appendix 9 - News Detail Page Wire-frame*

![News Detail Page Wire-frame](/docs/wireframes/d-news.png)

- **Styles page** : Provides user with all Styles Available along with name of style, image and artists that excel in this style. Also information of amount of likes, tries and comments is provided to both logged in and not logged in users *( Appendix 10 )*.

*Appendix 10 - Styles Wire-frame*

![Styles Wire-frame](/docs/wireframes/styles.png)

- **Style Detail page** : Provides user with details of selected Style along with names of artists that excel in this style, other details and users have ability to create a booking from here. User sees likes, tries and amount of comments. Logged in user has ability to comment like and mark to try. *( Appendix 11 )*.

*Appendix 11 - Style Detail Page Wire-frame*

![Style Detail Page Wire-frame](/docs/wireframes/d-styles.png)

- **Team page** : Provides user with all Team members list along with name of artist, profile picture and artist's rating.*( Appendix 12 )*.

*Appendix 12 - Team Wire-frame*

![Team Wire-frame](/docs/wireframes/artists.png)

- **Team Member Detail page** : Provides user with details of selected team member, their bio, profile picture and list of styles this artist excels in along with option to create a booking *( Appendix 13 )*.

*Appendix 13 - Team Member Detail Page Wire-frame*

![Team Member Detail Page Wire-frame](/docs/wireframes/d-artists.png)

- **My Bookings page** : Provides user with information of their pending, confirmed and past bookings. Pending and confirmed bookings can be edited, past bookings can be rated. User is also provided with amount of free slots for today and tomorrow for each artist. *( Appendix 14 )*.

*Appendix 14 - My Bookings Wire-frame*

![My Bookings Wire-frame](/docs/wireframes/bookings.png)

- **New Booking/Edit Booking Forms** : Provides user with selection of booked style, booked artist, date and time of booking. Logic is used so user can only book artist that excels in style selected, also bookings of other users are taken into consideration to ensure multiple bookings fo same date/time can't be submitted. *( Appendix 15 )*.

*Appendix 15 - New/Edit Booking Form Wire-frame*

![New/Edit Booking Form Wire-frame](/docs/wireframes/bookings-form.png)

- **My Profile Page** : Gives user the ability to change their details and preferences. The form is pre-populated with existing details. It also gives the user ability to delete their account entirely. *( Appendix 16 )*.

*Appendix 16 - My Profile Page*

![My Profile Page](/docs/wireframes/profile.png)

- **Search Results Page** : Provides the user with results of their search query in three groups. News Posts, Styles and Artists. user has the option to search again from the same page. *( Appendix 17 )*.

*Appendix 17 - Search Results Page*

![Search Results Page](/docs/wireframes/search-results.png)

- **Forms** : Forms do interact with user. They are designed to be clear and to the point, always in center of the screen. *( Appendix 18 )*.

*Appendix 18 - Forms*

![Forms](/docs/wireframes/forms.png)

## **3.5. The Surface Plane**

Once the Strategy, Scope, Structure and Skeleton Planes were in place, it was time to work on the Surface Plane (Design).

### 3.5.1. Logo

To create the logo, site called [Looka](https://looka.com/) was used. Few ideas were presented to the site owner and one of the logos was picked *( Appendix 19 )*

*Appendix 19 - Logo*

![Logo](/docs/email_logo.png)

### 3.5.2. Color pallette

Based on the colors of the logo, rest of the colors were picked using the [Adobe Color Wheel](https://color.adobe.com/create/color-wheel), following colors were picked into the color pallette *( Appendix 20 )*. As some of the colors needed to be opaque, following CSS variables were established *( Appendix 21 )*.

*Appendix 20 - Color pallette*

![Color pallette](/docs/color-palette.png)

*Appendix 21 - Color variables*

![Color variables](/docs/color-vars.png)

### 3.5.3. Fonts

[Google Fonts](https://fonts.google.com/) site was used to pick the best typography style. The most importance was given to balance between style and readability. As a developer I needed to ensure that all text is displayed clear.

Two fonts were picked and saved in CSS vars *( Appendix 24)* :
 - Permanent Marker (Sans Serif fallback) -  *( Appendix 22 )*
 - Sriracha (Sans Serif fallback) - *( Appendix 23 )*

*Appendix 22 - Permanent Marker Font*

![Permanent Marker Font](/docs/marker.png)

*Appendix 23 - Sriracha Font*

![Sriracha Font](/docs/sriracha.png)

*Appendix 24 - Font Variables*

![Font Variables](/docs/font-vars.png)

### 3.5.4. Icons and pictures

Icons were downloaded from [Flaticon](https://www.flaticon.com/icons). Majority of icons are free to download and use under the their T&C license. Icons were user for like, try, comments and rating functions in this project.

Site called [Freepik](https://www.freepik.com/) was used to download images used in this project. The site offers massive amounts of imagery that is free to download and use under their T&C license. Images from [Freepik](https://www.freepik.com/) were mainly used as background images.

Profile pictures of non-existing artists in this project were created by AI called [Canva](https://www.canva.com/). Reason for this was a need of profile pictures of artists with certain parameters and they were very difficult to find under free license.

---

# **4. Features**



---


