from linkedin import linkedin

API_KEY = "75i4121vcmndhp"
API_SECRET = "Zi6dEWMS9GijIyuS"
RETURN_URL = "http://9efbc57c.ngrok.io"
authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
print authentication.authorization_url





