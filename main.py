import flet as ft
import ollama

# Function to generate examples and grammar explanation
def generate_examples(topic):
    prompt = f"""
    You are an English teacher. 
    For the topic '{topic}', do the following in a concise way:

    1. Give a short explanation of the grammar rule.
    2. Provide a brief formula or structure.
    3. Create 10 short English sentences illustrating the rule. Include examples in affirmative, negative, and interrogative forms.
    4. Provide the Portuguese (pt-br) translation for each sentence, except for the English words.

    ## Regra:
    - explanation in English and translation of the explanation into Portuguese (pt-br).

    ## Fórmula:
    - structure in English and translation of the structure into Portuguese (pt-br).


    ## Exemplos:
    - English sentence 1 - Portuguese (pt-br) translation.
    - English sentence 2 - Portuguese (pt-br) translation.
    ...
    """
    response = ollama.chat(model="deepseek-r1:latest", messages=[
        {"role": "system", "content": "You are an English teacher."},
        {"role": "user", "content": prompt}
    ])
    return response['message']['content']

# Define topics per level
TOPICS = {
    "A": [
        "Personal pronouns", "Interrogative sentences", "Common adjectives",
        "Auxiliary verbs", "Basic vocabulary", "Verb 'to be'",
        "Imperative mood", "Prepositions", "Possessives",
        "Quantifiers", "There to be", "Time expressions",
        "Modal verbs", "Simple present", "Present continuous",
        "Simple past", "Past continuous", "Simple future"
    ],
    "B": [
        "Adverbs", "Comparatives", "Superlatives", "Future continuous",
        "Conditionals", "Past continuous and perfect",
        "Present perfect – and difference with simple past",
        "Present perfect continuous", "Passive voice", "Predictions",
        "Reported speech", "Relative pronouns", "Wishes"
    ],
    "C": [
        "Mixed conditionals", "Narrative verb tenses", "Regrets",
        "Review of future forms", "Future continuous",
        "All forms of passive voice", "Phrasal verbs",
        "More technical vocabulary"
    ]
}

# Main Flet app
def main(page: ft.Page):
    page.title = "📘 Interactive English Learning with AI"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.window.maximized = True

    # UI elements
    level_dropdown = ft.Dropdown(
        label="📖 Escolha um nível",
        width=250,
        options=[ft.dropdown.Option(l) for l in ["A", "B", "C"]]
    )

    topic_dropdown = ft.Dropdown(
        label="📚 Escolha um tópico",
        width=250,
        options=[]
    )

    output_md = ft.Markdown(value="", selectable=True, expand=True)

    # Update topics based on level
    def on_level_change(e):
        selected_level = level_dropdown.value
        topic_dropdown.options = [ft.dropdown.Option(t) for t in TOPICS.get(selected_level, [])]
        topic_dropdown.value = None
        output_md.value = ""
        page.update()

    level_dropdown.on_change = on_level_change

    # Generate examples
    def on_generate_click(e):
        if topic_dropdown.value:
            output_md.value = "Gerando exemplos... ⏳"
            page.update()
            try:
                examples = generate_examples(topic_dropdown.value)
                output_md.value = examples
            except Exception as ex:
                output_md.value = f"Error: {ex}"
            page.update()
        else:
            output_md.value = "Por favor, selecione um tópico."
            page.update()

    generate_button = ft.ElevatedButton(
        text="Gerar Exemplos",
        on_click=on_generate_click
    )

    # Main container with centered content
    main_container = ft.Container(
        content=ft.Column(
            [
                # Header section with inputs at the top
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "Selecione um nível e um tópico para ver regras gramaticais concisas, fórmulas e exemplos (afirmativo, negativo e interrogativo) gerados pela IA (LLaMA).",
                                text_align=ft.TextAlign.CENTER,
                                size=16
                            ),
                            level_dropdown,
                            topic_dropdown,
                            generate_button,
                        ],
                        spacing=20,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.top_center,
                    padding=ft.padding.only(top=50),
                ),
                # Results section below
                ft.Container(
                    content=output_md,
                    width=800,
                    padding=20,
                    border_radius=10,
                    alignment=ft.alignment.top_center,
                ),
            ],
            spacing=30,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll="always",
            expand=True
        ),
        alignment=ft.alignment.top_center,
        expand=True
    )

    page.add(main_container)

# Run Flet desktop app
ft.app(target=main)
