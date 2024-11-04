import tkinter as tk
from tkinter import ttk, messagebox
import random
from ttkbootstrap import Style
from PIL import Image, ImageTk
import os  # Import os for path handling

# Expanded Data about José Rizal
rizal_data = {
    'birth': (
        "José Rizal was born on June 19, 1861, in Calamba, Laguna, Philippines. "
        "He was the seventh of eleven children born to a well-to-do family. "
        "His father, Francisco Rizal Mercado, was a prosperous farmer, and his mother, Teodora Alonso Realonda, was a well-educated woman. "
        "From a young age, Rizal showed a keen intelligence and a deep love for learning."
    ),
    'childhood': (
        "As a child, Rizal displayed remarkable intelligence and creativity. At age three, he learned the alphabet from his mother. "
        "He wrote his first poem at age eight and began his formal education at a local school at the age of six."
    ),
    'education': (
        "Rizal's education began at home, where he was taught by his mother. At the age of 11, he traveled to Manila to pursue his studies at the "
        "Ateneo Municipal de Manila, where he excelled academically. At 16, he graduated with a Bachelor of Arts degree, and at 23, he studied medicine and philosophy in Spain "
        "at the Universidad Central de Madrid, earning a degree in medicine."
    ),
    'family_life': (
        "José Rizal had a close-knit family. His mother, Teodora, was a significant influence on his life beyond formal education. "
        "The family was known for their values of education and civic duty."
    ),
    'novels': [
        {
            "title": "Noli Me Tangere",
            "description": (
                "Published in 1887, this novel is a critique of Spanish colonial rule and social injustice in the Philippines. "
                "The story revolves around Crisostomo Ibarra, a young man who returns to his homeland after studying in Europe. "
                "Through his journey, Rizal exposes the flaws of Philippine society and the oppressive regime."
            )
        },
        {
            "title": "El Filibusterismo",
            "description": (
                "Released in 1891, this sequel to Noli Me Tangere delves deeper into the struggles faced by Filipinos under Spanish rule. "
                "It follows the character of Simoun, a wealthy jeweler with a revolutionary agenda against the injustices of the government."
            )
        },
    ],
    'poetry': [
        {
            "title": "A La Patria",
            "lines": (
                "A poem expressing Rizal's love for his country, written in 1876 when he was just 15 years old. "
                "The poem reflects his deep nationalistic sentiments and desire for Filipino pride."
            )
        },
        {
            "title": "El Cuento de los Dos Hermanos",
            "lines": (
                "A fable reflecting national pride, highlighting the virtues of unity and love for one’s country. "
                "Rizal's poetry often calls for social reforms and a collective national identity."
            )
        },
    ],
    'life_events': [
        "Executed on December 30, 1896, in Bagumbayan (present-day Rizal Park, Manila) for charges of sedition.",
        "Traveled extensively across Europe and Asia, advocating for political reform.",
        "Key figure in the Philippine nationalist movement, influencing future leaders like Andres Bonifacio and Emilio Aguinaldo."
    ],
    'legacy': (
        "José Rizal's role as a reformist and advocate for Philippine independence has cemented his status as the national hero of the Philippines. "
        "His writings awakened national consciousness among Filipinos and paved the way for the Philippine Revolution against Spanish colonial rule. "
        "In 1956, the Philippine government declared June 19 as 'Rizal Day' in recognition of his contributions."
    ),
    'quotes': [
        "The youth is the hope of our future.",
        "He who does not know how to look back at where he came from will never get to his destination.",
        "There can be no tyrants where there are no slaves.",
        "Anger knows no boundaries; if it says all, it shall say nothing.",
        "Education is the great equalizer."
    ],
    'trivia': [
        "Rizal was a polymath who excelled in multiple fields such as medicine, politics, and the arts.",
        "He studied in code to evade Spanish censorship, writing his works in a hidden manner.",
        "Rizal was fluent in more than ten languages including Spanish, French, and German.",
        "He had a great interest in the sciences, including anthropology and archaeology."
    ]
}

