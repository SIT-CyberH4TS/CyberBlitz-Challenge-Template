# CYBERH4TS-CYBERBLITZ-CTF
Challenge submission template for CYBERH4TS/CYBERBLITZ CTF

## Submission Template
The challenge & file structure should look like this:
```
challenge_name/
    |
    |
    |
    ├─ dist/
    |       ├─ image.png
    |
    |
    ├─ service/
    |       ├─ docker-compose.yml
    │       ├─ container-name/
    │           ├─ Dockerfile
    │           ├─ files_to_host_challenge
    |
    ├─ solution/
    │       ├─ writeup.md
    │       ├─ solution_files
    |
    ├─ challenge.yml
    ├─ README.md
```

*note: please ensure that your `README.md` & `challenge.yml` contains the same information*

- `dist`
  - This folder contains all the files that **will be given** to the participants, leave this folder empty if none.
- `service`
  - This folder contains all the files that will be used by the team to host your challenge, leave this folder empty if none.
  - `container-name`
    - This folder contains all the files that will be used to build the docker image for your challenge, do note that this may be given to participants to host the challenge locally if they wish to do so.
    - `Dockerfile`
      - This file contains the instructions to build the docker image for your challenge.
- `solution`
  - This folder should contain a writeup of your challenge and solution files (if any)
  - If your challenge is generated using a script, please include the script in this folder.

