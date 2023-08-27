# from get_images import get_images

async def nop(data, category, item):
    return

config = {
    "bot_description": "Fossil ID - A SciOly Discord Bot for aspiring paleontologists",
    "bot_signature": "Fossil ID - A Paleontology Bot",
    "prefixes": ["f.", "F."],
    "id_type": "fossils",
    "github_image_repo_url": None,
    "support_server": "https://discord.gg/2HbshwGjnm",
    "source_link": "https://github.com/tctree333/Fossil-ID",
    "name": "fossil-id",
    # "members_intent": False,
    "download_func": nop, # get_images,
    "refresh_images": False,
    "evict_images": True,
    "evict_frequency": 3.0,
    "evict_threshold": 6,
    "max_evict": 2,
    "evict_func": nop, # get_images,
    "download_dir": "images/",
    "data_dir": "data/",
    "group_dir": "group/",
    "state_dir": "state/",
    "default_state_list": "NATS",
    "wikipedia_file": "wikipedia.txt",
    "logs": True,
    "logs_dir": "logs/",
    "bot_files_dir": "bot_files",
    "short_id_type": "f",
    "invite": "https://discord.com/api/oauth2/authorize?client_id=678437690848313373&permissions=51200&scope=bot",
    "authors": "person_v1.32, EraserBird, and hmmm",
    "extra_about_fields": [
        {
            "name": "Privacy Policy",
            "value": "By using this bot, you agree to our [Privacy Policy](https://sciolyid.org/privacy/).",
        },
        {
            "name": "Attribution",
            "value": "Images used by this bot are the copyright of their respective owners. These images are sourced from [iDigBio](https://www.idigbio.org/) and Wikimedia Commons.",
        },
    ],
    "id_groups": True,
    "category_name": "taxon",
    "sentry": True,
    "local_redis": False,
    "backups_channel": None,
}
