# TL;DR: look for the name "Danya Generalov <danya02>"

AKA "Never Trust The Client".

At first, [this](https://gist.github.com/VorontsovIE/f1af96c7e562c7447b54f90873b1f335) would seem like a formidable challenge of breaking the SHA1 hash for the password, and the rainbow tables I've found online didn't contain the password.
But that's the point when you notice that you can just cheat the `session_id` cookie to be something that leaves `valid_session_id` in an accepting state, and since all that that function does is check the length of the string, it's a simple matter of opening up the web developer menu, typing in some 32-length randomness into the field and clicking the submit button.

Despite the last line of the source code suggesting that the script is run as-is, the fact that when you send a large cookie along with your request, the resulting error (`400 Bad Request: Request Header Or Cookie Too Large`) is coming from `nginx/1.10.3 (Ubuntu)`, suggesting that there is some WSGI arrangement going on in there. Or I'm misunderstanding how the `bottle` library works.
