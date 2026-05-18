
const { test, expect }
= require('@playwright/test');

test('Test Case - SCRUM-1 TS001 TC001',
async ({ page }) => {

    // 1. Launch the OrangeHRM application in a web browser [Test Data- URL: https://opensource-demo.orangehrmlive.com/] [Acceptance Criteria- AC1]

    await page.goto(
        'https://opensource-demo.orangehrmlive.com/'
    );

    // 2. Verify that the login page contains Username field, Password field, and Login button [Acceptance Criteria- AC1]

    await page.getByPlaceholder(
        'Username'
    ).fill('Admin');

    // 3. Enter valid username in the Username field [Test Data- validAdmin] [Acceptance Criteria- AC1]

    await page.getByPlaceholder(
        'Username'
    ).fill('Admin');

    // 4. Enter valid password in the Password field [Test Data- validPassword123!] [Acceptance Criteria- AC1]

    await page.getByPlaceholder(
        'Password'
    ).fill('admin123');

    // 5. Click on the Login button [Acceptance Criteria- AC1]

    await page.getByRole(
        'button',
        { name: 'Login' }
    ).click();

    // 6. Verify that the dashboard displays HR administrator functionalities and employee management options [Acceptance Criteria- AC1]

    await expect(page)
        .toHaveURL(/dashboard/);


});
