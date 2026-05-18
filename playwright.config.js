// @ts-check
import { defineConfig, devices } from '@playwright/test';

/**
 * @see https://playwright.dev/docs/test-configuration
 */

export default defineConfig({

  testDir: './tests',

  /* Run tests in parallel */
  fullyParallel: true,

  /* Fail build if test.only exists */
  forbidOnly: !!process.env.CI,

  /* Retry on CI */
  retries: process.env.CI ? 2 : 0,

  /* Workers */
  workers: process.env.CI ? 1 : undefined,

  /* Reporters */
  reporter: [
    ['html'],
    ['json', {
      outputFile: 'test-results.json'
    }]
  ],

  /* Shared settings */
  use: {

    /* Collect trace */
    trace: 'on-first-retry',

    /* Open browser */
    headless: false,
  },

  /* Browser projects */
  projects: [
    {
      name: 'chromium',
      use: {
        ...devices['Desktop Chrome']
      },
    },
  ],
  const isCI = !!process.env.CI;

module.exports = {
  use: {
    headless: isCI ? true : false,
  },
};
});