class RizalApp:
    def __init__(self, root):
        self.style = Style(theme='flatly')
        self.root = root
        self.root.title("José Rizal Interactive App")
        self.root.geometry("900x700")
        self.root.config(bg="#f2f2f2")

        self.current_question = 0
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        # Creating tabs
        self.create_tabs()

        # Adding a quit button with enhanced design
        quit_button = ttk.Button(self.root, text="Quit", command=self.root.quit, style='danger.TButton')
        quit_button.pack(side='bottom', pady=10)

    def create_tabs(self):
        # Create each tab with additional historical context
        self.tab1 = self.create_tab('Early Life', rizal_data['birth'], self.get_image_path('early_life.jpg'), [
            ("Childhood", self.show_childhood_frame),
            ("Family Life", self.show_family_frame),
            ("Education", self.show_education_frame)
        ])
        self.tab2 = self.create_novels_tab()
        self.tab3 = self.create_poetry_tab()
        self.tab4 = self.create_events_tab()
        self.tab5 = self.create_legacy_tab()
        self.tab6 = self.create_quotes_tab()
        self.tab7 = self.create_trivia_tab()
        self.tab8 = self.create_quiz_tab()

    def create_tab(self, title, content, img_path, buttons=None):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=title)

        # Add background image
        self.set_background_image(frame, img_path)

        label = ttk.Label(frame, text=content, wraplength=700, font=("Helvetica", 12), background="#f2f2f2")
        label.pack(pady=20, padx=20)

        if buttons:
            button_frame = ttk.Frame(frame)
            button_frame.pack(pady=15)
            for btn_text, btn_command in buttons:
                button = ttk.Button(button_frame, text=btn_text, command=btn_command)
                button.pack(side='left', padx=5)

        self.main_frame = frame  # Keep a reference to the main frame
        self.current_sub_frame = None  # To keep track of the currently loaded sub-frame

        return frame

    def show_childhood_frame(self):
        self.load_sub_frame(self.create_childhood_frame())

    def show_family_frame(self):
        self.load_sub_frame(self.create_family_frame())

    def show_education_frame(self):
        self.load_sub_frame(self.create_education_frame())

    def load_sub_frame(self, new_frame):
        if self.current_sub_frame:
            self.current_sub_frame.destroy()  # Clear the previous frame
        new_frame.pack(fill='both', expand=True)  # Show the new frame
        self.current_sub_frame = new_frame  # Update current frame reference

    def create_childhood_frame(self):
        frame = ttk.Frame(self.main_frame)  # Use the main frame from the current tab
        label = ttk.Label(frame, text=rizal_data['childhood'], wraplength=700, font=("Helvetica", 12), background="#f2f2f2")
        label.pack(pady=20, padx=20)
        return frame

    def create_family_frame(self):
        frame = ttk.Frame(self.main_frame)
        label = ttk.Label(frame, text=rizal_data['family_life'], wraplength=700, font=("Helvetica", 12), background="#f2f2f2")
        label.pack(pady=20, padx=20)
        return frame

    def create_education_frame(self):
        frame = ttk.Frame(self.main_frame)
        label = ttk.Label(frame, text=rizal_data['education'], wraplength=700, font=("Helvetica", 12), background="#f2f2f2")
        label.pack(pady=20, padx=20)
        return frame

    def get_image_path(self, filename):
        """ Return the relative path to the images. Modify if the directory structure changes."""
        return os.path.join('src', filename)

    def set_background_image(self, frame, img_path):
        bg_image = Image.open(img_path)
        bg_image = bg_image.resize((900, 700), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = ttk.Label(frame, image=bg_photo)
        bg_label.image = bg_photo  # Keep a reference
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_novels_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Novels')
        self.create_list_tab(frame, rizal_data['novels'], 'title', 'description', "Novels")
        return frame

    def create_poetry_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Poetry')
        self.create_list_tab(frame, rizal_data['poetry'], 'title', 'lines', "Poetry")
        return frame

    def create_list_tab(self, frame, items, title_key, detail_key, section_name):
        self.set_background_image(frame, self.get_image_path('lifeandworksofrizal.jpg'))
        item_frame = ttk.Frame(frame)
        item_frame.pack(pady=10)

        item_listbox = tk.Listbox(item_frame, font=("Helvetica", 11), selectmode=tk.SINGLE)
        item_listbox.pack(side='left', padx=10)

        # Populate the list with titles
        for item in items:
            item_listbox.insert(tk.END, item[title_key])
        
        detail_label = ttk.Label(item_frame, text="", wraplength=400, font=("Helvetica", 12), background="#f2f2f2")
        detail_label.pack(side='left', padx=10, fill='y')

        # Bind the selection event to show the details in the label
        item_listbox.bind("<<ListboxSelect>>", lambda event: self.show_item_details(item_listbox, items, detail_key, detail_label))

    def show_item_details(self, listbox, items, detail_key, detail_label):
        selected_index = listbox.curselection()
        if selected_index:
            item = items[selected_index[0]]
            detail_label.config(text=item[detail_key])  # Set the text of detail_label to show item details
        else:
            detail_label.config(text="Please select a title to view details.")  # Default message if nothing is selected

    def create_events_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Important Events')
        self.set_background_image(frame, self.get_image_path('lifeandworksofrizal.jpg'))
        events_str = "\n".join(rizal_data['life_events'])
        label = ttk.Label(frame, text=f"Important Life Events:\n{events_str}", wraplength=700, font=("Helvetica", 12), background="#f2f2f2")
        label.pack(pady=20, padx=10)
        return frame

    def create_legacy_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Legacy')
        self.set_background_image(frame, self.get_image_path('lifeandworksofrizal.jpg'))
        label = ttk.Label(frame, text=rizal_data['legacy'], wraplength=700, font=("Helvetica", 12), background="#f2f2f2")
        label.pack(pady=20, padx=10)
        return frame

    def create_quotes_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Quotes')
        self.set_background_image(frame, self.get_image_path('lifeandworksofrizal.jpg'))
        quote_label = ttk.Label(frame, text=random.choice(rizal_data['quotes']), wraplength=700, font=("Helvetica", 12, "italic"), background="#f2f2f2")
        quote_label.pack(pady=30)
        share_button = ttk.Button(frame, text="Share Quote", command=lambda: messagebox.showinfo("Share Quote", quote_label['text']))
        share_button.pack(pady=10)
        return frame

    def create_trivia_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Trivia')
        self.set_background_image(frame, self.get_image_path('lifeandworksofrizal.jpg'))
        trivia_str = "\n".join(rizal_data['trivia'])
        label = ttk.Label(frame, text=f"Interesting Trivia:\n{trivia_str}", wraplength=700, font=("Helvetica", 12), background="#f2f2f2")
        label.pack(pady=20, padx=8)
        return frame

    def create_quiz_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Quiz')
        self.set_background_image(frame, self.get_image_path('lifeandworksofrizal.jpg'))

        self.question_label = ttk.Label(frame, text="", font=("Helvetica", 14, "bold"), background="#f2f2f2")
        self.question_label.pack(pady=20)

        self.answer_var = tk.StringVar()
        self.answer_frame = ttk.Frame(frame)
        self.answer_frame.pack(pady=10)

        self.answer_buttons = []
        for _ in range(4):
            rb = ttk.Radiobutton(self.answer_frame, text="", variable=self.answer_var, value="")
            rb.pack(anchor='w')
            self.answer_buttons.append(rb)

        self.submit_button = ttk.Button(frame, text="Submit Answer", command=self.submit_answer, style='success.TButton')
        self.submit_button.pack(pady=10)

        self.load_question()
        return frame

    def load_question(self):
        questions = self.get_questions()
        if self.current_question < len(questions):
            self.answer_var.set("")
            for rb in self.answer_buttons:
                rb.config(value="", text="")
            
            question = questions[self.current_question]
            self.question_label.config(text=question['question'])
            for i, option in enumerate(question['options']):
                self.answer_buttons[i].config(value=option, text=option)
            self.submit_button.config(state='normal')
        else:
            self.end_quiz()

    def submit_answer(self):
        questions = self.get_questions()
        if self.current_question < len(questions):
            selected_answer = self.answer_var.get()
            correct_answer = questions[self.current_question]['answer']

            # Provide feedback to the user about their answer
            if selected_answer == correct_answer:
                self.score += 1
                messagebox.showinfo("Answer", "Correct! Well done!")
            else:
                messagebox.showwarning("Answer", f"Incorrect! The correct answer is: {correct_answer}")
            
            self.submit_button.config(state='disabled')  # Disable the button after submission
            self.current_question += 1  # Move to the next question after answering
            self.root.after(1000, self.load_question)  # Wait for 1 second before loading the next question

    def end_quiz(self):
        messagebox.showinfo("Quiz Finished", f"Your score: {self.score}/{self.get_questions_count()}")
        self.current_question = 0
        self.score = 0
        self.load_question()  # Load the questions again for another attempt

    def get_questions(self):
        return [
            {
                "question": "When was José Rizal born?",
                "options": ["1861", "1871", "1881", "1891"],
                "answer": "1861"
            },
            {
                "question": "What are the titles of Rizal's famous novels?",
                "options": ["Noli Me Tangere and El Filibusterismo", "La Solidaridad", "Filipinas Dentro de Cien Años", "Mina de Oro"],
                "answer": "Noli Me Tangere and El Filibusterismo"
            },
            {
                "question": "What is Rizal's famous quote about the youth?",
                "options": [
                    "The youth is the hope of our future.",
                    "Knowledge is power.",
                    "Freedom is everything.",
                    "Education is a treasure."
                ],
                "answer": "The youth is the hope of our future."
            },
            {
                "question": "What was the name of Rizal's first novel?",
                "options": ["El Filibusterismo", "Noli Me Tangere", "La Liga Filipina", "Liwanag at Dilim"],
                "answer": "Noli Me Tangere"
            }
        ]

    def get_questions_count(self):
        return len(self.get_questions())

if __name__ == "__main__":
    root = tk.Tk()
    app = RizalApp(root)
    root.mainloop()