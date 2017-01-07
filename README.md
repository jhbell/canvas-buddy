# canvas-buddy
Python script for accessing canvas grades

## How to install

* Step 1:
Download/Clone the repository

* Step 2:
Generate an access token in Canvas. **Copy the token!** See "Manual Token Generation": [Link](https://canvas.instructure.com/doc/api/file.oauth.html#manual-token-generation)

* Step 3:
Create a file called auth.py containing:
`TOKEN = "<your-access-token>"`

* Step 4: 
Change the `_ROOT_URL` in canvas.py to match your canvas subdomain. (Optional, utexas by default)

* Step 5:
Fire 'er up and check out your grades!
