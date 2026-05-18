import requests
import urllib3

# -----------------------------------
# Disable SSL warnings
# (For office laptop/corporate proxy)
# -----------------------------------

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)

# -----------------------------------
# TestRail Credentials
# -----------------------------------

testrail_url = "https://ascendionqesmoketest.testrail.io"

username = "navneet.bhargavan@ascendion.com"

password = "Y3Gd2GUFrNKfu9ykmZaA-AAu2wMvbFpXNhskSkytq"

# -----------------------------------
# Single Test Case ID
# -----------------------------------

case_id = 1816

# -----------------------------------
# API Endpoint
# -----------------------------------

endpoint = (
    f"{testrail_url}"
    f"/index.php?/api/v2/get_case/{case_id}"
)

# -----------------------------------
# Get Test Case
# -----------------------------------

response = requests.get(
    endpoint,
    auth=(username, password),
    verify=False
)

response.raise_for_status()

case_data = response.json()

print("Connected to TestRail successfully")

title = case_data.get(
    "title",
    "Untitled_Test"
)

print("Test Case Title:", title)

# -----------------------------------
# Read Test Steps
# -----------------------------------

steps = case_data.get(
    "custom_steps",
    ""
)

step_lines = steps.split("\n")

playwright_steps = ""

# -----------------------------------
# Convert TestRail Steps
# → Playwright Code
# -----------------------------------

for step in step_lines:

    if step.strip() == "":
        continue

    step_lower = step.lower()

    playwright_steps += (
        f"    // {step}\n"
    )

    # Launch application
    if "launch" in step_lower:

        playwright_steps += """
    await page.goto(
        'https://opensource-demo.orangehrmlive.com/'
    );

"""

    # Username
    elif "username" in step_lower:

        playwright_steps += """
    await page.getByPlaceholder(
        'Username'
    ).fill('Admin');

"""

    # Password
    elif "password" in step_lower:

        playwright_steps += """
    await page.getByPlaceholder(
        'Password'
    ).fill('admin123');

"""

    # Login button
    elif "login button" in step_lower:

        playwright_steps += """
    await page.getByRole(
        'button',
        { name: 'Login' }
    ).click();

"""

# -----------------------------------
# Add Validation
# -----------------------------------

playwright_steps += """
    await expect(page)
        .toHaveURL(/dashboard/);
"""

# -----------------------------------
# Generate Playwright Script
# -----------------------------------

script = f"""
const {{ test, expect }}
= require('@playwright/test');

test('{title}',
async ({{ page }}) => {{

{playwright_steps}

}});
"""

# -----------------------------------
# File Name
# -----------------------------------

filename = (
    title
    .replace(" ", "_")
    .replace("-", "_")
    .lower()
)

filepath = (
    f"tests/{filename}.spec.js"
)

# -----------------------------------
# Save File
# -----------------------------------

with open(filepath, "w") as file:
    file.write(script)

print(
    "Playwright script generated:",
    filepath
)