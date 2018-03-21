#
# core/utils.py - utilities for yama to use
# 
# author: superwhiskers
# license: gplv3 
#

"""
# log to the message log
def log(str_to_log):
    sanitized_str = ''.join(filter(lambda x: x in string.printable, str_to_log))
    print(sanitized_str)
    with open("output.log", "a", -1, "utf-8-sig") as output:
        output.write(str_to_log + "\n")

# return true if user is mod
def is_mod(user):
    return user.id in cfg["moderators"]


# Tag helpers
def get_tags():
    with open("tags.json", "r") as tags_file:
        return json.load(tags_file)

def get_tag(tag_name):
    tags = get_tags()
    for name, tag in tags.items():
        if name == tag_name:
            return tag

    return None

def create_tag(name, content):
    tags = get_tags()
    tags[
        name
    ] = {
        # support for future additions
        'content': content
    }
    save_tags(tags)

def delete_tag(name):
    tags = get_tags()
    del tags[name]
    save_tags(tags)

def save_tags(tags):
    with open("tags.json", "w") as tags_file:
        tags_file.seek(0)
        tags_file.write(json.dumps(tags))
        tags_file.truncate()

# returns the server the bot is in
def server():
    for x in bot.guilds:
        return x

# return a channel object by name
def channel(channel_name):
    return discord.utils.get(server().channels, name=channel_name)

# returns a role object by name
def role(role_name):
    return discord.utils.get(server().roles, name=role_name)

# returns a user object by name
def user(user_name):
    return discord.utils.get(server().members, name=user_name)

# checks if a command is at the start of a message
def command(command, msg):
    return re.match(
        "^" + cfg["prefix"] + command + "(?:\\s+|$)", msg, re.MULTILINE
    )

# checks if the specified member has a role
def hasRole(member, role):
    hasRole = False
    for x in range(0, len(member.roles)):
        if role == member.roles[x].name:
            hasRole = True
    return hasRole

def coo(channel, target_user, response):
    target_part = f"{ target_user.mention }, " if target_user is not None else ""
    return channel.send(f"Coo, { target_part }{ response }")

def log_message(message, is_edit=False, is_delet=False):
    result = f"[{ message.author.name } "
    if is_edit:
        result += "edited a message "
    if is_delet:
        result += f"had their message deleted "
    result += "in "
    if isinstance(message.channel, discord.channel.DMChannel):
        result += "a DM with me"
    else:
        result += message.channel.name
    result += f"]: { message.clean_content } [{ strftime('%m/%d/%Y %H:%M:%S', gmtime()) }]"
    log(result)
"""