import time
import asyncio

async def calcular_imposto(faturamento):
    print(faturamento * 0.1)


async def calcular_bonus_funcionarios(vendas):
    for funcionario in vendas:
        venda = vendas[funcionario]
        print(funcionario, "Bonus:", venda * 0.05)
        await asyncio.sleep(1)

async def fechamento():
    vendas = {
        "lira": 1500,
        "joao": 500,
        "amanda": 5000
    }
    faturamento = 1000
    tarefa1 = asyncio.create_task(calcular_bonus_funcionarios(vendas))
    tarefa2 = asyncio.create_task(calcular_imposto(faturamento))
    await tarefa1, tarefa2
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(asyncio.gather(calcular_bonus_funcionarios(vendas), calcular_imposto(faturamento)))
    #loop.close()
    print("Finalizou")


asyncio.run(fechamento())