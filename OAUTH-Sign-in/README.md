# OAUTH-Sign-in

Once the application is running,it should run on <http://localhost:3000> in the web browser.

You should be redirected to the login page, where you can authenticate with the chosen OAuth provider (i.e Google, Facebook and Apple SSOs).

After authenticating, you will be redirected back to the application and a session will be created. You can then access protected routes and resources that require authentication.

Configuration
The following environment variables are required for configuring the application:

SESSION_SECRET: A secret value used to sign session cookies.
OAUTH_CLIENT_ID: The client ID of the OAuth application.
OAUTH_CLIENT_SECRET: The client secret of the OAuth application.
OAUTH_CALLBACK_URL: The callback URL for the OAuth application.
