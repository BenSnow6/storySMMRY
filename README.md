# Better tags
Team artificially intelligent

- Creating better natural language processing to create better tags for short story recommendations

- Tagging is currently done by humans and is fairly general because it has to be done quickly to tag lots of products, or current automated methods tag with general topics
- Tagging is very context dependant (may be more obvious the tags for a scientific paper than for a romance novel due to different interpretations of art)
- Found a series of short stories [here](https://blog.reedsy.com/short-stories/) 

# Project proposal

Can natural language processing be used to improve the reccomendation system for short stories?

## Project description
Curently, the reccomendation system for short stories is based on tags. These tags are created by humans and are fairly general. We want to see if we can use natural language processing to create tags that reflect the content of the story more accurately. We wish for tags to include details such as common tropes and themes. We particularly like the work of the website [doesthedogdie.com](https://doesthedogdie.com/) which lets users filter popular media for unsettling topics, such as a dog dying in a movie. We want to see if we can use similar techniques to create tags that are more specific to the content of the story.

## Project goals
- Create a corpus of short stories from the reedsy website
- Hand tag a subset of the corpus with our more specific tags
- Use natural language processing to create tags for the rest of the corpus
- Create an embedding from the tags to allow stories to be compared with one another
- Create a lightweight web app to allow a user to input a story from reedsly and get a list of similar stories based on the generated tags and similarity of the embeddings

