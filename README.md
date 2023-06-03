# graduation_project
This is a program that uses keywords to generate corresponding marketing advertisements.

SKill: PYTHON,HTML,FLASK,CHATGLM

Usage: 
First run program, click the button to view the program introduction. 
Then click the input field, double-click without input will return to the initial interface. 
Enter (marketing product) keywords and click Generate to generate corresponding product images and marketing text.


Introduction: This is a program that uses keywords to generate corresponding marketing advertisements. I use html to develop an interface, so that users have a place to enter keywords. Then use the python crawler to obtain Google images, call the story model API to generate text, and ensure that the project can be implemented. The model I use is CHATGLM, which is an open source Chinese-English bilingual language model. Its biggest advantage is that it does not require high configuration and can be deployed locally to realize the story generation function. Since I'm designing for marketers, I translate the mockup's text story into specific marketing copy for targeted design for users. Next is the implementation of the backend. I will use flask to initiate a request and return the query result as a json response, so as to render the AI model to the local interface to achieve the final interface effect.


