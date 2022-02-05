import asyncio
async def factorial(n: int) -> int:
    result =1
    print(f"started to calculate {n}!")
    for i in range(1,n+1):
        result *=i
        if i % 1_000 == 0:
            await asyncio.sleep(0.1)
    print(f"finished to calculate {n}!")
    return result


async def main():
    numbers = [1000000,20,300,1230]
    vals = []
    for num in numbers:
        #vals.append(factorial(num))
        vals.append(loop.create_task(factorial(num)))
    await asyncio.wait(vals)
    return vals
    #print(vals)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
