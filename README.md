# 📘 App Inglês Ollama Flet

Um aplicativo interativo para aprendizado de inglês desenvolvido com **Flet** e **Ollama**, que gera exemplos gramaticais personalizados usando inteligência artificial.

## ✨ Funcionalidades

- **🎯 Níveis de Aprendizado**: Sistema organizado em 3 níveis (A, B, C) com tópicos específicos
- **🤖 IA Generativa**: Utiliza Ollama com modelo DeepSeek para criar exemplos personalizados
- **📚 Tópicos Abrangentes**: Cobre desde conceitos básicos até avançados da gramática inglesa
- **🌍 Tradução Bilíngue**: Exemplos em inglês com traduções em português brasileiro
- **💻 Interface Moderna**: Interface gráfica intuitiva e responsiva com Flet
- **📱 Multiplataforma**: Funciona em Windows, macOS e Linux

## 🚀 Como Funciona

1. **Selecione o Nível**: Escolha entre os níveis A (básico), B (intermediário) ou C (avançado)
2. **Escolha o Tópico**: Selecione um tópico gramatical específico do nível escolhido
3. **Gere Exemplos**: Clique em "Gerar Exemplos" para criar conteúdo personalizado
4. **Aprenda**: Receba explicações, fórmulas e 10 exemplos práticos com traduções

## 📋 Tópicos Disponíveis

### Nível A (Básico)
- Personal pronouns, Verb 'to be', Simple present, Present continuous
- Basic vocabulary, Prepositions, Possessives, Modal verbs
- E mais 18 tópicos fundamentais

### Nível B (Intermediário)
- Adverbs, Comparatives, Superlatives, Conditionals
- Present perfect, Passive voice, Reported speech
- E mais 12 tópicos intermediários

### Nível C (Avançado)
- Mixed conditionals, Narrative verb tenses
- Phrasal verbs, Technical vocabulary
- E mais 8 tópicos avançados

## 🛠️ Tecnologias Utilizadas

- **Flet**: Framework Python para interfaces gráficas
- **Ollama**: Plataforma local para modelos de linguagem
- **DeepSeek R1**: Modelo de IA para geração de conteúdo educacional
- **Python 3.8+**: Linguagem de programação base

## 📦 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- Ollama instalado e configurado
- Modelo DeepSeek R1 baixado

### Passos de Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/eduardoml93/flet-ollama-english-PTbr.git
cd AppInglesOllamaFlet
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Configure o Ollama**
```bash
# Instale o Ollama (se ainda não tiver)
# Baixe o modelo DeepSeek R1
ollama pull deepseek-r1:latest
```

4. **Execute o aplicativo**
```bash
python main.py
```

## 🎮 Como Usar

1. **Inicie o aplicativo**: Execute `python main.py`
2. **Selecione o nível**: Escolha A, B ou C no primeiro dropdown
3. **Escolha o tópico**: Selecione um tópico específico no segundo dropdown
4. **Gere conteúdo**: Clique em "Gerar Exemplos"
5. **Aguarde**: A IA processará e gerará exemplos personalizados
6. **Estude**: Leia as regras, fórmulas e exemplos com traduções

## 🔧 Estrutura do Projeto

```
AppInglesOllamaFlet/
├── main.py              # Arquivo principal da aplicação
├── requirements.txt     # Dependências Python
├── assets/             # Recursos visuais
│   └── icon_windows.png
└── README.md           # Este arquivo
```

## 📝 Exemplo de Saída

O aplicativo gera conteúdo estruturado incluindo:

- **Regra**: Explicação da regra gramatical em inglês e português
- **Fórmula**: Estrutura gramatical com tradução
- **Exemplos**: 10 frases em inglês com traduções em português brasileiro


---

**⭐ Se este projeto te ajudou, considere dar uma estrela no GitHub!**
