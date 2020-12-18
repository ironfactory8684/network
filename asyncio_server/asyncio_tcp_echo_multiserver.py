import asyncio
async def handle_echo(reader, writer):
    while True:
        data = await reader.read(100)

        if data:
            message = data.decode()
            addr = writer.get_extra_info('peername')
            print("Received %r from %r"%(message, addr))

            print('Send: %r'%message)
            writer.write(data)
            await writer.drain()

loop = asyncio.get_event_loop()

coro =asyncio.start_server(handle_echo, '127.0.0.1', 2500, loop=loop)

server = loop.run_until_complete(coro)

print("serving on {}".format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
