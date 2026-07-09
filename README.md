# Mallette

This briefcase is a CTF (Capture The Flag) training kit built by PoC Innovation. It's a collection of small, independently dockerized challenges covering web exploitation, binary exploitation/reversing and auth bypass, meant to be handed out as a ready-to-run practice kit for beginners.

## How does it work?

Mallette is not a single application — it's a set of standalone challenges, each living in its own `Challenge-N/` directory with its own stack, Dockerfile and (deliberate) vulnerability:

- **Challenge-1**: a Django-based CTF portal/scoreboard, vulnerable to a raw-SQL injection in its team search feature.
- **Challenge-2**: a C binary exploitation / reversing challenge exposed over SSH (command injection and anti-debug password checks).
- **Challenge-4**: a PHP/MySQL web app vulnerable to an authentication bypass via PHP type juggling.

Each challenge is meant to be built and run as its own Docker container. The `launch.sh` script at the root is a convenience wrapper meant to start all of the challenge containers at once, and `user_generator.py` generates a flat list of fake participant credentials (`user`) that can be handed out to players.

## Getting Started

### Installation

Each challenge is self-contained, so there is no single dependency set to install at the root of the repository. The only requirement to run the challenges as intended is Docker.

If you want to run Challenge-1 outside of Docker, it also has its own Python dependencies:

```sh
cd Challenge-1
pip3 install -r requirements.txt
```

### Quickstart

Build each challenge's Docker image from within its own directory (see each `Challenge-N/` folder for its Dockerfile or build script), then start the containers with:

```sh
./launch.sh
```

### Usage

Once the containers are running, the challenges are reachable on the following ports:

| Challenge | Port | Protocol |
| --- | --- | --- |
| Challenge-1 | 8000 | HTTP |
| Challenge-2 | 2222 | SSH |
| Challenge-4 | 8080 | HTTP |

Distribute the credentials from the `user` file to participants, and let them find the flag hidden in each challenge.

## Get involved

You're invited to join this project ! Check out the [contributing guide](./CONTRIBUTING.md).

If you're interested in how the project is organized at a higher level, please contact the current project manager.

## Our PoC team ❤️

Developers
| [<img src="https://github.com/Codelax.png?size=85" width=85><br><sub>Jules Castéran</sub>](https://github.com/Codelax) | [<img src="https://github.com/Thezap.png?size=85" width=85><br><sub>Theo ZAPATA</sub>](https://github.com/Thezap)
| :---: | :---: |

Manager
| [<img src="https://github.com/KillianG.png?size=85" width=85><br><sub>Killian Gardahaut</sub>](https://github.com/KillianG)
| :---: |

<h2 align=center>
Organization
</h2>

<p align='center'>
    <a href="https://www.linkedin.com/company/pocinnovation/mycompany/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn logo">
    </a>
    <a href="https://www.instagram.com/pocinnovation/">
        <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram logo"
>
    </a>
    <a href="https://twitter.com/PoCInnovation">
        <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter logo">
    </a>
    <a href="https://discord.com/invite/Yqq2ADGDS7">
        <img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white" alt="Discord logo">
    </a>
</p>
<p align=center>
    <a href="https://www.poc-innovation.fr/">
        <img src="https://img.shields.io/badge/WebSite-1a2b6d?style=for-the-badge&logo=GitHub Sponsors&logoColor=white" alt="Website logo">
    </a>
</p>

> 🚀 Don't hesitate to follow us on our different networks, and put a star 🌟 on `PoC's` repositories

> Made with ❤️ by PoC