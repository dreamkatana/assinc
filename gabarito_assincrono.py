import asyncio
import time


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
    tarefa = asyncio.create_task(calcular_bonus_funcionarios(vendas))
    tarefa2 = asyncio.create_task(calcular_imposto(faturamento))
    print("Finalizou")
    await tarefa
    await tarefa2

asyncio.run(fechamento())