# Platform web-ui-automation

Python-based UI automation framework based on BDD

## For start using the framework:
### REQUIRES: Python >= 2.7.11
And run the command `pip install -r <THIS_FILE>` - help you install all necessary packages

NB if you don't have the pip, first install pip with `easy_install` or `brew`. 


## For running script on Jenkins :
### I use the PyVirtualDisplay, which specify in code
```
   if 'JENKINS' in os.environ:
        from pyvirtualdisplay import Display
        global display
        display = Display(visible=0, size=(1280, 1024))
        display.start()
```
   
   And executing the shell command on Jenkins:
```
   /home/jenkins/.local/bin/lettuce -v 3 --with-xunit
```


## Reporting: 
  
  For reporting I use the pre-installed Jenkins plugin <a href='https://wiki.jenkins.io/display/JENKINS/Allure+Plugin'>Allure Report</a>

`lettuce -v 3 --with-xunit` - this command will help you generate the XML file for allure.

