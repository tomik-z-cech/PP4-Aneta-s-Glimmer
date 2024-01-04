# **5.3. Bugs**

## **5.3.1. Fixed Bugs**

**During the development, following bugs were noted :**

| Issue                                                                 | Title                                                                           | Description                                                                           | Screenshot          | Solution                                                                                                                                                                                                                                   | Final Commit                                                                                                   | Result |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | ------ |
| [# 45](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/45) | BUG : Nav-bar isnt' clickable when scrolled down                                | The Nav-bar stops being clickable after scrolled down the page.                       | Not Available       | Z-index of header changed to 9                                                                                                                                                                                                             | [3020bfc](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/3020bfc1b88cba55d19d672acf1999e3c4212853) | FIXED  |
| [# 47](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/47) | BUG : Styles "want to try" not displaying correct amount of "want to try" marks | Styles "want to try" not displaying correct amount of "want to try" marks.            | Not Available       | List sorted by number of "want to try" but displaying number of "likes" originally. After patch, list sorted by number of "want to try" and displays number of "want to try".                                                              | [ec56b3c](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/ec56b3c3455d1634cfcd5e3e93e97221ecbd4007) | FIXED  |
| [# 46](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/46) | BUG : List of News doesn't filter "published" or "not published" news           | List of news doesn't filter published or not published news.                          | Not Available       | `.filter(is_published=1)` added as a search query.                                                                                                                                                                                       | [503f6ab](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/503f6ab884226ae2453e5598ae5792f19e83788d) | FIXED  |
| [# 50](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/50) | BUG : Artist rating not displaying properly when 4.75                           | The rating of artists goes to error when rating is 4.75.                              | *( Appendix 63 )* | Add equal ` >=`  to if else statement on landing page.                                                                                                                                                                                   | [bd08ac1](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/bd08ac1392d556365fc42a2aa7a699ecb7f17d79) | FIXED  |
| [# 49](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/49) | BUG : URL's doubleng                                                            | All URL's are doubling after making project more modular into smaller apps.           | Not Available       | Wrong setup of project + apps URL's, all fixed.                                                                                                                                                                                            | [fe0b058](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/fe0b058e78c136c73dce7ca2a0b7d272054d225f) | FIXED  |
| [# 63](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/63) | BUG : Sizing of forms background                                                | Forms field are overfloving (x axle) from background container.                       | *( Appendix 64 )* | `@media screen and (max-width: 991px) { .form-background { width: 80%; } }` added to style.css                                                                                                                                           | [d71d7f3](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/d71d7f3d9bced7c66dd36ed8b7ccb2874d24fa0f) | FIXED  |
| [# 68](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/68) | BUG : "Last minute" shows negative numbers                                      | Last minute section shows negative numbers of bookings between midnight and 9am.      | *( Appendix 65 )* | Bug fixed with extending if statement to start counting free slots at midnight by adding `if ( time_now >= datetime.strptime("00:00", "%H:%M").time() and time_now < datetime.strptime("09:00", "%H:%M").time() ): slots_left_today = 8` | [b0d9f79](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/b0d9f799e689f525461e6eb541d3c87d18bd5a05) | FIXED  |
| [# 69](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/69) | BUG : Comments link scrolls to top of page                                      | Both, Styles and News scroll to top of the page when "Show comments" link is clicked. | Not Available       | `event.preventDefault();` added to both js scripts to prevent scrolling.                                                                                                                                                                 | [e299eec](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/e299eec55ed063aa426a6d2bf5ad59ba3cd3cf0c) | FIXED  |
| [# 64](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/64) | BUG : Menu not displaying correctly                                             | Menu after clicking the burger icon isn't displaying correctly.                       | *( Appendix 66 )* | Adjust CSS styling via media queries                                                                                                                                                                                                       | [f8925bb](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/f8925bbc5264f77e3b411a29b952a083d89bad65) | FIXED  |
| [# 65](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/65) | BUG : Length of menu items                                                      | Nav-bar items overflow over logo.                                                     | *( Appendix 67 )* | Adjust CSS styling via media queries                                                                                                                                                                                                       | [f8925bb](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/f8925bbc5264f77e3b411a29b952a083d89bad65) | FIXED  |
| [# 66](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/66) | BUG : Creating new booking throws "Naive time warning"                          | When creating new booking, termial displays warning about naive time being used.      | *( Appendix 68 )* | `timezone.make_aware(new_booking.date_time)` - added to new booking                                                                                                                                                                      | [160c5d4](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/160c5d46a89e6e9a99bb913e0bd98d3349551a2c) | FIXED  |
| [# 67](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/issues/67) | BUG : "Naive time warning" when editing booking                                 | When editing existing booking, terminal displays warning about naive time being used. | *( Appendix 69 )* | `timezone.make_aware(new_booking.date_time)` - added to edited booking                                                                                                                                                                   | [275b529](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/commit/275b529fddcd0725a5c9746f6f76c4d20f08311e) | FIXED  |

*Appendix 63 - Bug - issue 50*

![Bug - issue 50](/docs/bugs/bug-63.png)

*Appendix 64 - Bug - issue 63*

![Bug - issue 63](/docs/bugs/bug-64.png)

*Appendix 65 - Bug - issue 68*

![Bug - issue 68](/docs/bugs/bug-65.jpg)

*Appendix 66 - Bug - issue 64*

![Bug - issue 64](/docs/bugs/bug-66.png)

*Appendix 67 - Bug - issue 65*

![Bug - issue 65](/docs/bugs/bug-67.png)

*Appendix 68 - Bug - issue 66*

![Bug - issue 66](/docs/bugs/bug-68.png)

*Appendix 69 - Bug - issue 67*

![Bug - issue 67](/docs/bugs/bug-69.png)


## **5.3.2. Unfixed bugs**

There are no know unfixed bugs as of 3.1.2024.

[Back to top](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/docs/bugs.md#53-bugs)

[Back to README.md](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/tree/main#1-key-project-information)

---
