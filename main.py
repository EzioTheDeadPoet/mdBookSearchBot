import discord
import yaml
import mdbook_search

with open("secrets.yaml", "r") as secrets_yaml:
    secrets = yaml.safe_load(secrets_yaml)
with open("config.yaml", "r") as cfg_yaml:
    cfg = yaml.safe_load(cfg_yaml)

mdbook_url = cfg["mdBookHomeURL"]
mdbook_name = cfg["mdBookName"]

bot = discord.Bot()


@bot.command(description=f"Search in {mdbook_name}.")
# pycord will figure out the types for you
async def wiki_search(ctx, query: discord.Option(str)):
    results = mdbook_search.search_wiki(query)
    results_url = mdbook_url + "?search=" + mdbook_search.url_string(query)
    embed = discord.Embed(
        title=f"{len(results)} search results for '{query}'",
        url=f"{results_url}",
        color=discord.Color.from_rgb(216, 186, 248))
    embed.set_author(name=mdbook_name, url=mdbook_url)
    i = 0
    for result in results:
        i += 1
        title = result["title"]
        href = result["href"]
        paragraph_preview = result["paragraph_preview"]
        embed.add_field(name=f"Result {i}:", value=f"[**{title}**]({href}) \n"
                                                   f" {paragraph_preview}", inline=False)
    await ctx.respond(embed=embed)


bot.run(secrets["token"])
