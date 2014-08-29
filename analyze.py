from phapi import ProductHuntApi
import settings
import json

pha = ProductHuntApi(settings.DEVELOPER_TOKEN)

posts = pha.get_posts()

print json.dumps(posts, indent=2)