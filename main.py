import time
from datetime import datetime as dt

# Path to the hosts file on macOS
HOSTS_PATH = "/etc/hosts"

# The IP address to redirect blocked sites to
REDIRECT_IP = "127.0.0.1"

# List of social media websites to block
website_list = [
    "www.facebook.com", "facebook.com",
    "www.youtube.com", "youtube.com",
    "www.reddit.com", "reddit.com",
    # Add more
]

# Hours to block
BLOCK_START_HOUR = 9   # 9:00
BLOCK_END_HOUR = 17    # 17:00

def is_work_time():
    current_hour = dt.now().hour
    return BLOCK_START_HOUR <= current_hour < BLOCK_END_HOUR

def block_websites():
    with open(HOSTS_PATH, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                continue
            file.write(f"{REDIRECT_IP} {website}\n")

def unblock_websites():
    with open(HOSTS_PATH, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            # Write only lines that do not reference the blocked websites
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()

def main():
    print("Distraction Destroyer in action")
    try:
        while True:
            if is_work_time():
                print("Blocking social media sites.")
                block_websites()
            else:
                print("Unblocking social media sites.")
                unblock_websites()
            # Wait 60 seconds before checking again
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nExiting")

if __name__ == '__main__':
    main()
