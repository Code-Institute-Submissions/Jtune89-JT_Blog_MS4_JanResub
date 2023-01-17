UK Politics Blog


<img width="996" alt="Screenshot 2022-11-22 at 10 07 09" src="https://user-images.githubusercontent.com/95533259/203286864-9fdba7a8-7983-4f55-9972-7b70752208af.png">



Purpose

UK politics is a minefield of nonsense and everyone has an opinion but people are often looking for information which presents an honest opinion.
Whilst blog posts are the opinion of an individual, the site could give the user the comfort that other people are feeling the way they are.

User Stories / Build Development / Sprints

User Stories have been created to document the different requirements for use of the site.  It is important to document the user stories as we need to make sure that we are creating the full requirements of the site for the user.  I wrote all the requirement stories, when I was working on a story I moved it to in development, then when I completed working on a story, I moved it to completed.
As there is a small number of varied stories, I did not feel the need to build an Epic.
The Acceptance Criteria on the User Stories was specific enough for me to understand what it is I had written and what the story requirements were. Which means that each of the stories written is in the build of the project.

I completed 



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

HTML Validator – does not like django and has some errors relating to construct of Django code
CSSC Validator – no issues found

Lighthouse:
Found an issue with accessibility to do ALT tags on images which are loaded as blog posts, which I then resolved.

Heroku<img width="1092" alt="Screenshot 2022-11-22 at 10 33 01" src="https://user-images.githubusercontent.com/95533259/203292794-4121e411-9468-40fb-b67f-d5481f3728f8.png">

Deployment Issues:
Am I Responsive – getting an image from Heroku is impossible so I found a solution on Slack to open the gitpod port and use that to get the image

The static files would not load in Heroku because I had forgotten to remove the config vars relating to static from Heroku – which I resolved.

Credits
Code Institute: I used the basis of the CodeStar blog code for this project which was created by Code Institute and I then adapted this code for my own project

Youtube Videos: how to create a blog in Django

Slack: I utilised various slack posts for ideas and issues as and when they arose.
![image](https://user-images.githubusercontent.com/95533259/203292738-92368c7f-f2dd-45d3-91a6-b51bbe6c4fa8.png)
