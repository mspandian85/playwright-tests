
const { test, expect }
= require('@playwright/test');

test('Test Case - SCRUM-1 TS001 TC001',
async ({ page }) => {

    // 1. Launch the OrangeHRM application in a web browser [Test Data- URL: https://orangehrm.example.com] [Acceptance Criteria- AC1]

    await page.goto(
        'https://opensource-demo.orangehrmlive.com/'
    );

    // 2. Enter valid username in the username field [Test Data- Username: valid_admin] [Acceptance Criteria- AC1]

    await page.getByPlaceholder(
        'Username'
    ).fill('Admin');

    // 3. Enter valid password in the password field [Test Data- Password: ValidPassword123] [Acceptance Criteria- AC1]

    await page.getByPlaceholder(
        'Password'
    ).fill('admin123');

    // 4. Click on the Login button [Acceptance Criteria- AC1]

    await page.getByRole(
        'button',
        { name: 'Login' }
    ).click();


    await expect(page)
        .toHaveURL(/dashboard/);


});
