*******
Models
*******


**File:** *./blod/models.py*

.. topic:: Explanation:

    In this file, you will find all the database models related
    to blog app like, Post, Comment, etc.

.. compound::

   In this file, we have all the database models related to blog app and
   these are the followings.

1. **PostModel:** The model for the blog post.
2. **CommentModel:** The model for the comment on a blog post.

^^^^^^^^^^^^
PostModel
^^^^^^^^^^^^


`````````````
Fields
`````````````
    :title: This is a field of type string which can contain 255 characters max.
    :author: A reference to an authenticated user who has the the permissions to create a blog post.
    :content: Main body field of the blog post which hold the main content.
    :photo: An Image field to add a banner picture to blog post.
    :created_at: The Datetime field, will be populated with the current time automatically.
    :category: A field with the bunch of choices to categorize the blog post.

`````````````
Methods
`````````````
**__str__**
   A function which will return the title of then post when called for an object of PostModel.

**get_last_5**
   This function will return the five most recent posts in descending order.


^^^^^^^^^^^^
CommentModel
^^^^^^^^^^^^


`````````````
Fields
`````````````
    :post: A reference field to the *PostModel* for the post on which comment will be applied.
    :author: A reference to an authenticated user who has the permissions to comment on a post.
    :content: Main body field of the post comment.
    :reply: A reference to the other comments it it is a reply to an existing comment.
    :timestamp: The Datetime field, will be populated with the current time automatically.

`````````````
Methods
`````````````
__str__
   A function which will return the title of the post and the author of the comment.




