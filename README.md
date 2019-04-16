# TextLogger
A basic, homemade class for logging information and messages from a script to a text file. 

__Further development: questionable__

---

### What this is not:
 - This is not a real logger. As such, it does not `import logging`.
 - This is also not going to catch warnings.
 - This does not supress errors. You still need to use try/except for that.
    - However, you can put the TextLogger.log_error method in an except statement and pass over the error while writing it to your text file.
