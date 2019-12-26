Users
=============

Subpackages
-----------

.. toctree::

   users.signals
   users.templatetags


Submodules
----------

users.admin
------------------
File: *./users/admin.py*

~~~~~~~~~~~~~
Introduction
~~~~~~~~~~~~~

    In this file, we have register the Blog application
    to django admin, so we can control it from admin dashboard.

contents
~~~~~~~~
    The path to this file is: *./blog/admin.py*

    So, in this file, we have created custom admin interface for custom User and the TaggedArticles.
    We have the following classes in this file:
1. **InlineTaggedArticle:** To create the overview of TaggedArticles in tabular form.
2. **CustomAdmin:** It will display the customized view for tagged articles, binned the **InlineTaggedArticle**
   to the articles view and also show the total number of tagged articles.
3. **TaggedArticleResource:** It will define the model to use for CSV/Excel import and export of articles.
4. **TaggedArticleAdmin:** It will register **TaggedArticleResource** and add proper fields and display for import/export.



.. automodule:: users.admin
   :members:
   :undoc-members:
   :show-inheritance:

users.apps
-----------------
   This is the file where we have initialized the **users** app for this project.
.. automodule:: users.apps
   :members:
   :undoc-members:
   :show-inheritance:

users.forms
------------------
   **File:** *./users/forms.py*

.. topic:: Explanation:

    In this file, you will find all the forms classes related
    to the users on the project.

.. compound::

   In this file, we have the following Forms classes:

1. **SignUpForm:** It will provide a form to register a new user with all the fields with proper validation.
   And, also define new custom fields we need to get information related to them from the user.
2. **LogoutForm:** The will get the current user, it's session adn get the logged out.
3. **CertForm:** This form will allow to generate a certificate of completion for a user.

.. automodule:: users.forms
   :members:
   :undoc-members:
   :show-inheritance:

users.models
-------------------
**File:** *./users/models.py*

.. topic:: Explanation:

    In this file, you will find all the database models related
    to users app.

.. compound::

   In this file, we have all the database models related to users and
   these are the followings.

1. **TaggedArticle:** The model to define what a Tagged article is? and defined all the required and
   optional fields with the proper input types to create a database table to store tagged articles.


TaggedArticle
^^^^^^^^^^^^


Fields
`````````````
    :user: A reference to an authenticated user who has the the permissions to tag an article.
    :email: An email field to store the email of sue who tagged the article.
    :category_fit: Will store the category for the article.
    :article: A reference to the Article model.
    :link: Will the store the link to the actual article.
    :relevant_feedback: A text type field to store the user's feedback about the article.
    :category: Will store the category user thinks a suitable category.
    :created_at: The Datetime field, will be populated with the current time automatically.

.. automodule:: users.models
   :members:
   :undoc-members:
   :show-inheritance:

users.urls
-----------------
*******
Urls
*******


**File:** *./users/urls.py*

.. topic:: Explanation:

    In this file, you will find all the url patterns to load various pages
    and call the corresponding views.

.. compound::

   In this file, we have all the url paths to load and call different functions of the users module.

`````````````
All urls
`````````````
    :profile: This is the path to the profile page of logged in user.
    :search: Will land you to the login page and get the user logged in on form submission.
    :signup: Will land you to the signup page and get the user registers in the platform on form submission.
    :logout: Allow a user to get logged out from the site.
    :dashboard: Will land you to the main dashboard page after login.
    :process: This url will handle the processing of the payment on request to get the certificate.
    :process: Will cancel the payment processing if you hit that by mistake and something went wrong.
    :paypal: Will handle all the payment's related operation while requesting a certificate of completion.


.. automodule:: users.urls
   :members:
   :undoc-members:
   :show-inheritance:


users.views
------------------

*******
Views
*******


**File:** *./users/views.py*

.. topic:: Explanation:

    In this file, you will find all the views classes and functions related
    to the users application of the project.

.. compound::

   In this file, we have the following views classes and functions:

1. **Dashboard(class):** It will load the main dashboard page after login.
2. **LogoutView(class):** It will handle the user's request to logout from the site.
   input form on blog home page.
3. **Profile(class):** A class to handle the user's profile functions, like load user's data on profile page.
4. **Tagging(class):** This will load the articles to get tagged.Query the database to grab all un-tagged articles
   for the user to tag.
5. **TagView(class):** A class to handle the request to tag an article with the user's feedback and update the database.
6. **delete_post(function):** A function to delete a single post. It will take the ID of the post you
   want to delete.
7. **generate_cid(function):** A function to generate a random ID for the certificate.
8. **payment_process(function):** A function to process user's payment and allow him to generate the certificate.
9. **payment_done(function):** A function to redirect the user to a specific page if the payment processed successfully.
10. **payment_canceled(function):** A function to redirect the user to a specific page if the payment has been canceled.



.. automodule:: users.views
   :members:
   :undoc-members:
   :show-inheritance:


Module contents
---------------

.. automodule:: users
   :members:
   :undoc-members:
   :show-inheritance:
