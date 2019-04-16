import sys
import os
import subprocess
from pprint import pprint
from datetime import datetime


class TextLogger:
    """
    An object to be used to log info, errors and results to a text file.
    
    When a new instance of this object is made, it will open a text 
    file at the given path and immediately record the python version,
    the path to the python .exe, the current working directory, and 
    the path to the python file that is being run (NOTE: this will 
    not happen in a jupyter notebook). If you are using a conda 
    environment, it will also log the modules and versions of the 
    packages in the environment.

    Example:
        try:
            # do someting
        except Exception as e:
            log.log_error(e)
    """

    def __init__(self, path=False):
        if not path:
            self.path = "log_{}.txt".format(
                str(datetime.now()).split(" ")[0].replace("-", "")
            )
        else:
            self.path = path
        self.executable = sys.executable
        self.version = sys.version
        self.cwd = os.getcwd()
        self.closed = False
        self.is_timing = False

        try:
            self.filepath = os.path.realpath(__file__)
        except:
            pass

        if "Continuum" in self.executable:
            self._conda_packages = subprocess.check_output(
                "conda list -n {}".format(sys.executable.split("\\")[-2]),
                universal_newlines=True,
            )

        def start_log(self):
            with open(self.path, "w") as f:
                f.write("LOG INITIALIZED AT :  {}\n".format(str(datetime.now())))
                f.write("Python version: {}\n".format(self.version))
                f.write("Python executable path: {}\n".format(self.executable))
                f.write("Current working directory: {}\n".format(self.cwd))
                try:
                    f.write("File path: {}\n".format(self.filepath))
                except:
                    pass
                try:
                    f.write("\n{}{}\n".format(self._conda_packages, "-" * 72))
                except:
                    pass
            return

        start_log(self)

    def conda_pkgs(self):
        """
        Use this method to pretty print the packages in your conda env.
        """
        if not self.closed:
            return pprint(self._conda_packages)
        else:
            raise Exception(
                "This log has been closed. See {} for the log file.".format(self.path)
            )

    def log_error(self, error):
        """
        Use this method within "except" to log errors and move on.
        """
        if not self.closed:
            with open(self.path, "a") as f:
                f.write("\n--- {} ---\n".format(str(datetime.now())))
                f.write("ERROR:  {}\n".format(error))
            print(error)
            return
        else:
            raise Exception(
                "This log has been closed. See {} for the log file.".format(self.path)
            )

    def log_output(self, output):
        """
        Use this method to log the output of an operation to your text log.
        """
        if not self.closed:
            with open(self.path, "a") as f:
                if isinstance(output, list):
                    f.write("\n--- {} ---\nOUTPUT:  list\n".format(str(datetime.now())))
                    [f.write(x + "\n") for x in output]
                else:
                    f.write("\n--- {} ---\n".format(str(datetime.now())))
                    f.write("OUTPUT:  {}\n".format(str(output)))
            return
        else:
            raise Exception(
                "This log has been closed. See {} for the log file.".format(self.path)
            )

    def add_message(self, message, printed=False):
        """
        Use this method to add a message to your log.
        """
        if not self.closed:
            if not printed:
                assert isinstance(
                    message, str
                ), "Error: method add_message expects a string."
                with open(self.path, "a") as f:
                    f.write("\n--- {} ---\n".format(str(datetime.now())))
                    f.write("MESSAGE:  {}\n".format(message))
                return
            else:
                assert isinstance(
                    message, str
                ), "Error: method add_message expects a string."
                with open(self.path, "a") as f:
                    f.write("\n--- {} ---\n".format(str(datetime.now())))
                    f.write("MESSAGE:  {}\n".format(message))
                print("MESSAGE:  {}\n".format(message))
        else:
            raise Exception(
                "This log has been closed. See {} for the log file.".format(self.path)
            )

    def timestamp(self):
        """
        Use this method to insert a timestamp into your log.
        """
        if not self.closed:
            with open(self.path, "a") as f:
                f.write("\n--------------\n")
                f.write("TIMESTAMP:  {}".format(str(datetime.now())))
                f.write("\n--------------\n")
            return
        else:
            raise Exception(
                "This log has been closed. See {} for the log file.".format(self.path)
            )

    def start_timer(self):
        """
        Use this method to begin a timer.
        """
        if not self.closed:
            self.timing = True
            self.start = datetime.now()
            return
        else:
            raise Exception(
                "This log has been closed. See {} for the log file.".format(self.path)
            )

    def end_timer(self, message=False):
        """
        Use this method to end a timer. The processing time will be 
        printed and written to the log file.
        """
        if not self.closed:
            if self.timing:
                if not message:
                    proc_time = datetime.now() - self.start
                    print("Processing time:  {}".format(proc_time))
                    with open(self.path, "a") as f:
                        f.write("\nProcessing time:  {}\n".format(proc_time))
                else:
                    assert isinstance(
                        message, str
                    ), "Error: end_timer expects no arguments or a message string."
                    proc_time = datetime.now() - self.start
                    print(
                        "MESSAGE:  {}\nProcessing time:  {}".format(message, proc_time)
                    )
                    with open(self.path, "a") as f:
                        f.write(
                            "\nMESSAGE:  {}\nProcessing time:  {}\n".format(
                                message, proc_time
                            )
                        )
            else:
                raise Exception(
                    "No timer has been started. Call the start_timer method to begin timing a process."
                )
            return
        else:
            raise Exception(
                "This log has been closed. See {} for the log file.".format(self.path)
            )

    def close(self):
        """
        Use this method to end the log. This will record the time it
        was closed. Making a new log with the same filepath will 
        overwrite the old log.
        """
        if not self.closed:
            self.closed = True
            with open(self.path, "a") as f:
                f.write("\n\n--------------\n")
                f.write("LOG CLOSED AT: {}".format(str(datetime.now())))
            print("Log closed.")
            return
        else:
            raise Exception(
                "This log has been closed. See {} for the log file.".format(self.path)
            )
