# 1. *args 和 **kwargs 练习
def order_info(*dishes, **customer_info):
    print(f'顾客信息：{customer_info}')
    print(f'菜品：{','.join(dishes)}')

order_info('宫保鸡丁', '麻婆豆腐', name='张三', table=5)

# 2. 基础装饰器
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'函数{func.__name__} 执行耗时：{end - start:.2f}秒')
        return result
    return wrapper
@timer
def slow_function():
    time.sleep(0.5)
    print('任务完成')

slow_function()


import asyncio
import time
# 1. 最简单的异步函数
async def say_hello():
    print('hello')
    await asyncio.sleep(1)
    print('world')

# 运行异步函数
asyncio.run(say_hello())

# 2. 并发执行多个任务
async def fetch_data(name, delay):
    print(f'{name} 开始获取数据....')
    await asyncio.sleep(delay)
    print(f'{name} 数据获取完成')
    return f'{name}的数据'

async def main():
    # 顺序执行（慢）
    # result1 = await fetch_data('任务1', 3)
    # result2 = await fetch_data('任务2', 3)
    # result3 = await fetch_data('任务3', 3)

    # 并发执行（快）
    results = await asyncio.gather(
        fetch_data('任务1', 1),
        fetch_data('任务2', 1),
        fetch_data('任务3', 1)
    )
    print(f'所有结果：{results}')

asyncio.run(main())