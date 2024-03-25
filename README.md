# mdBookSearchBot

This is more of a personal project intended to be used in the Wabbajack community to run search queries to answer questions in discord.

## How to use

### Get a Bot-Token

Follow this guide to get a Token for your Bot:
https://docs.pycord.dev/en/stable/discord.html

### Configuration Environment Variables

- `DISCORD_HBOT_TOKEN` Needs to be set to the bot token
- `MDBOOK_NAME` Name of the mdBook you want to search
- `MDBOOK_HOME_URL` main url for your mdBook
- `DISCORD_MAX_RESULTS` Max number of search results you want to be listed in the discord embed. I use `4` because it looks better. 

### Example Configuration

Docker-Compose.yaml:
```yaml
services:
  mdbook-search-and-support-discord-bot:
    image: eziothedeadpoet/mdbook-search-and-support-discord-bot:latest
    env_file:
      - .env
      - secrets.env
    restart: unless-stopped
```

.env:
```dotenv
MDBOOK_NAME="Wabbajack Wiki"
MDBOOK_HOME_URL=https://wiki.wabbajack.org/
DISCORD_MAX_RESULTS=4
```

secrets.env (needs to be created):
```dotenv
DISCORD_BOT_TOKEN=COPY_TOKEN_HERE
```

## To-Do

- [x] Restructure Code to work with Docker for easier Deployment
- [x] Update Documentation (Instructions on how to set it up)
- [ ] Add feature to define autocomplete targets for search queries
  - For easier repetition of queries that result in precise search results
 
## Plans for Feature Expansion

- Tag-command that displays markdown files as embeds in Discord
  - tags are stored in a .json or .yaml accessible over the internet (for example github)
    ```json
    [
      {"dummy":"https://raw.files/dummy.md"}
    ]
    ```
    ```yaml
    dummy: https://raw.files/dummy.md
    ```
  - the bot uses this file to offer autocomplete options and as the source for the markdown text to render
  - advantage of this over similar tags offered by bots like dyno would be that everyone in a community can contribute as long as they have a github account
