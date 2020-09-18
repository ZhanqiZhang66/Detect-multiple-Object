# Detect multiple Object 
 This project is inspired by and coded based on Google Cloud Platform, Cloud Vision API https://cloud.google.com/vision/docs/object-localizer
# Set up the environment
 1. please follow the link here and select the python as the language https://cloud.google.com/vision/docs/object-localizer
 2. in terminal, cd to the project you want to locate 
 3. in terminal, activate the venv you just created in step 1. For example, mine is called gcp and the command I used is ```.\gcp\Scripts\activate  ```
 4. Don't forget to set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of the JSON file that contains your service account key. This variable only applies to your current shell session, so if you open a new session, set the variable again. 
 # To run the code
 In terminal, cd to the folder containing the project, run ```python  localize_object.py```
