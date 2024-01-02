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
- [3. Features](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [4.1. Features used in every HTML template](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.1.1 Header](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.1.2 Footer](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.1.3 Favicon](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.1.4 Error Pages](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.1.5 Scrollbar](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [4.2. Main Content](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.2.1 Landing Page](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.2.2 News Page](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.2.3 News Detail Page](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.2.4 Style Page](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.2.5 Style Detail Page](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.2.6 Team Page](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.2.7 Artist Detail Page](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.2.8 My Bookings Page](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.2.9 Booking Forms](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.2.10 My Details Page](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.2.11 Search Results Page](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [4.2.12 Forms](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [4.3. Future Features](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
- [5. Validation, Testing & Bugs](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [5.1. Validation](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [5.2. Testing](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [5.3. Bugs](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
- [6. Deployment](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [6.1. Transfer of progress from IDE](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [6.2. Offline cloning](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [6.3. Deployment Prerequisites](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [6.3.1 Gmail](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [6.3.2 ElephantSQL](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [6.3.3 Cloudinary](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
    - [6.3.4 Settings.py & file-tree](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [6.4. Heroku Deployment](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
- [7. Technologies & Credits](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [7.1. Technologies used to develop and deploy this project](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [7.2. Requirements.txt](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
  - [7.3. Credits](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer#2table-of-content)
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

## **4.1. Features used in every HTML template**

### **4.1.1 Header**
- Header contains a Logo section *( Appendix 25 )* which is also used as a link to Home page `{% url 'home' %}` in the left top corner and Menu section *( Appendix 26 )* for easy navigation through all the pages. Menu is designed to change to "hamburger menu" *( Appendix 27 )* when the resolution changes to less than 1200 pixels in width.
- Header is designed to have fixed position on top of page `top: 0px` through all browsing.
- Header is designed to cover full width `width: 100%` of the browsing window.
- This will allow user to navigate through the pages and to navigate back to home page when click on logo.
- Header appears same on all devices.
- Header extends `base.html` in block `{% include 'header.html' %}`

*Appendix 25 - Logo*

![Logo](/docs/email_logo.png)

*Appendix 26 - Menu*

![Menu](/docs/features/menu.png)

*Appendix 27 - Hamburger Menu*

![Menu](/docs/features/hamburger.png)


### **4.1.2. Footer**

- Footer  *( Appendix 28 )* is designed to reveal basic contact details of **Aneta's Glimmer** on the left hand side, phone number and email address are constructed to be clickable links that are very useful especially for mobile phone users. Right-hand side of footer is designed to bring the user to Facebook via link that opens in new browser tab.
- Footer is designed to cover full width `width: 100%` of the browsing window.
- This will allow user to open phone app (dial the number directly), send e-mail (open e-mail application on phone/tablet) and open Facebook link in new window.
- Footer appears same on all devices.
- Footer extends `base.html` in block `{% include 'footer.html' %}`

*Appendix 28 - Footer*

![Footer](/docs/features/footer.png)

### **4.1.3. Favicon**

- Every template in this project is equipped with Favicon. This is to ease navigation for user in case of more tabs opened. The logo was selected as Favicon *( Appendix 29)*. 

*Appendix 29 - Favicon*

![Favicon](/docs/features/favicon.png)

### **4.1.4. Error Pages**

- This project is designed to have custom error pages. In case of user clicks on broken link, submits action that isn't supported or tries to reach certain view without permission, then user isn't completely "cut off" from browsing, instead an error page with header and footer appears and user is informed of the situation.

- The following custom error pages were created :
- - 403 - Received when user attempts to access a web resource for which they lack the necessary permissions. *( Appendix 30 )*
- - 404 - Encountered when the requested web resource by user is not found on the server. *( Appendix 31 )*
- - 500 - Displayed when the web server encounters an internal error while processing the request. *( Appendix 32 )*

*Appendix 30 - 403.html*

![403.html](/docs/features/403.png)

*Appendix 31 - 404.html*

![404.html](/docs/features/404.png)

*Appendix 32 - 500.html*

![500.html](/docs/features/500.png)

### **4.1.5. Scroll bar**
- Custom scroll bar was used to fit within the color theme within the project.

*Appendix 33 - Scroll bar*

![Scrollbar](/docs/features/scrollbar.png)


## **4.2. Main Content**

### **4.2.1. Landing Page**

- **App :** `landing`
- **Template File :** `index.html` - extends `base.html`
- **User :** Provides user with clear understanding of what the page is about. User is also provided with 3 newest News Post along with statistics of top artists and top styles by like and "try"  *( Appendix 34 )*.

*Appendix 34 - Landing Page*

![Landing Page](/docs/features/landing.png)

### **4.2.2. News Page**

- **App :** `news`
- **Template File :** `all_news.html` - extends `base.html`
- **User :** Provides user with all News Posts published along with name of creator, date created and a snippet of News Post body. Also information of amount of likes and comments is provided to both logged in and not logged in users *( Appendix 35 )*.

*Appendix 35 - News Page*

![News Page](/docs/features/news.png)

### **4.2.3. News Detail Page**

- **App :** `news`
- **Template File :** `news_detail.html` - extends `base.html`
- **User :** Provides user with selected News Post along with name of creator, date created and full News Post body *( Appendix 36 )*. User sees likes and amount of comments. Logged in user has ability to comment and like. *( Appendix 37 )*.

*Appendix 36 - News Detail Page*

![News Detail Page](/docs/features/d-news.png)

*Appendix 36 - News Detail Page - comments & likes*

![News Detail Page - Comments](/docs/features/cl-news.png)

### **4.2.4. Styles Page**

- **App :** `styles`
- **Template File :** `styles.html` - extends `base.html`
- **User :** Provides user with all Styles Available along with name of style, image and artists that excel in this style. Also information of amount of likes, tries and comments is provided to both logged in and not logged in users *( Appendix 37 )*.

*Appendix 37 - Styles Page*

![Styles Page](/docs/features/styles.png)

### **4.2.5. Styles Detail Page**

- **App :** `styles`
- **Template File :** `style_detail.html` - extends `base.html`
- **User :** Provides user with details of selected Style along with names of artists that excel in this style, other details and users have ability to create a booking from here *( Appendix 38 )*. User sees likes, tries and amount of comments. Logged in user has ability to comment like and mark to try *( Appendix 39 )*.

*Appendix 38 - Style Detail Page*

![Style Detail Page](/docs/features/d-styles.png)

*Appendix 39 - Style Detail Page - comments, likes & tries*

![Style Detail Page - Comments](/docs/features/cl-styles.png)

### **4.2.6. Team Page**

- **App :** `artists`
- **Template File :** `artists.html` - extends `base.html`
- **User :** Provides user with all Team members list along with name of artist, profile picture and artist's rating.*( Appendix 40 )*.

*Appendix 40 - Team Page*

![Team Page](/docs/features/team.png)

### **4.2.7. Artist Detail Page**

- **App :** `artists`
- **Template File :** `artist_detail.html` - extends `base.html`
- **User :** Provides user with details of selected team member, their bio, profile picture and list of styles this artist excels in along with option to create a booking *( Appendix 41 )*.

*Appendix 41 - Artist Detail Page*

![Artist Detail Page](/docs/features/d-team.png)

### **4.2.8. My Bookings Page**

- **App :** `bookings`
- **Template File :** `bookings.html` - extends `base.html`
- **User :** Provides user with information of their pending, confirmed and past bookings. Pending and confirmed bookings can be edited, past bookings can be rated *( Appendix 42 )*. User is also provided with amount of free slots for today and tomorrow for each artist *( Appendix 43 )*.

*Appendix 42 - My Bookings Page*

![My Bookings Page](/docs/features/bookings.png)

*Appendix 43 - Last Minute Bookings*

![Last Minute Bookings](/docs/features/last-minute.png)

### **4.2.9. Bookings Forms**

- **App :** `bookings`
- **Template File :** `new_booking.html` and `edit_booking.html` - extends `base.html`
- **User :** Provides user with selection of booked style, booked artist, date and time of booking. Logic is used so user can only book artist that excels in style selected, also bookings of other users are taken into consideration to ensure multiple bookings fo same date/time can't be submitted *( Appendix 44 )*.

*Appendix 44 - Bookings Forms*

![Booking Forms](/docs/features/booking-form.png)

### **4.2.10. My Profile Page**

- **App :** `profilemanager`
- **Template File :** `my_details.html` - extends `base.html`
- **User :** Gives user the ability to change their details and preferences. The form is pre-populated with existing details. It also gives the user ability to delete their account entirely. *( Appendix 45 )*.

*Appendix 45 - My Details Page*

![My Details Page](/docs/features/my_profile.png)

### **4.2.11. Search Results Page**

- **App :** `landing`
- **Template File :** `search_results.html` - extends `base.html`
- **User :** Provides the user with results of their search query in three groups. News Posts, Styles and Artists. user has the option to search again from the same page *( Appendix 46 )*.

*Appendix 46 - Search Results Page*

![Search Results Page](/docs/features/results.png)

### **4.2.12. Forms**

- **App :** `AllAuth` extension
- **Template File :** `*.html` in `./templates/account` - extends `base.html`
- **User :** Forms do interact with user. They are designed to be clear and to the point, always in center of the screen. *( Appendix 47 )*.

*Appendix 47 - Forms*

![Forms](/docs/features/form.png)

## **4.3. Future Features**

This project could be significantly improved by adding more features this could include :

- Toggle between light mode and dark mode (currently working on)
- Custom Admin interface to fit within the style of project (currently working on)
- Ability to Login with other page credentials (Google, Facebook)
- Virtual Try On function
- Messaging between users
- E-Commerce section 


---

# **5. Validation, Testing & Bugs**

## **5.1. Validation**

Validation is documented separately in [validation.md](/docs/validation.md) file.

## **5.2. Testing**

Testing is documented separately in [testing.md](/docs/testing.md) file.

## **5.3. Bugs**

Bugs are documented separately in [bugs.md](/docs/bugs.md) file.

---

# **6. Deployment**

## **6.1. Transfer of progress from IDE**

- **Task :** To ensure regular commitments are done to avoid any data/progress loss.
- **Method :** 
   - commands `git add [filename]` was used to add specific file to staging area, alternatively command `git add .` was used to add all changed files to staging area
   - command `git commit -m "[commit description]"` was used to add commitments into queue
   - command `git push` was used to push all commitments to remote repository on GitHub

## **6.2. Offline cloning**

- **Task :** To use repository on local machine.
- **Method :** 
  - Navigate to GitHub and follow `Code -> HTTPS -> Copy button` . after those steps open your local coding environment and type `git clone [copied link]`.

## **6.3. Deployment Prerequisites**

### **6.3.1. Gmail**

- **Task :** Obtain GMail username and app key (password) - GMAIL SMTP to be used as mailing client.
- **Method :** 
  - Navigate to `https://accounts.google.com/` and follow all steps for registering new email address
  - Login to google with newly created email address and password.
  - Navigate to `https://accounts.google.com/` once again
  - Select `Security > Signing in to Google > 2-Step Verification > App Passwords`
  - Enter a name of the app password and select `Generate`
  - You will get app password in format `xxxx xxxx xxxx xxxx`
  - Update `settings.py` in the project directory

### **6.3.2. ElephantSQL**

- **Task :** Obtain database URL to be used as project's database.
- **Method :** 
  - Select one of the DB providers, I did use [ElephantQSL](https://www.elephantsql.com/)
  - Navigate to `https://www.elephantsql.com/` and follow all steps for registering new account
  - Login to ElephantSQL with newly created account credentials
  - Navigate to `+ Create New Instance`
  - Select `Name, Plan and Region`
  - Confirm the instance by pressing `Create Instance`
  - Obtain database URL in format `postgres://NAME:PASSKEY@flora.db.elephantsql.com/NAME`
  - Update `settings.py` in the project directory

### **6.3.3. Cloudinary**

- **Task :** Obtain Cloudinary URL to be used as project's static storage
- **Method :** 
  - Select one of the static storage providers, I did use [Cloudinary](https://console.cloudinary.com/)
  - Navigate to `https://console.cloudinary.com/` and follow all steps for registering new account
  - Login to Cloudinary with newly created account credentials
  - Navigate to `+ Add a new environment`
  - Confirm your selection
  - Obtain Cloudinary URL in format `cloudinary://USER:PASSKEY@ENVIRONMENT`
  - Update `settings.py` in the project directory

### **6.3.4. Settings.py & file-tree**

- **Task :** Prepare `settings.py` adn file-tree for deployment 
- **Method :** 
  - Create file `env.py` to keep all sensitive information in
  - See example of `env.py` file *( Appendix 48 )*
  - Add `env.py` into `.gitignore` file to ensure this fill won't be uploaded to GitHub
  - update `settings.py` with `import os`
  - for every secured variable add code `VARIABLE = os.environ.get("VARIABLE")`
  - ensure this process for Gmail, ElephantSQL, Cloudinary, DEBUG and Django Secret Key
  - update default database settings in `settings.py` with `
if "DATABASE_URL" in os.environ:
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }`
  - update default static settings in `settings.py` with `
  STATIC_URL = "/static/"
STATICFILES_STORAGE = "cloudinary_storage.storage.StaticHashedCloudinaryStorage"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")
MEDIA = "/media/"
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
  `
  - update email settings in `settings.py` with `EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True`
  - Migrate - your database models to ElephantSQL using `python manage.py migrate` command
  - Create directories `.\static` and `.\templates`
  - commit and push changes to GitHub 

*Appendix 48 - `env.py` file*

![env.py](/docs/env.png)

### **6.4. Deployment to Heroku**

- **Task :** To ensure users are able to view live version of **Aneta's Glimmer** project.
- **Method :** 
  - Register & Log In with heroku
  - Navigate to `New > Create New App`
  - Select Name of the app that is unique
  - Navigate to `Settings > Reveal Config Vars`
  - Add all variables from `env.py` to ConfigVars of Heroku App *( Appendix 49)*
  - Add variable pair `PORT:8000`
  - For the testing deployment add variable pair `COLLECT_STATIC:1`
  - Add the Heroku app URL into `ALLOWED HOSTS` in `settings.py`
  - In root create file name `Procfile` *( Appendix 50 )*
  - Navigate to `Deploy > GitHub > Connect`
  - Navigate to `Deploy > Deploy Branch`
  - Optionally, you can enable automatic deploys
  - See the deployment log - if the deployment was successful, you will be prompted with option to see live page  


*Appendix 49 - Heroku Config Vars*

![Heroku Config Vars](/docs/vars.png)

*Appendix 50 - Procfile*

![Procfile](/docs/procfile.png)

---

## **7. Technologies & Credits**

### 7.1. Technologies used to develop and deploy this project

- [**Django**](https://docs.djangoproject.com/en/5.0/) - main Framework of the project
- [**Python**](https://www.python.org/) - main BackEnd programming language of the project
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/HTML) - templates programming language of this project (FrontEnd)
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS) - styling the project via external CSS file `./static/css/style.css`
- [**Java Script**](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - dynamic templates programming language of this project (FrontEnd)
- [**jQuery**](https://api.jquery.com/) - API for JavaScript - dynamic templates programming language of this project (FrontEnd)
- [**Bootstrap v. 5.3**](https://getbootstrap.com/) - styling framework used in this project (FrontEnd)
- [**Heroku**](https://heroku.com) - to deploy this project
- [**Balsamiq**](https://balsamiq.com/support/) - to create wireframes
- [**Git**](https://git-scm.com/doc) - to make commitments of progress and push the results back to GitHub
- [**GitHub**](https://github.com/) - to keep the track of version control

### 7.3. Requirements.txt

Following modules were used in development of **Aneta's Glimmer** website :

 - `asgiref==3.7.2` - ASGI reference implementation, providing a specification for asynchronous web servers and applications
- `bleach==6.1.0` - sanitizing and cleaning HTML input
- `certifi==2023.7.22` - validating SSL certificates.
- `cffi==1.16.0` - way to call C functions from Python
- `charset-normalizer==3.3.2` - normalizing character encodings
- `cloudinary==1.36.0` - SDK for interacting with the Cloudinary media management service, facilitating image and video uploads
- `cryptography==41.0.5` - cryptographic recipes, including encryption, hashing, and key management
- `defusedxml==0.7.1` - library for safely parsing XML documents
- `dj-database-url==0.5.0` - utility for using database URLs in Django settings, simplifying database configuration
- `dj3-cloudinary-storage==0.0.6` - Django storage backend for Cloudinary, allowing seamless integration of Cloudinary as a storage solution for media files
- `Django==4.2.7` - framework that encourages rapid development and clean, pragmatic design
- `django-allauth==0.58.2` - package providing a set of authentication views, templates, and adapters for handling user registration, authentication, and account management
- `django-crispy-forms==1.14.0` - application that lets you easily build and customize crispy forms using Bootstrap styles
- `django-summernote==0.8.20.0` - application for integrating the Summernote WYSIWYG editor into Django admin forms
- `gunicorn==21.2.0` -  WSGI HTTP server for running Django applications in production
- `idna==3.4` - handling Internationalized Domain Names in Applications
- `oauthlib==3.2.2` - reusable Python library for implementing OAuth1 and OAuth2 providers
- `packaging==23.2` - core utility for Python packaging, providing functions for reading metadata, version parsing, and more
- `psycopg2==2.9.9` - PostgreSQL adapter for Python, allowing Python applications to interact with PostgreSQL databases
- `pycparser==2.21` - C parser in Python, used by cffi and other Python libraries to parse C code
- `PyJWT==2.8.0` - Python library for JSON encoding and decoding
- `python3-openid==3.2.0` - set of Python modules for OpenID authentication
- `pytz==2023.3.post1` - Python library for working with time zones
- `requests==2.31.0` -  Python library for making HTTP requests
- `requests-oauthlib==1.3.1` - Python library for OAuth1 and OAuth2 authentication
- `six==1.16.0` - Python 2 and 3 compatibility library
- `sqlparse==0.4.4` - library for parsing SQL statements
- `tzdata==2023.3` - Time zone database for Python
- `urllib3==2.1.0` - HTTP library for making requests in Python
- `webencodings==0.5.1` - library for working with HTML, XML, and other web encodings


### 7.3. Credits

- [**Daisy McGirr**](https://www.linkedin.com/in/daisy-mcgirr/?originalSubdomain=uk) - massive shout-out for keeping me in the right direction
- [**Alan Bushell**](https://www.linkedin.com/in/bushell23/) - thank you for all the support
- [**Magdalena Olajrz Photography**](https://www.facebook.com/profile.php?id=61553435195090) - massive credit for creating beautiful profile pictures
- [**Canva**](https://canva.com/) - used for creating non-existent profile images
- [**Looka**](https://looka.com/) - used for creating logo
- [**Adobe Color Wheel**](https://color.adobe.com/create/color-wheel) - used for picking the best color schema
- [**Google Fonts**](https://fonts.google.com/) - used for picking the best typography
- [**ElephantSQL**](https://www.elephantsql.com/) - used as a database storage
- [**Cloudinary**](https://console.cloudinary.com/) - used as a storage of static files
- [**FavIcon.io**](https://favicon.io/favicon-converter/) - used to compress favicon
- [**FreePik**](https://www.freepik.com/) - used as images database
- [**FlatIcon**](https://www.flaticon.com/icons) - used as icons database
- [**W3Schools**](https://www.w3schools.com/) - useful information and cheat sheets

