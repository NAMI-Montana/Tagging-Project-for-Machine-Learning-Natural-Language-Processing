*******
Urls
*******


**File:** *./blod/urls.py*

.. topic:: Explanation:

    In this file, you will find all the url patterns to load various pages
    and call the corresponding views.

.. compound::

   In this file, we have all the database models related to blog app and
   these are the followings.

`````````````
All urls
`````````````
    :'blog-home': This is the path to the home page of Blog.
    :search: Will land you to the search page to search for blog posts.
    :post/<id>: By this url, you can access a specific post by passing it's id in the url.
    :category/(?P<link>[\w|-]+)/$: Using this, you can access all posts under a same category.
    :post/new: Will land you to page where you can create new blog posts (if you have permissions to do so).
    :post/delete/<id>: By logging to this url, you can delete a post (if you have permissions to do so).
    :comment/new: This url will handle the creation of a comment on a blog post.
