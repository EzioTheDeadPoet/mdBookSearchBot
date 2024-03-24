import discord
import yaml
import mdbook_search

with open("secrets.yaml", "r") as secrets_yaml:
    secrets = yaml.safe_load(secrets_yaml)
with open("config.yaml", "r") as cfg_yaml:
    cfg = yaml.safe_load(cfg_yaml)

mdbook_url = cfg["mdBook"]["mdBookHomeURL"]
mdbook_name = cfg["mdBook"]["mdBookName"]
maxResults = cfg["discord"]["maxResults"]

bot = discord.Bot()


@bot.command(description=f"Search in {mdbook_name}.")
# pycord will figure out the types for you
async def wiki_search(ctx, query: discord.Option(str)):
    results = mdbook_search.search_wiki(query)
    results_url = mdbook_url + "?search=" + mdbook_search.url_string(query)
    embed_title = f"{len(results)}/{len(results)} search results for '{query}':"
    if len(results) > maxResults:
        embed_title = f"{maxResults}/{len(results)} search results for '{query}':"
    embed = discord.Embed(
        title=embed_title,
        url=f"{results_url}",
        color=discord.Color.from_rgb(216, 186, 248))
    embed.set_author(name=mdbook_name, url=mdbook_url)
    i = 0
    for result in results:
        i += 1
        title = result["title"]
        href = result["href"]
        paragraph_preview = result["paragraph_preview"]
        if paragraph_preview == "":
            paragraph_preview = "This result has no preview."
        embed.add_field(name="", value=f"[**{title}**]({href}) \n"
                                       f" ```{paragraph_preview}```", inline=False)
        if i == maxResults:
            break
    await ctx.respond(embed=embed)


bot.run(secrets["token"])
