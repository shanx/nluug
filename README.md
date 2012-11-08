Presentation for the NLUUG conference on november 8th 2012
==========================================================

The presentation is a semi-live coding demo that builds part of the app found here: https://github.com/shanx/sytycnluug

The coding is split up by a number of tags for notable changes. These tags are the following:
1. Added basic buildout + gitignore
2. Added django to buildout
3. Added project as develop egg
4. Added ratezzz app
5. Updated settings file with db and apps installed
6. Added talk model
7. Added initial migration for ratezzz
8. Added first test for ratezzz
9. Added basic urls.py and views.py. Our first test responds green, yay!
10. Check for actual talk content in response
11. Added talk content to view using a template
12. Added command to import talks and added csv
13. Added test for rating a talk
14. Added Rating model with proper schemamigration
15. Test posting of rating
16. Added post view for talks (to post ratings), fixes the test again. Yay!
17. Add test of sending multiple rating for same talk, logic should be that same client updates value while a different client adds a new rating.
18. Implemented cookie logic. Same client updates rating with multiple posts. New clients add a new rating on post.

