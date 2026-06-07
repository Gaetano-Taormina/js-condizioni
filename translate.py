import os
import shutil
import subprocess

translations = {
    "es_1": {
        "new_name": "club-access",
        "script.js": """console.log("JS connected correctly");\n\nlet age = prompt("Enter your age: ");\n\nage = Number(age);\nif (age > 18){\n    console.log("Access granted to the club");\n} else {\n    window.open('','self');\n    window.close();\n}\n""",
        "README.md": "# Exercise\n* Ask the user's age via prompt. If the user is an adult, print \"Access granted to the club\" to the console.\n\n## Reasoning\n\n* read the user's age \n* if user is an adult print message\n* else windows.open('','self') to open and window.close() to close the window for minors\n"
    },
    "es_2": {
        "new_name": "luggage-fee",
        "script.js": """console.log("JS connected correctly");\n\nlet ticketPrice = 36;\nlet luggageWeight = prompt("Enter your luggage weight in kg");\n\nluggageWeight = Number(luggageWeight);\n\nif (luggageWeight > 23) {\n    ticketPrice = ticketPrice + 20;\n}\n\nconsole.log(`The ticket price is ${ticketPrice}`);""",
        "README.md": "# Exercise\n\n- The ticket cost is 36 €. Ask the luggage weight in kg. If the weight exceeds 23kg, there is a 20 € surcharge, finally print the ticket price.\n\n## Reasoning\n\n- the ticket cost varies only under a certain condition\n- the luggage weight can vary\n- ask the luggage weight\n- read the luggage weight\n  - if luggage weight exceeds 23 kg add 20 euros to the ticket price\n"
    },
    "es_3": {
        "new_name": "even-odd",
        "script.js": """console.log("JS connected correctly");\n\nlet n = prompt("Enter a number: ");\n\nn = Number(n);\n\nif (n % 2 == 0){\n    console.log("Even");\n} else {\n    console.log("Odd");\n}""",
        "README.md": "# Exercise\n* Ask the user for a number. Print if it is even or odd.\n\n## Reasoning\n* ask the user for a number\n* read number\n* if even print even\n    * else print odd\n"
    },
    "es_4": {
        "new_name": "rollercoaster",
        "script.js": """console.log("JS connected correctly");\n\nlet age = prompt("Declare the user's age: ");\nage = Number(age);\n\nif (age < 14) {\n    alert("Access Denied: user is too young");\n} else {\n    let height = prompt("Declare the user's height(cm): ");\n    height = Number(height);\n    if (height < 140){\n        alert("Access Denied: user does not meet the requirements");\n    } else {\n        console.log("Have fun");\n    }\n}\n""",
        "README.md": "# Exercise\n* An amusement park requires a minimum height of 140cm and at least 14 years of age for the rollercoaster. Ask the user for this data and print if they can access the rollercoaster.\n\n## Reasoning v1.0\n* request height\n* request age\n\n* use if to check the requirements\n* if the requirements are not met use an alert to indicate the lack of minimum requirements\n\n## Reasoning v1.1\n* request age\n    * if age is under 14 do not request height\n\n* after checking age and finding the minimum age, request height\n    * if height is under 140 cm declare the user's lack of requirements\n"
    },
    "es_5": {
        "new_name": "age-greeting",
        "script.js": """console.log("JS connected correctly");\n\nlet age = prompt("Enter the user's age: ");\nage  = Number(age);\n\nif (age < 18) {\n    console.log("Hi");\n} else if (age >= 60) {\n    console.log("Greetings");\n} else {\n    console.log("Welcome");\n}""",
        "README.md": "# Exercise\n* Ask the user's age. If minor print \"Hi\", if over 60 print \"Greetings\", otherwise print \"Welcome\".\n\n## Reasoning \n* read the age\n* if minor print hi\n    * if over 60 print greetings \n        * otherwise print welcome\n"
    },
    "es_6": {
        "new_name": "loyalty-discount",
        "script.js": """console.log("JS connected correctly");\n\nlet loyaltyCard = prompt("Do you have the loyalty card? (yes/no)");\n\nloyaltyCard = loyaltyCard.trim().toLowerCase();\n\nif (loyaltyCard === "yes" || loyaltyCard === "y") {\n    loyaltyCard = 1;\n} else {\n    loyaltyCard = 0;\n}\n\nlet price = prompt("Enter the product price: ");\n\nif (loyaltyCard) {\n    price = price * 0.9;\n}\n\nconsole.log("The price to pay is: ", price);""",
        "README.md": "# Exercise\n* Ask if the user has a loyalty card. If they have the card apply a 10% discount to the entered price, otherwise leave the full price. Print the price.\n\n## Reasoning\n* read loyalty card \n* read price\n* if loyalty card exists so loyaltyCard=1 apply discount\n* print the final price \n"
    },
    "es_7": {
        "new_name": "weekend-check",
        "script.js": """console.log("JS connected correctly");\n\nlet day = prompt("Enter the day of the week: ");\n\nday = day.trim().toLowerCase();\n\nif (day == "saturday" || day == "sunday") {\n    console.log("Have a good weekend");\n} else {\n    console.log("Have a good day at work");\n}""",
        "README.md": "# Exercise\n* Ask the user what day it is today. If it is \"saturday\" or \"sunday\" print \"Have a good weekend!\", otherwise print \"Have a good day at work\".\n\n## Reasoning \n* read the day string \n* if saturday or sunday print Have a good weekend\n    * otherwise print have a good day at work \n"
    },
    "es_8": {
        "new_name": "login-check",
        "script.js": """console.log("JS connected correctly");\n\nlet username = prompt("Enter username: ");\nlet password = prompt("Enter password: ");\n\nif( username == "admin" && password == "1234") {\n    console.log("Login successful");\n} else {\n    alert("Invalid credentials");\n}""",
        "README.md": "# Exercise\n\n* Ask username and password. If they are respectively \"admin\" and \"1234\", print \"Login successful\", otherwise print \"Invalid credentials\".\n\n## Reasoning\n\n* read username and password\n* if username == admin && password == \"1234\" print Login successful\n  * otherwise print Invalid credentials \n"
    },
    "es_9": {
        "new_name": "grade-eval",
        "script.js": """console.log("JS connected correctly");\n\nlet n = prompt("Enter a number between 1 and 10: ");\n\nwhile (n < 1 || n > 10 ) {\n    alert("Error: Invalid value");\n    n = prompt("Enter a number between 1 and 10: ");\n}\n\nn = Number(n);\nif(n < 6){\n    console.log("Insufficient");\n} else if (n < 8 ){\n    console.log("Sufficient");\n} else if (n < 10){\n    console.log("Good");\n} else{\n    console.log("Excellent");\n}""",
        "README.md": "# Exercise\n* Ask for a grade from 1 to 10. Print \"Insufficient\" if < 6, \"Sufficient\" if between 6 and 7, \"Good\" if between 8 and 9, \"Excellent\" if 10.\n\n## Reasoning\n* read a value \n* check if given value is between 1 and 10 \n\n* if n < 6 print insufficient\n    * otherwise if n < 8 print sufficient\n        * otherwise if n < 10 print good \n            * otherwise print excellent\n"
    },
    "es_10": {
        "new_name": "parking-fee",
        "script.js": """console.log("JS connected correctly");\n\nlet h = Number(prompt("Indicate how many hours you will stay in the parking lot: "));\nlet cost;\n\nif (h > 5){\n    cost = 15;\n} else if (h > 2){\n    cost = 10;\n} else {\n    cost = 5;\n}\n\nconsole.log("The amount due is: " + cost + " € ");""",
        "README.md": "# Exercise\n\nAsk how many hours you stay in the parking lot. If <= 2 hours it costs 5€, if <= 5 hours it costs 10€, otherwise it costs 15€.\n\n## Reasoning\n\n* read hours\n* if hours > 5 print cost 15 euros\n  * otherwise if hours > 2 print cost 10\n  * otherwise cost 5\n"
    },
    "es_11": {
        "new_name": "retirement-check",
        "script.js": """console.log("JS connected correctly");\nlet g;\ndo {\n    g = prompt("Enter the user's gender: (M/F)");\n    if (g) g = g.trim().toLowerCase();\n\n    const mVariants = ["m", "male", "boy"];\n    const fVariants = ["f", "female", "girl"];\n\n    if (mVariants.includes(g)) {\n        g = "M";\n    } else if (fVariants.includes(g)) {\n        g = "F";\n    } else {\n        alert("Invalid value");\n        g = "";  \n    }\n\n} while (g !== "M" && g !== "F")\n\nlet age = prompt("Enter age: ");\nage = Number(age);\n\nif ((g === "M" && age >= 67 ) || (g === "F" && age >=62)){\n    console.log("You can retire");\n} else {\n    console.log("You still have to work");\n}""",
        "README.md": "# Exercise\n\n* Ask the age and gender (\"M\" or \"F\"). If it is a man and has >= 67 years or a woman and has >= 62 years, print \"You can retire\", otherwise \"You still have to work\".\n\n## Reasoning\n\n* gender initialization\n* do\n  * read gender from user;\n  * declaration of two arrays for M and F;\n  * if array M includes;\n    * g gets M as value\n  * otherwise if array F includes;\n    * g gets F as value;\n* while to correct the user in case of incorrect terms for gender;\n\n* read user age;\n* if gender === M && age >= 67 || gender === F && age >= 62\n  * print you can retire;\n* else\n  * print you still have to work.\n"
    },
    "es_13": {
        "new_name": "name-check",
        "script.js": """// script.js\nconsole.log("JS connected correctly");\nlet name;\n\ndo {\n    name = prompt("Enter user's name: ");\n    if (!name) {\n        alert("You have not entered any name");\n    }\n} while (!name);\n\nconsole.log("The user's name is: ", name);\n""",
        "README.md": "\n## Exercise \n * Gaetano:\nAsk the user to enter their name. Verify that they have not left the field empty.\n\n## Reasoning\n* declare variable name \n* read the user's name\n    * if the user has not entered the user's name \n        * point it out to the user\n* go back in case of missing name\n* give the user's name as a result \n"
    }
}

