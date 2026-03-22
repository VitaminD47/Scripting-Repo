import asyncio
import getpass
import telnetlib3

#this script was made by ChatGPT. It uses a more dated module and method via telnet with an older api. 
#the code provided from the author was outdated and did not work any longer because telnetlib is not used.


HOST, PORT = "7.7.7.2", 23  # change if needed

async def main():
    user = input("Username: ")
    pw = getpass.getpass("Password: ")

    # bytes mode to avoid str/bytes issues
    reader, writer = await telnetlib3.open_connection(
        HOST, PORT, encoding=None, shell=None
    )

    # --- Login (per your prompt) ---
    await reader.readuntil(b"Username:")
    writer.write(user.encode("ascii") + b"\r\n")

    await reader.readuntil(b"Password:")
    writer.write(pw.encode("ascii") + b"\r\n")

    await reader.readuntil(b"#")  # privileged prompt

    # --- Run commands & show output after each ---
    async def send(cmd: bytes):
        writer.write(cmd + b"\r\n")
        out = await reader.readuntil(b"#")
        print(out.decode("ascii"), end="")

    await send(b"terminal length 0")
    await send(b"conf t")
    await send(b"int loop 0")
    await send(b"ip address 1.1.1.1 255.255.255.255")
    await send(b"int eth0/1")
    await send(b"ip address 20.20.20.1 255.255.255.0")
    await send(b"no shut")
    await send(b"end")
    await send(b"show ip int brief")

    # --- Clean close (quiet) ---
    try:
        writer.write(b"exit\r\n")
        # drain until closed or short timeout
        while True:
            try:
                chunk = await asyncio.wait_for(reader.read(1024), timeout=0.5)
            except asyncio.TimeoutError:
                break
            if not chunk:
                break
    except (ConnectionResetError, BrokenPipeError):
        pass
    finally:
        try:
            writer.close()
            await asyncio.sleep(0.1)
        except Exception:
            pass

if __name__ == "__main__":
    asyncio.run(main())


