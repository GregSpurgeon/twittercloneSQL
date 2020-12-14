Though we can only hope that your time with SQL will be limited, it's important to understand and be familiar with some of the grittier details of writing SQL queries.

#### **Your Task**

This assignment is to submit a github gist that contains valid SQL queries to build the Twitterclone database (with the exception of no following; we'll forgo the many-to-many relationship, as it's more complicated than necessary). Likewise, we do not need to worry about storing encrypted passwords.

#### **Part 1:**

The first part of your document should be the statements required to create all the tables and the appropriate fields, data types, and nullability. Use your existing models as a reference, and use a local version of postgresql to test your commands. (Install with `brew install postgresql`). If you're installing it for the first time, remember that `psql` will need your username as the default database, so create it with `createdb {yourusername}`. After that you can create the tables you'll need.

#### **Part 2:**

The second part of your document should be queries which provide the results for the following operations (hint: most of these will need subqueries!):

1.  Query to create a new user (username: steve, password: hunter2, display name: steve-o)
2.  Query to create two new users <span style="text-decoration: underline;">at once</span>: 
    *   username: dave, password: asdf, display name: davey
    *   username: bob, password: qwer, display name: bobbinator
3.  Query to get the username and password of twitteruser ID 1
4.  Query to get the ID of a user by the username of dave
5.  Query to create a new tweet written by the user with the username steve (yes, you have to get the ID of Steve first -- _hint_: subqueries are your friend)
6.  <span>Query to g</span>et the count of tweets by username steve (<span>_hint_: subqueries are your friend</span>)
7.  Query to get the date and text of all tweets <span>by username steve (_hint_: subqueries are your friend)</span>
8.  Query to get the username and password of the username bob
9.  Query to create a notification for username bob using the tweet written by username steve (<span>_hint_: subqueries are your friend</span>)
10.  Query to get all IDs of notifications for bob (<span>_hint_: subqueries are your friend</span>)

**Extra Credit:**

1.  Extra Credit, 1pt: Query to delete a tweet starting when you already know the ID (use 1)
2.  Extra Credit: 2pts: Single query to delete all the tweets belonging to username bob
3.  Extra Credit: 5pts: Single query to output:
    *   Username of the person the notification is meant for (steve-o)
    *   username of the person who wrote the tweet that triggered the notification
    *   text of the tweet
    *   ...where the only piece of information you start with is the _display name_ of Steve; "steve-o"

#### **Submission:**
Copy and paste the appropriate lines from your terminal into the submission.txt document (we only care about the commands that were ran in order to accomplish the task).  Then submit your pull request to canvas.
