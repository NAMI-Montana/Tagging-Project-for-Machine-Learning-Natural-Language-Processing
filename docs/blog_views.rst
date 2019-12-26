*******
Views
*******


**File:** *./blog/views.py*

.. topic:: Explanation:

    In this file, you will find all the views classes and functions related
    to the Blog application of the project.

.. compound::

   In this file, we have the following views classes and functions:

1. **home(function):** The function to load the home page of the Blog along
   with all the published posts.
2. **search(function):** A function to handle the search query submit by user via the search
   input form on blog home page.
3. **category(function):** A function return the blog posts related to a category.It will
   take the name of the category as the input.
4. **post_detail(function):** A function to get a single post detail page. It will take the ID of
   the post you want to get as the input.
5. **PostCreate(class):** A class to handle the creation of a new Blog Post.Upon the GET request
   it will load the page with a form to fill for the new post and on the POST request,
   it will check the permission against the user and save the new post to database.
6. **delete_post(function):** A function to delete a single post. It will take the ID of the post you
   want to delete.
7. **comment(function):** A function to post comment on a single blog post.


