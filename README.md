UK Politics Blog


<img width="996" alt="Screenshot 2022-11-22 at 10 07 09" src="https://user-images.githubusercontent.com/95533259/203286864-9fdba7a8-7983-4f55-9972-7b70752208af.png">



Purpose:

UK politics is a minefield of nonsense and everyone has an opinion but people are often looking for information which presents an honest opinion.
Whilst blog posts are the opinion of an individual, the site could give the user the comfort that other people are feeling the way they are.

User Stories / Build Development / Sprints / Wireframe

User Stories have been created to document the different requirements for use of the site.  It is important to document the user stories as we need to make sure that we are creating the full requirements of the site for the user.  I wrote all the requirement stories, when I was working on a story I moved it to in development, then when I completed working on a story, I moved it to completed.
As there is a small number of varied stories, I did not feel the need to build an Epic.
The Acceptance Criteria on the User Stories was specific enough for me to understand what it is I had written and what the story requirements were. Which means that each of the stories written is in the build of the project.

Build Development / Sprints / iterations:

I completed this project in 2 x 1 day sprints.  As there is a limited number of user stories, I did not feel the need to spread the build over a number of days or weeks.
Within a larger project team, you might expect a sprint to last 2 weeks, however due to the limited amount of stories that required build, it did not take that long.
This project is not really an "Agile" project, it is a Waterfall project.  I knew what I wanted to create and there was an end vision, a blog where users could read posts about UK politics.  There wasn't any need for an iterative approach.

Wireframe:

As with any project, it is important to understand the user experience and with this blog site, I have documented this in a wireframe.  This captures the requirements of a user of this site.


![wireframe](https://user-images.githubusercontent.com/95533259/212945343-6c2ba4e1-c9f4-46f8-88ab-0dae61101a42.jpg)

Technologies Used

HTML5
CSS3
Javascript
Python
Django
Bootstrap
ElephantSQL
Cloudinary

Testing

I spent quite a while manually testing the site to ensure that the functionality works.  I would create a post and then comment on it.  Then I would like it.  Then I would delete the comment and I would unlike the post.
I then repeated this activity on different posts.  Commenting, liking, deleting the comment and unliking the post.
I also tested based on User Stories.
When I implemented User Story one - I tested that the pagination works by selecting the other pages
When I implemented User Story two - I tested that a user could open a post by opening a post
When I implemented User Story three - I tested that a user could like a post by liking a post
When I implemented User Story four - I tested that a user could comment on a post by commenting on a post
When I implemented User Story five - I tested that a user could register by registering as a user
When I implemented User Story six - I tested that a user could view comments by creating comments and then viewing them
When I implemented User Story seven - I tested that a user could see how many likes and comments a post had by adding likes and comments and viewing them on the post
When I implemented User Story eight - I tested that a user had to be authenticated before liking or commenting on a post by attempting to like/comment on a post when not logged in, this didn't work and therefore I knew the functionality worked
When I implemented User Story nine - I tested that a user could un-like a post by liking a post and then unliking it
When I implemented User Story 10 - I tested that a user could delete a comment they had added, by adding a comment and then deleting it.

HTML Validator – does not like django and has some errors relating to construct of Django code
CSSC Validator – no issues found

Lighthouse:
Found an issue with accessibility to do ALT tags on images which are loaded as blog posts, which I then resolved.

Heroku<img width="1092" alt="Screenshot 2022-11-22 at 10 33 01" src="https://user-images.githubusercontent.com/95533259/203292794-4121e411-9468-40fb-b67f-d5481f3728f8.png">

Deployment:

In order for these projects to be deployed, for some unknown and baffling reason, we have to do that on Heroku which charges users for storing their project builds.
In order to deploy this project, we have to make all sorts of adjustments to the settings to make sure that this project works:
Setting the debug flag to False
Adding in X_FRAME_OPTIONS as "SAME_ORIGIN" otherwise summernote won't work!!
Once that was done, I redeployed the project to GitHub.
I connected Heroku to the GitHub repo and deployed it on Heroku.
I then opened the app on Heroku and made sure that it was visible.

Deployment Issues:

Am I Responsive – getting an image from Heroku is impossible so I found a solution on Slack to open the gitpod port and use that to get the image

The static files would not load in Heroku because I had forgotten to remove the config vars relating to static from Heroku – which I resolved.

Credits
Code Institute: I used the basis of the CodeStar blog code for this project which was created by Code Institute and I then adapted this code for my own project

Youtube Videos: how to create a blog in Django

Slack: I utilised various slack posts for ideas and issues as and when they arose.
![image](https://user-images.githubusercontent.com/95533259/203292738-92368c7f-f2dd-45d3-91a6-b51bbe6c4fa8.png)
