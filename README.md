# mdBookSearchBot

This is more of a personal project intended to be used in the Wabbajack community to run search queries to answer questions in discord.

## To-Do

- Restructure Code to work with Docker for easier Deployment
- Update Documentation (Instructions on how to set it up)
- Add feature to define autocomplete targets for search queries
  - For easier repetition of queries that result in precise search results
 
## Plans for Feature Expansion

- Tag-command that displays markdown files as embeds in Discord
  - tags are stored in a .json or .yaml accessible over the internet (for example github)
    ```json
    [
      "dummy": "https://raw.files/dummy.md"
    ]
    ```
    ```yaml
    dummy: https://raw.files/dummy.md
    ```
  - the bot uses this file to offer autocomplete options and as the source for the markdown text to render
  - advantage of this over similar tags offered by bots like dyno would be that everyone in a community can contribute as long as they have a github account