for old_dir, data in translations.items():
    if os.path.exists(old_dir):
        new_dir = data["new_name"]
        
        # Rewrite script.js
        script_path = os.path.join(old_dir, "assets", "js", "script.js")
        if os.path.exists(script_path):
            with open(script_path, "w", encoding="utf-8") as f:
                f.write(data["script.js"])
                
        # Rewrite README.md
        readme_path = os.path.join(old_dir, "README.md")
        if os.path.exists(readme_path):
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(data["README.md"])
                
        # Rewrite index.html language to en
        index_path = os.path.join(old_dir, "index.html")
        if os.path.exists(index_path):
            try:
                with open(index_path, "r", encoding="utf-8") as f:
                    html = f.read()
                html = html.replace('lang="it"', 'lang="en"')
                html = html.replace('<title>Document</title>', f'<title>{new_dir}</title>')
                with open(index_path, "w", encoding="utf-8") as f:
                    f.write(html)
            except:
                pass
        
        # Finally copy and remove from git
        try:
            if not os.path.exists(new_dir):
                shutil.copytree(old_dir, new_dir)
            subprocess.run(["git", "rm", "-r", "--cached", old_dir], check=False)
            subprocess.run(["git", "add", new_dir], check=False)
            print(f"Copied {old_dir} to {new_dir} and updated git.")
        except Exception as e:
            print(f"Failed to copy {old_dir}: {e}")
