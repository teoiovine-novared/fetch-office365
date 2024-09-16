# fetch-office365
## Introduction (English)
Python/BASH script that pulls O365 IP list from Microsoft web service (https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide) and generates a data group in F5 to be used by an iRule/Policy

## How to use
1. Download the content of this repo.
2. Upload it to the F5 device, to a directory of your choice. Normally, /shared.
3. Assign execution permissions:
   - > chmod +x -R fetch-office365/
   - > chmod +rw fetch-office365/latest_version
4. Add directory to PATH:
   - Temporal: > export PATH="/shared/fetch-office365:$PATH"
   - Permanent: add 'export PATH="/shared/fetch-office365:$PATH"' at the end of .bashrc
   - 


