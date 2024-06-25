# PRODIGY_CS_03

# Password Complexity Checker

 Build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength.

## Step 1: Define Password Strength Criteria

We need to establish what makes a password strong. Here are common criteria:

Length: A minimum number of characters (e.g., at least 8 characters).<br>

Uppercase Letters: Presence of at least one uppercase letter (A-Z).<br>

Lowercase Letters: Presence of at least one lowercase letter (a-z).<br>

Numbers: Presence of at least one digit (0-9).<br>

Special Characters: Presence of at least one special character (e.g., !, @, #, $).<br>

## Step 2: Create a Function to Check Each Criterion
We'll create separate functions to check if a password meets each of the above criteria.<br>

## Step 3: Combine Checks to Assess Overall Strength
Now, let's create a function that uses the above checks to determine the password strength. We'll give feedback based on how many criteria are met.

## Step 4: Provide Feedback to the User
Finally, we need a way to get the password from the user and provide the feedback. Here’s how we can do that in a simple script.


# How to Run

## 1. Open the file in the VS Code

## 2. Open Terminal in VS Code:

Click on Terminal > New Terminal from the top menu. This will open a new terminal at the bottom of the VS Code window.

## 3. Navigate to the Script Location (Optional):

If your script is not in the default directory, use the cd command to navigate to the directory where you saved password_checker.py. For example: cd path\to\your\script

## 4. Run the Script:

In the terminal, type the following command and press Enter: Password Complexity Checker.py

You will be prompted to enter a password. After entering the password, you will receive feedback on its strength.

# Here’s how it might look in the VS Code terminal:

PS C:\path\to\your\script> python password_checker.py
Enter your password: MyPassw0rd!
Password is very strong.



