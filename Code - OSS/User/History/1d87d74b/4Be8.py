import httpx
import asyncio
import re

async def download_proxies(url):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        proxies = r.text.strip().split('\n')
        # Clean proxies from non-printable characters
        proxies = [re.sub(r'[^\x20-\x7E]+', '', proxy) for proxy in proxies]
        # Format proxies if necessary (for the third repository)
        proxies = ["http://" + (proxy.split(':')[0]+':'+proxy.split(':')[1] if len(proxy.split(':'))>2 else proxy) for proxy in proxies]
        return proxies

async def is_proxy_alive(proxy):
    try:
        async with httpx.AsyncClient(proxies={"http://": proxy, "https://": proxy}, timeout=5) as client:
            r = await client.get('http://httpbin.org/ip')
            if r.status_code == 200:
                return True
    except Exception as e:
        print(f"Error with proxy {proxy}: {e}")
    return False

async def main():
    urls = [
        'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
        'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/socks5_proxies.txt',
        'https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt'
    ]

    proxies = []
    for url in urls:
        proxies += await download_proxies(url)

    # Remove duplicates
    proxies = list(set(proxies))

    with open('VALID_PROXY.txt', 'w') as f:
        for proxy in proxies:
            if await is_proxy_alive(proxy):
                print(f"Proxy {proxy} is alive!")
                f.write(proxy + "\n")

if __name__ == "__main__":
    asyncio.run(main())
