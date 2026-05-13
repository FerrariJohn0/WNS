import time
import requests
from bs4 import BeautifulSoup


HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts" 


REDIRECT_IP = "127.0.0.1"

def block_website(website): #To block website
    try:
        with open(HOSTS_PATH, "r+") as file:
            content = file.read()
            # Block website if it's not already blocked
            if website not in content:
                file.write(f"{REDIRECT_IP} {website}\n")
                print(f"[+] Blocked: {website}")
                #print(f"[+] {website} is not found in the file.")
            else:
                print(f"[!] Website '{website}' is already blocked.")
    except FileNotFoundError:
        print(f"❌ FileNotFoundError: hosts file not found at:\n   {HOSTS_PATH}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def unblock_website(website): #Unblock website
    try:
        with open(HOSTS_PATH, "r") as file:
            lines = file.readlines()
        
        with open(HOSTS_PATH, "w") as file:
            for line in lines:
                # Write back all lines that don't contain the website
                if website not in line:
                    file.write(line)
        print(f"[-] Unblocked: {website}")
    except FileNotFoundError:
        print(f"❌ FileNotFoundError: hosts file not found at:\n   {HOSTS_PATH}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def scrape_website(url):
    try:
        response = requests.get(f"http://{url}", timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text().lower()
    except requests.RequestException:
        print(f"❌ Failed to fetch website: {url}")
        return ""

def detect_patterns(text, keywords):#Detect patterns
    for keyword in keywords:
        if keyword.lower() in text:
            return True
    return False

def auto_block(url, keywords):
    print(f"\n[+] Scanning website: {url}")
    content = scrape_website(url)
    
    if detect_patterns(content, keywords):
        block_website(url)
        print(f"[AUTO] Website '{url}' blocked based on detected pattern.\n")
    else:
        print("[AUTO] No harmful pattern detected.\n")

def main():
    keywords = ["gaming", "casino", "social media", "adult", "betting"]
    
    while True:
        print("\n--- Python Website Blocker ---")
        print("1. Block Website")
        print("2. Unblock Website")
        print("3. Auto Block (Pattern Detection + Scraping)")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            site = input("Enter website (example: facebook.com): ")
            block_website(site)

        elif choice == "2":
            site = input("Enter website to unblock: ")
            unblock_website(site)

        elif choice == "3":
            site = input("Enter website to scan: ")
            auto_block(site, keywords)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()