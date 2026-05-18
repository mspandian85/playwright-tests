import json
import requests
import urllib3

# -----------------------------------
# Disable SSL warnings
# -----------------------------------

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)

# -----------------------------------
# Credentials
# -----------------------------------

testrail_url = "https://ascendionqesmoketest.testrail.io"

username = "navneet.bhargavan@ascendion.com"

password = "Y3Gd2GUFrNKfu9ykmZaA-AAu2wMvbFpXNhskSkytq"

# -----------------------------------
# TestRail Details
# -----------------------------------

run_id = 117
case_id = 1816

# -----------------------------------
# Read Playwright JSON Result
# -----------------------------------

with open(
    "test-results.json",
    "r"
) as file:

    report = json.load(file)

status = "failed"

# -----------------------------------
# Find Result
# -----------------------------------

for suite in report.get(
    "suites",
    []
):

    for spec in suite.get(
        "specs",
        []
    ):

        for test in spec.get(
            "tests",
            []
        ):

            for result in test.get(
                "results",
                []
            ):

                if (
                    result.get("status")
                    == "passed"
                ):

                    status = "passed"

# -----------------------------------
# Convert Status
# -----------------------------------

status_id = 5

if status == "passed":
    status_id = 1

# -----------------------------------
# Update TestRail
# -----------------------------------

endpoint = (
    f"{testrail_url}"
    f"/index.php?/api/v2/"
    f"add_result_for_case/"
    f"{run_id}/{case_id}"
)

payload = {
    "status_id": status_id,
    "comment":
        f"Playwright Automation Result: {status}"
}

response = requests.post(
    endpoint,
    json=payload,
    auth=(username.strip(), password.strip()),
    verify=False
)

print("Status Code:", response.status_code)
print("Response:", response.text)

response.raise_for_status()

print(
    f"Updated TestRail successfully: {status}"
)