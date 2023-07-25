import httpx
import asyncio

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
    with open('PROXY.txt', 'r') as f:
        proxies = f.read().splitlines()

    # Remove duplicates
    proxies = list(set(proxies))

    with open('VALID_PROXY.txt', 'w') as f:
        for proxy in proxies:
            if await is_proxy_alive(proxy):
                print(f"Proxy {proxy} is alive!")
                f.write(proxy + "\n")

if __name__ == "__main__":
    asyncio.run(main())
