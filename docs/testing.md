# **5.2. Testing**

## **5.2.1. Table of Content - Testing**

- [5.2.1. Table of Content - Testing]()
- [5.2.2. User stories testing]()
- [5.2.3. Test Cases]()
- [5.2.4. Viewport Testing]()
- [5.2.5. Compatibility Testing]()

## **5.2.2. User stories testing**

| Epic 1                                                                |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------ |
| Issue                                                                 | Title                                                                    | User Story                                                                                                                                                  | Acceptance Criteria                                                                                                                                                                                          | Implementation                                                                                  | Final Commit                                                                                                   | Result |
| [# 1](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/1)   | USER STORY : Set up GiHub repository                                     | As a Developer, I need to set-up a repository on GitHub platform to be able to have control over versions of project.                                       | Working GitHub repository.                                                                                                                                                                                   | Not Applicable                                                                                  | N/A                                                                                                            | PASS   |
| [# 2](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/2)   | USER STORY : Create working Django app                                   | As a Developer, I need to install all dependencies, correctly set settings.py and create working app in local environment.                                  | All dependencies are installed, settings.py all set for local view and when project is ran locally, symbol of correctly set app is shown (rocket).                                                           | Not Applicable                                                                                  | [251e391](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/b606c30f5658763d01e6535726f4a4d92d4ce0e0) | PASS   |
| [# 3](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/3)   | USER STORY : Deploy to Heroku                                            | As a Developer I need to create a working Heroku deployement.                                                                                               | Working Heroku Deployment, when first deployed site accesed, it gives hint of correctly installed Django App (DEBUG = True). Create if statement in settings.py for DEBUG = False when deployed.             | Not Applicable                                                                                  | [cca2ec2](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/cca2ec26e07aaf9676052fa4a2db3a2be50f366a) | PASS   |
|                                                                       |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Epic 2                                                                |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Issue                                                                 | Title                                                                    | User Story                                                                                                                                                  | Acceptance Criteria                                                                                                                                                                                          | Implementation                                                                                  | Final Commit                                                                                                   | Result |
| [# 13](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/13) | USER STORY : Define Database Schema and create sub apps.                 | As a Developer, I need to create databse schema that fits the purpose of the project and also create all the modular apps that will be used in the project. | All Django apps are created and database schema in place to stick to.                                                                                                                                        | ( Appendix 68 )                                                                                 | [1202424](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/12024248cc53b3966b70377388984862bfc50c0b) | PASS   |
| [# 14](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/14) | USER STORY : Create database realtionships                               | As a Developer, I need to define relatinships between models and import the relationships into working apps models.                                         | All models are working with the relationships defined, all models that are related to other app models are linked via import statements.                                                                     | ( Appendix 69 )                                                                                 | [1202424](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/12024248cc53b3966b70377388984862bfc50c0b) | PASS   |
| [# 15](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/15) | USER STORY : Implement Data Validation in Models                         | As a Developer, I need implement data validation rules within Glimmer database models.                                                                      | All values insrted to database are the correct values and types, all applicable fileds are all set to be required or/and to be unique or/and nullable/not nullable.                                          | ( Appendix 70 )                                                                                 | [1202424](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/12024248cc53b3966b70377388984862bfc50c0b) | PASS   |
|                                                                       |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Epic 3                                                                |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Issue                                                                 | Title                                                                    | User Story                                                                                                                                                  | Acceptance Criteria                                                                                                                                                                                          | Implementation                                                                                  | Final Commit                                                                                                   | Result |
| [# 17](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/17) | USER STORY : Implement user registration                                 | As a Site User I am able to register to create new account and to select username and passsword.                                                            | Not registered user : When I visit the site then I am able to register, select free username and create valid password.                                                                                      | ( Appendix 71 )                                                                                 | [1ceb3cf](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/1ceb3cfbc0d845f7fc77cbbe23e657f34159fe16) | PASS   |
| [# 18](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/18) | USER STORY : Log In                                                      | As a Site User I am able to Log In to see registered user section.                                                                                          | 1.Registered user : When I visit the site then I am able to login via login link. 2.Not registered user : When I visit the site and trying to log in then I am given error message that user does not exist. | ( Appendix 72 ) and ( Appendix 73 )                                                             | [1ceb3cf](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/1ceb3cfbc0d845f7fc77cbbe23e657f34159fe16) | PASS   |
| [# 19](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/19) | USER-STORY : Reset my password if forgotten                              | As a Site User I am able to Reset My Password to change my password if forgotten.                                                                           | When I visit login page then I have the option to reset my password via provided link and email with reset link is sent to me.                                                                               | ( Appendix 74 )                                                                                 | [491242a](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/491242a472f186f75c15335507cfe605ef1d5dbd) | PASS   |
| [# 48](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/48) | USER STORY : Log out                                                     | As a Site User, I am able to log out to leave the site functions for registered users.                                                                      | 1.Registered user : When I am logged in then I am able to logout. 2.Not registered user : Don't have that option.                                                                                            | ( Appendix 75 )                                                                                 | [491242a](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/491242a472f186f75c15335507cfe605ef1d5dbd) | PASS   |
|                                                                       |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Epic 4                                                                |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Issue                                                                 | Title                                                                    | User Story                                                                                                                                                  | Acceptance Criteria                                                                                                                                                                                          | Implementation                                                                                  | Final Commit                                                                                                   | Result |
| [# 21](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/21) | USER STORY : Opt In/Out for Newsletter                                   | As a Site User I can Opt In/Out for Newsletter to be able to change my preferences.                                                                         | 1.Logged in user : When I navigate to "My Details" section then I can mark/unmark to receive marketing emails. 1.Not logged in user : Don't have that option as not logged in.                               | ( Appendix 76 )                                                                                 | [1f168ee](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/1f168eeb43330c02cb3ad79931c84002e46a5ede) | PASS   |
| [# 22](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/22) | USER STORY : Change Details (Phone Nuber, Email Address, etc.)           | As a Site User I can Update My Detail to be able to manage my account in case of changes.                                                                   | 1\. Logged in user : When I login then I can clearly navigate to "My Details" section where I can change my details. 2. Not logged in user : Don't have that option as not logged in.                        | ( Appendix 76 )                                                                                 | [1f168ee](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/1f168eeb43330c02cb3ad79931c84002e46a5ede) | PASS   |
| [# 23](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/23) | USER STORY : Delete my account                                           | As a Site User I can Delete My Account to be able to opt out from all services.                                                                             | 1\. Logged in user : When I navigate to "my details" then I have the option of delete my account entirely.2. Not logged in user : Don't have that option as not logged in.                                   | ( Appendix 76 ) and ( Appendix 77 )                                                             | [1f168ee](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/1f168eeb43330c02cb3ad79931c84002e46a5ede) | PASS   |
|                                                                       |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Epic 5                                                                |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Issue                                                                 | Title                                                                    | User Story                                                                                                                                                  | Acceptance Criteria                                                                                                                                                                                          | Implementation                                                                                  | Final Commit                                                                                                   | Result |
| [# 25](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/25) | USER STORY : See News Highlights on landing page                         | As a Site User I can See the News Highlights to see three newest news posts.                                                                                | When I visit the site's landing page then I am able to see news highlights on a carousel rotation.                                                                                                           | ( Appendix 78 )                                                                                 | [503f6ab](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/503f6ab884226ae2453e5598ae5792f19e83788d) | PASS   |
| [# 26](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/26) | USER STORY : See list of all News & Details                              | As a Site User I can Visit Page with all News to be able tosee all News.                                                                                    | When I visit the site's landing page then I am comfortably able to navigate to list of all news and see details of each news posts.                                                                          | ( Appendix 79 ) and ( Appendix 80 )                                                             | [503f6ab](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/503f6ab884226ae2453e5598ae5792f19e83788d) | PASS   |
| [# 27](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/27) | USER STORY : Like/Unlike News                                            | As a Site User I can Like or Unlike News Post to highlight the News Post as interesting.                                                                    | Logged in user : When I open news post detail then I am able to like or unlike the post. Not logged in user : Doesn't have that option.                                                                      | ( Appendix 81 )                                                                                 | [11010d4](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/11010d40fbe33d667ee6804c4869e5ae96aeeb7c) | PASS   |
| [# 28](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/28) | USER STORY : Comment on News                                             | As a Site User I can Comment on News Post to share my opinion.                                                                                              | Logged in user : When I open news post detail then I am able to add comment on the relevant news post. Not logged in user : Doesn't have that option.                                                        | ( Appendix 82 )                                                                                 | [a42b417](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/a42b4178dacdd64c00b0bbb532e20f1fe75ab06f) | PASS   |
| [# 29](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/29) | USER STORY : See other users Comments                                    | As a Site User I can see other comments on News Posts to read other Users opinions.                                                                         | Logged in user :When I open news post detail then I am able to see other people comments.Not logged in user :Doesn't have that option.                                                                       | ( Appendix 82 )                                                                                 | [a823dfc](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/a823dfc321ea432c1fe688e19e6739187d252c0a) | PASS   |
| [# 30](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/30) | USER STORY : See who else liked                                          | As a Site User I can see who else liked News Posts to see who else has the same opinion.                                                                    | Logged in user :When I open news post detail then I am able to see who else liked the post.Not logged in user :Doesn't have that option.                                                                     | ( Appendix 83 )                                                                                 | [7b09a2e](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/7b09a2ec75cffb8656d34d00b1f34a49b5374161) | PASS   |
|                                                                       |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Epic 6                                                                |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Issue                                                                 | Title                                                                    | User Story                                                                                                                                                  | Acceptance Criteria                                                                                                                                                                                          | Implementation                                                                                  | Final Commit                                                                                                   | Result |
| [# 32](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/32) | USER STORY : List of Styles                                              | As a Site User I can See list of available styles to be able to choose one to see details.                                                                  | When I navigate to styles from navbar then I see list of all styles that are available.                                                                                                                      | ( Appendix 84 ) and ( Appendix 85 )                                                             | [f989ca8](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/f989ca83477ccde96828399d58d3fffe0a949450) | PASS   |
| [# 33](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/33) | USER STORY : Styles Details                                              | As a Site User I can See Style details to see description and what artist does this particular style.                                                       | When I open list of styles then I like to be able to see all details about the particular style including likes and "tries".                                                                                 | ( Appendix 85 )                                                                                 | [9e5415a](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/9e5415a8102cb5d27f315315407267ae87e3cbc4) | PASS   |
| [# 34](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/34) | USER STORY : Like / Unlike Styles                                        | As a Site User I can Like / Unlike particular Style to express my opinion.                                                                                  | Logged in user : When I open detail of a particular style then I am able to like/unlike style.Not logged in user : Doesn't have that option.                                                                 | ( Appendix 85 )                                                                                 | [b22d266](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/b22d266264181a63874720aa066c9c87c3ff4b1b) | PASS   |
| [# 35](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/35) | USER STORY : See who else likes the particular Style                     | As a Site User I can see who else liked the particular style to see who else has same opinion.                                                              | Logged in user :When I open style detail then I am able to see who else liked the style.Not logged in user :Doesn't have that option.                                                                        | ( Appendix 83 )                                                                                 | [9e5415a](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/9e5415a8102cb5d27f315315407267ae87e3cbc4) | PASS   |
| [# 36](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/36) | USER STORY : Mark / Unmark Styles as "Wan't to try"                      | As a Site User I can Mark / Unmark particular style to express my interest.                                                                                 | Logged in user :When I open detail of a particular style then I am able to mark it as "try/untry".Not logged in user :Doesn't have that option.                                                              | ( Appendix 85 )                                                                                 | [b22d266](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/b22d266264181a63874720aa066c9c87c3ff4b1b) | PASS   |
| [# 37](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/37) | USER STORY : See who else marked the partucular style as "Want to try"   | As a Site User I can see who else marked partulcar style as "Want to try to see who else has same interests.                                                | Logged in user :When I open style detail then I am able to see who else marked the style as "want to try".Not logged in user :Doesn't have that option.                                                      | ( Appendix 86 )                                                                                 | [9e5415a](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/9e5415a8102cb5d27f315315407267ae87e3cbc4) | PASS   |
|                                                                       |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Epic 7                                                                |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Issue                                                                 | Title                                                                    | User Story                                                                                                                                                  | Acceptance Criteria                                                                                                                                                                                          | Implementation                                                                                  | Final Commit                                                                                                   | Result |
| [# 39](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/39) | USER STORY : Create a booking                                            | As a Site User I can Create new booking and to be able to choose date, time and artist.                                                                     | Logged in user :When I navigate to "my bookings" then I am able to create a booking.Not logged in user :Doesn't have that option.                                                                            | ( Appendix 87 )                                                                                 | [a817445](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/a817445b3fd1c8c5fc891bcee4b777a1f83972a4) | PASS   |
| [# 40](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/40) | USER STORY : See my bookings                                             | As a Site User I can See all my bookings to be able to keep record of them.                                                                                 | Logged in user :When I navigate to "My bookings", I can clearly see upcoming and past bookings.Not logged in user :Doesn't have that option.                                                                 | ( Appendix 88 )                                                                                 | [0893feb](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/0893feb43f831438ef9f3503e409d8f4c9d49c7b) | PASS   |
| [# 41](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/41) | USER STORY : Update my bookings                                          | As a Site User I can Update any of my future bookings to change details.                                                                                    | Logged in user :When I navigate to "My Bookings" then I am able to select a booking that I wan to change.Not logged in user :Doesn't have that option.                                                       | ( Appendix 89 )                                                                                 | [1ab529e](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/1ab529e66fe125bfab99fe14c65e45a7f758af10) | PASS   |
| [# 42](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/42) | USER STORY : Delete my bookings                                          | As a Site User I can Delete any of my future bookings to cancel the booking.                                                                                | Logged in user :When I navigate to my bookings then I can cancel the booking(s).Not logged in user :Doesn't have that option.                                                                                | ( Appendix 89 )                                                                                 | [74d849c](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/74d849cdd3887da3019f13dc34ee4799ed6ef771) | PASS   |
| [# 43](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/43) | USER STORY : Leave review after booking finished                         | As a Site User I can leave review to let the others know about my satisfaction.                                                                             | Logged in user :When my booking is done I can navigate to "My bookings" and leave a review for particular booking.Not logged in user :Doesn't have that option.                                              | ( Appendix 90 )                                                                                 | [0ff4da1](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/0ff4da14bc3eecb6ab818efe9883789a81cf3a26) | PASS   |
| [# 44](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/44) | USER STORY : Get confirmation of my booking being approved               | As a Site User I get confirmation email when my booking is approved to be sure the booking is going ahead.                                                  | When I my booking is confirmed by Site Admin then I am notified via email.                                                                                                                                   | ( Appendix 91 )                                                                                 | [8e4ef41](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/8e4ef412be0228a064f9bc9d698b4c8fc402f14c) | PASS   |
|                                                                       |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Epic 8                                                                |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Issue                                                                 | Title                                                                    | User Story                                                                                                                                                  | Acceptance Criteria                                                                                                                                                                                          | Implementation                                                                                  | Final Commit                                                                                                   | Result |
| [# 52](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/52) | USER STORY : Create search bar on landing page                           | As a Site User I am able to use search function through Artists, Styles and News to quickly find what am I looking for.                                     | When I open the landing page then I can see the search bar.                                                                                                                                                  | ( Appendix 78 )                                                                                 | [0c9cebe](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/0c9cebea491867384d9fc385f5f1e34935bba0ce) | PASS   |
| [# 53](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/53) | USER STORY : Provide search results                                      | As a Site User I can see search result to easily navigate through them.                                                                                     | When I submit search criteria and clcik the search button then I am able to see the results.                                                                                                                 | ( Appendix 92 )                                                                                 | [3a4d8f3](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/3a4d8f3311e5117b90a6619f1d2efe8b7e60e39b) | PASS   |
|                                                                       |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Epic 9                                                                |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Issue                                                                 | Title                                                                    | User Story                                                                                                                                                  | Acceptance Criteria                                                                                                                                                                                          | Implementation                                                                                  | Final Commit                                                                                                   | Result |
| [# 55](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/55) | USER STORY : Delete user                                                 | As a Site Admin, I can delete user accounts that are no longer in use to make sure my database of clients is up to date.                                    | When I log in to admin suite then I can navigate to user profiles and delte user entirely.                                                                                                                   | ( Appendix 93 )                                                                                 | [3bf93b4](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/3bf93b4f0ab84850a9181d9d96973adcbd8a7b66) | PASS   |
| [# 56](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/56) | USER STORY : Manage news                                                 | As a Site Admin, I can add news posts to keep content up to date.                                                                                           | When I log in to admin suite then I can navigate to News and add, change or delete news content.                                                                                                             | ( Appendix 94 )                                                                                 | [3bf93b4](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/3bf93b4f0ab84850a9181d9d96973adcbd8a7b66) | PASS   |
| [# 57](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/57) | USER STORY : Manage available styles                                     | As a Site Admin, I can add available styles to keep content up to date.                                                                                     | When I log in to admin suite then I can navigate to Styles and add, change or delete available styles.                                                                                                       | ( Appendix 95 )                                                                                 | [3bf93b4](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/3bf93b4f0ab84850a9181d9d96973adcbd8a7b66) | PASS   |
| [# 58](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/58) | USER STORY : Manage artists                                              | As a Site Admin, I can add nail artists to keep list of employees up to date.                                                                               | When I log in to admin suite then I can navigate to Artists and, change and delete avalable artists.                                                                                                         | ( Appendix 96 )                                                                                 | [3bf93b4](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/3bf93b4f0ab84850a9181d9d96973adcbd8a7b66) | PASS   |
| [# 59](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/59) | USER STORY : Approve comments                                            | As a Site Admin, I can approve comments to ensure no harmful content.                                                                                       | When I log in to admin suite then I can navigate to Comments and approve or delete comments.                                                                                                                 | ( Appendix 97 )                                                                                 | [3bf93b4](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/3bf93b4f0ab84850a9181d9d96973adcbd8a7b66) | PASS   |
| [# 60](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/60) | USER STORY : Mark bookings as confirmed                                  | As a Site Admin, I can mark bookings as confirmed to inform user of the progress.                                                                           | When I log in to admin suite then I can navigate to Bookings and mark pending bookings as confirmed.                                                                                                         | ( Appendix 98 )                                                                                 | [3bf93b4](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/3bf93b4f0ab84850a9181d9d96973adcbd8a7b66) | PASS   |
| [# 61](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/61) | USER STORY : Mark bookings as done                                       | As a Site Admin, I can mark bookings as done to inform user of the progress and allow user to rate.                                                         | When I log in to admin suite then I can navigate to Bookings and mark pending bookings as done.                                                                                                              | ( Appendix 99 )                                                                                 | [3bf93b4](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/3bf93b4f0ab84850a9181d9d96973adcbd8a7b66) | PASS   |
| [# 62](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/62) | USER STORY : Last-minute bookings                                        | As a Site Admin, I need to provide users with "last-minute" bookings available to let them know how many slots are free the following day.                  | Logged in user :When Site Users log in and navigate to "My Bookings" then they are provided with info of the following day free slots.Not logged in user :Doesn't have that option.                          | ( Appendix 100 )                                                                                | [7bb09fb](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/7bb09fb6b273ce873b23350cf89df2387bb26d62) | PASS   |
|                                                                       |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Epic 10                                                               |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Issue                                                                 | Title                                                                    | User Story                                                                                                                                                  | Acceptance Criteria                                                                                                                                                                                          | Implementation                                                                                  | Final Commit                                                                                                   | Result |
| [# 71](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/71) | USER STORY : Intuitive navigation                                        | As a Site Developer, I need to insure easy navigation throughout the site.                                                                                  | Not Applicable                                                                                                                                                                                               | [Please see readme.md](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/README.md) | Not Applicable                                                                                                 | PASS   |
| [# 72](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/72) | USER STORY : Color scheme                                                | As a Site Developer, I need to insure same color scheme throughout the site                                                                                 | Not Applicable                                                                                                                                                                                               | [Please see readme.md](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/README.md) | Not Applicable                                                                                                 | PASS   |
| [# 73](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/73) | USER STORY : WAVE compatibility                                          | As a Site Developer, I need to insure that site can be easily navigated using page readers, so it doen't have WAVE issues.                                  | Not Applicable                                                                                                                                                                                               | [Please see readme.md](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/README.md) | Not Applicable                                                                                                 | PASS   |
|                                                                       |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                | PASS   |
| Epic 11                                                               |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Issue                                                                 | Title                                                                    | User Story                                                                                                                                                  | Acceptance Criteria                                                                                                                                                                                          | Implementation                                                                                  | Final Commit                                                                                                   | Result |
| [# 75](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/75) | USER STORY : W3C HTML validation                                         | As a Site Developer, I need to ensure \*.html files do pass the W3C validation.                                                                             | Not Applicable                                                                                                                                                                                               | [Please see readme.md](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/README.md) | Not Applicable                                                                                                 | PASS   |
| [# 76](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/76) | USER STORY : W3C CSS validation                                          | As a Site Developer, I need to ensure style.css file do pass the W3C validation.                                                                            | Not Applicable                                                                                                                                                                                               | [Please see readme.md](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/README.md) | Not Applicable                                                                                                 | PASS   |
| [# 77](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/77) | USER STORY : JS validation                                               | As a Site Developer, I need to ensure \*.js files do pass the JS Lint validation.                                                                           | Not Applicable                                                                                                                                                                                               | [Please see readme.md](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/README.md) | Not Applicable                                                                                                 | PASS   |
| [# 78](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/78) | USER STORY : PEP8 validation                                             | As a Site Developer, I need to ensure \*.py file do pass the PEP8 validation.                                                                               | Not Applicable                                                                                                                                                                                               | [Please see readme.md](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/README.md) | Not Applicable                                                                                                 | PASS   |
|                                                                       |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Epic 12                                                               |                                                                          |                                                                                                                                                             |                                                                                                                                                                                                              |                                                                                                 |                                                                                                                |        |
| Issue                                                                 | Title                                                                    | User Story                                                                                                                                                  | Acceptance Criteria                                                                                                                                                                                          | Implementation                                                                                  | Final Commit                                                                                                   | Result |
| [# 80](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/80) | USER STORY : Admin interface that copies functions of Django Admin Suite | As a Site Developer I need to come up with cusom admin interface that ensures all functions of Django Admin Suite,                                          | When I log in as Admin and click Admin in NavBar then I am able to use same functions as logging in to Django Admin Suite.                                                                                   | Not implemented, left in the back log. Marked as WONT'T HAVE on Kanban Board                    | Not Applicable                                                                                                 | FAIL   |

*Appendix 68 - Testing*

![Appendix 68](/docs/testing/test-68.png)

*Appendix 69 - Testing*

![Appendix 69](/docs/testing/test-69.png)

*Appendix 70 - Testing*

![Appendix 70](/docs/testing/test-70.png)

*Appendix 71 - Testing*

![Appendix 71](/docs/testing/test-71.png)

*Appendix 72 - Testing*

![Appendix 72](/docs/testing/test-72.png)

*Appendix 73 - Testing*

![Appendix 73](/docs/testing/test-73.png)

*Appendix 74 - Testing*

![Appendix 74](/docs/testing/test-74.png)

*Appendix 75 - Testing*

![Appendix 75](/docs/testing/test-75.png)

*Appendix 76 - Testing*

![Appendix 76](/docs/testing/test-76.png)

*Appendix 77 - Testing*

![Appendix 77](/docs/testing/test-77.png)

*Appendix 78 - Testing*

![Appendix 78](/docs/testing/test-78.png)

*Appendix 79 - Testing*

![Appendix 79](/docs/testing/test-79.png)

*Appendix 80 - Testing*

![Appendix 80](/docs/testing/test-80.png)

*Appendix 81 - Testing*

![Appendix 81](/docs/testing/test-81.png)

*Appendix 82 - Testing*

![Appendix 82](/docs/testing/test-82.png)

*Appendix 83 - Testing*

![Appendix 83](/docs/testing/test-83.png)

*Appendix 84 - Testing*

![Appendix 84](/docs/testing/test-84.png)

*Appendix 85 - Testing*

![Appendix 85](/docs/testing/test-85.png)

*Appendix 86 - Testing*

![Appendix 86](/docs/testing/test-86.png)

*Appendix 87 - Testing*

![Appendix 87](/docs/testing/test-87.png)

*Appendix 88 - Testing*

![Appendix 88](/docs/testing/test-88.png)

*Appendix 89 - Testing*

![Appendix 89](/docs/testing/test-89.png)

*Appendix 90 - Testing*

![Appendix 90](/docs/testing/test-90.png)

*Appendix 91 - Testing*

![Appendix 91](/docs/testing/test-91.png)

*Appendix 92 - Testing*

![Appendix 92](/docs/testing/test-92.png)

*Appendix 93 - Testing*

![Appendix 93](/docs/testing/test-93.png)

*Appendix 94 - Testing*

![Appendix 94](/docs/testing/test-94.png)

*Appendix 95 - Testing*

![Appendix 95](/docs/testing/test-95.png)

*Appendix 96 - Testing*

![Appendix 96](/docs/testing/test-96.png)

*Appendix 97 - Testing*

![Appendix 97](/docs/testing/test-97.png)

*Appendix 98 - Testing*

![Appendix 98](/docs/testing/test-98.png)

*Appendix 99 - Testing*

![Appendix 99](/docs/testing/test-99.png)

*Appendix 100 - Testing*

![Appendix 100](/docs/testing/test-100.png)


## **5.2.4. Test Cases**

Part ot this testing was to ensure user cannot access restricted content to registered users or user cannot change content that was created by another user. This was achieved by using `LoginRequiredMixin` for classes and `@login_required` for methods when user needs to be logged in for certain view.

For user not being able to change content that isn't created by user was used following Mixin and test function. 

`UserPassesTestMixin`

`    def test_func(self):
        """Test function to ensure user is the booking creator"""
        booking = get_object_or_404(
            Bookings, pk=self.kwargs["edit_booking_pk"])
        return self.request.user == booking.username`

### **Test case 001 - General Site Navigation ( Appendix 101 )**

General functionality of the project tested.

*Appendix 101 - Test Case 001*

![Test Case 001](/docs/testing/case-001.png)

### **Test case 002 - Search Function ( Appendix 102 )**

Search functionality of the project tested.

*Appendix 102 - Test Case 002*

![Test Case 002](/docs/testing/case-002.png)

### **Test case 003 - Registering New User ( Appendix 103 )**

Registering New User functionality tested.

*Appendix 103 - Test Case 003*

![Test Case 003](/docs/testing/case-003.png)

### **Test case 004 - Changing User Details ( Appendix 104 )**

Changing User Details functionality tested.

*Appendix 104 - Test Case 004*

![Test Case 004](/docs/testing/case-004.png)

### **Test case 005 - Changing Email Address ( Appendix 105 )**

Changing User's email address functionality tested.

*Appendix 105 - Test Case 005*

![Test Case 005](/docs/testing/case-005.png)

### **Test case 006 - Changing Password ( Appendix 106 )**

Changing User's password functionality tested.

*Appendix 106 - Test Case 006*

![Test Case 006](/docs/testing/case-006.png)

### **Test case 007 - Bookings CRUD ( Appendix 107 )**

Bookings CRUD functionality tested.

*Appendix 107 - Test Case 007*

![Test Case 007](/docs/testing/case-007.png)

### **Test case 008 - Commenting ( Appendix 108 )**

Commenting functionality tested.

*Appendix 108 - Test Case 008*

![Test Case 008](/docs/testing/case-008.png)

### **Test case 009 - Liking ( Appendix 109 )**

Liking functionality tested.

*Appendix 109 - Test Case 009*

![Test Case 009](/docs/testing/case-009.png)

### **Test case 010 - Deleting User Profile ( Appendix 110 )**

Deleting User Profile functionality tested.

*Appendix 110 - Test Case 010*

![Test Case 010](/docs/testing/case-010.png)

## **5.2.4. Viewport Testing**

- **Task :** To physically test the final project responsiveness on different devices with different view-port.
- **Method :** All test cases listed above were tested on following devices : 
  - IPhone 8 - mobile phone with small view-port
  - Samsung Fold Z4 - mobile phone with large view-port
  - FireHD 8 - tablet with small view-port
  - Samsung Galaxy tab S6 - tablet with large view-port
  - PC with resolution 1366px * 768px (HD)
  - PC with resolution 1920px * 1080px (Full HD)  
- **Expected result :** Project does response without distortion on all devices.
- **Actual result :**  No content is distorted on any of the listed devices.
- **Overall result :** Pass

## **5.2.5. Compatibility Testing**

- **Task :** To physically test the final project functionality in different browsing applications.
- **Method :** All test cases listed above were tested in following applications : 
  - Google Chrome
  - Mozilla Firefox
  - Microsoft Edge
  - Opera
  - Safari
- **Expected result :** Project does function in all web browsers.
- **Actual result :**  No content is distorted in any of the listed browsers and project keeps functionality, all navigation links are working and form is responsive to empty fields.
- **Overall result :** Pass