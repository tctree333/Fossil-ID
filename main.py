import sciolyid as bot

bot.setup(
    bot_description = "Fossil ID - A SciOly Discord Bot for aspiring paleontologists",
    bot_signature = "Fossil ID - A Paleontology Bot",
    prefixes = ["f!", "f.", "F!", "F."],
    id_type = "fossils",
    name = "fossil-id",

    github_image_repo_url = "https://github.com/tctree333/Fossil-Bot-Images.git",
    list_dir = "lists",
    wikipedia_file = "wikipedia.txt",
    alias_file = "aliases.txt",

    logs = True,
    log_dir = "logs",
    file_folder = "bot_files",
    data_dir = "data",

    backups_channel = 678435444219969538,
    local_redis = False,
    sentry = True,

    invite = "https://discordapp.com/api/oauth2/authorize?client_id=678437690848313373&permissions=51200&scope=bot",
    support_server = "https://discord.gg/4KdyGc5",
    authors = "person_v1.32, EraserBird, and hmmm",
    source_link = "https://github.com/tctree333/Fossil-ID",

    id_groups = True,
    category_name = "Taxon",
    category_aliases = {},

)

bot.start()