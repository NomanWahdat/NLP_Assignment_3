# NLP_Assignment_3
Assignment 3: Sentence Segmentation and Information Extraction Tasks
Task 1: Basic Sentence Segmentation
Objective: Implement a basic sentence segmentation algorithm that segments a paragraph based on common punctuation marks (e.g., periods, exclamation marks, and question marks).
Implementation:
A tkinter GUI is created where the user can input a paragraph of text. The re.split() function is used to split the text into sentences based on punctuation marks followed by a space. This segmentation technique is simple but effective for basic text segmentation.
Inputs:
•	A paragraph of text entered by the user in a text area.
Expected Outputs:
•	The segmented sentences displayed in the output area.
Example Input:
"This is the first sentence. Here is another one! Is this the third? Yes, it is."
Example Output:
"This is the first sentence."
"Here is another one!"
"Is this the third?"
"Yes, it is."
 



Task 2: Model-Based Sentence Segmentation
Objective: Implement a sentence segmentation algorithm using a pre-trained language model.
Implementation:
In this implementation, a sentiment analysis model from the Hugging Face transformers library is used (for demonstration purposes, as segmentation models require more resources). The user inputs a paragraph of text, and the text is split into sentences using a basic split by period (. ). In practice, a language model-based segmentation would involve using more advanced methods like BERT or similar models.
Inputs:
•	A paragraph of text entered by the user.
Expected Outputs:
•	Sentences segmented using a simple model-based approach (due to resource limitations).
Example Input:
"John went to the store. He bought some apples. Then, he walked home."
Example Output:
"John went to the store."
"He bought some apples."
"Then, he walked home."
 



Task 3: Domain-Specific Information Extraction
Objective: Extract domain-specific information (e.g., names, phone numbers) from a text.
Implementation:
For this task, a basic extraction of names (capitalized words followed by another capitalized word) and phone numbers (following a typical phone number pattern) is implemented using regular expressions. This task can be expanded to extract additional domain-specific information such as addresses, medical conditions, etc.
Inputs:
•	A block of text entered by the user, such as a medical report or contact information.
Expected Outputs:
•	Extracted names and phone numbers displayed in the output area.

Example Input:
"Patient Name: John Doe. Age: 45. Contact: 123-456-7890."
Example Output: 
"Names: John Doe"
"Phone Numbers: 123-456-7890"
 

 
