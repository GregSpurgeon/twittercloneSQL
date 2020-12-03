# 🐦The Ever-So-Slightly-Intimidating Project 🐦

Now that we've started really putting together real applications with Django, it's time to step up basically everything.

One of the most important things about web development (that I'm sure you've already figured out, but I'll reiterate here) is that once you learn the building blocks of what makes a website, you just repeat those blocks to build larger and larger sites. What we're going to do is take the building blocks from the recipe application and turn them into something much larger and greater.

What we're going to do is build a small clone of Twitter. It will feature logged in users, a customized homepage, a tweet composing page, the ability to follow other users, and more. We'll be using every single concept from the previous applications plus a few more; don't worry though, we've got plenty of time. The video from the demo I gave on my site is / will be linked at the bottom of this assignment.

<span>This project is divided into two parts. Part 1 is all about the folder structure. Part 2 is going to be implementing the logic and front end, and there's lots of resources available to help.</span> 

#### **Your Task**

**Part 1**

There will be four pieces to this application, each with their own app:

*   twitterclone <-- This is your project folder
*   twitteruser <-- This is a custom user app!
*   tweet
*   authentication
*   notification

<span style="text-decoration: underline;">Note</span>: Please follow PEP8's guidelines on naming conventions for your packages and modules ([<span>https://www.python.org/dev/peps/pep-0008/#package-and-module-names</span>](https://www.python.org/dev/peps/pep-0008/#package-and-module-names)). Mainly, just name them exactly how they are listed above.

Each app will (potentially) need its own:

*   models.py
*   views.py
*   urls.py
*   forms.py
*   \_\_init\_\_.py

Set up the initial folder structure and create all the files you'll need -- get the settings.py file configured and the django server ready to go. In Part 2, we'll start filling in the files with logic.

This project comes with a preconfigured **.gitignore** file in your project directory.

**Part 2**

Though this assignment requires some new knowledge, everything I used is either on stackoverflow or in the Django documentation. Some pieces that might help you:

*   [https://stackoverflow.com/a/16614136](https://stackoverflow.com/a/16614136)
*   [https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/](https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/)
*   [https://stackoverflow.com/questions/9410647/how-to-filter-model-results-for-multiple-values-for-a-many-to-many-field-in-djan](https://stackoverflow.com/questions/9410647/how-to-filter-model-results-for-multiple-values-for-a-many-to-many-field-in-djan)
*   [https://docs.djangoproject.com/en/3.0/howto/static-files/](https://docs.djangoproject.com/en/3.0/howto/static-files/) <-- only if you want to deliver custom CSS
*   [https://stackoverflow.com/questions/18622007/runtimewarning-datetimefield-received-a-naive-datetime](https://stackoverflow.com/questions/18622007/runtimewarning-datetimefield-received-a-naive-datetime)
*   [https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#include](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#include)

The demo video covers only the front end, and things like pretty CSS and formatting are completely optional. What matters is that the backend performs the work and it can deliver the user experience. It's up to you to design the backend and make it functional. You may have to do it more than once as your application gains complexity, but hopefully you don't!

Whatever you can write that delivers the pages and functionality shown in the video is good enough. Some suggestions:

*   Segment each major section of your app into its own folder, then put another copy of the appropriate files under it. For example, `from tweet.models import Tweet`.
*   Use the `include` keyword I linked above; it will make your templating so much easier.
*   Create a single function that organizes all the data most of your templates need; then you only have to import that helper function into each view that performs a large render and you know the information will already be there.

Take a look at the rubric for more specific requirements.

#### **Submission**

Submit a link to your pull request

<pre>https://github.com/kenzie-se-q4/recipebox-v1/&ltgithub_username&gt/pull/&ltnumber&gt</pre>
