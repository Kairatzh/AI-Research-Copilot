# === 1. LangChain: LLM и Memory ===
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

llm = OpenAI(temperature=0.7)
memory = ConversationBufferMemory()

prompt = PromptTemplate(
    input_variables=["task"],
    template="Ты агент-писатель. Составь план по задаче: {task}"
)
langchain_chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

# === 2. LangGraph: граф workflow ===
from langgraph import Graph, Node

node1 = Node("Составить план через LangChain")
node2 = Node("Разбить план на подзадачи")
node3 = Node("Запустить агентов CrewAI")

graph = Graph(start_node=node1)
node1.add_edge(node2)
node2.add_edge(node3)

# === 3. CrewAI: мультиагенты ===
from crewai import Agent as CrewAgent, Crew

# Агент-исследователь: ищет факты
researcher = CrewAgent(
    name="Researcher",
    task="Найти факты и ссылки по каждому пункту плана",
    llm_chain=langchain_chain  # использует LangChain внутри
)

# Агент-писатель: генерирует текст на основе найденных фактов
writer = CrewAgent(
    name="Writer",
    task="Составить текст на основе фактов Researcher",
    llm_chain=langchain_chain
)

crew = Crew([researcher, writer])

# === 4. Agno: автономные агенты с инструментами ===
from agno.agent import Agent as AgnoAgent
from agno.models.together import Together
from agno.tools import Calculator

agno_agent = AgnoAgent(
    model=Together(id="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"),
    tools=[Calculator()],
    memory=None  # можно подключить memory от LangChain
)

# === 5. Комбо: запуск графа ===
def run_combo(task):
    # 1. LangGraph workflow
    context = {"task": task}
    graph.run(context)
    
    # 2. CrewAI агенты выполняют подзадачи
    crew.run(task)
    
    # 3. Agno агент решает финальные вычисления или уточнения
    agno_agent.print_response(f"Проверить и дополнить результаты по задаче: {task}")

# === 6. Пример запуска ===
run_combo("Создай план обучения LLM-разработчику")
