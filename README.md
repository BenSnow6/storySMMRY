# Cohere hackathon

# Topic ideas
## Classifying song lyrics
- Generate tags by analysing song lyrics
- Use tags to to then make better informed recommendations

We tested the API locally for TLDR summarisation and it worked fine. We want to try testing with creating our own tags instead of summaries. I guess summaries and tags are fairly similar though.

Along with this, we spent some time discussing the usefulness of better tagging and the difficulties in a few areas (finding similar literature, book recommendations, product tagging) to better motivate the topic choice.

- Tagging is currently done by humans and is fairly general because it has to be done quickly to tag lots of products, or current automated methods tag with general topics
- Tagging is very context dependant (may be more obvious the tags for a scientific paper than for a romance novel due to different interpretations of art)
- Found a series of short stories [here](https://blog.reedsy.com/short-stories/) 
- 

## No code discord bots
- User enters a description of the bot that they want to create in a simple React web app (or even simpler, could be Gradio and/or Streamlit). (If it is React, it would be a bit easier to further prompt user when any classification is uncertain and/or if the bot generation requires more information from user). For example (stealing cohere's idea), the user might input "I want a bot that sends a creative affirmation message on #general channel every day at 9am ET" 
- Classifier #1: predicts the trigger event (scheduled, message detection, or arbitrary hook) which we can then map on to fairly simple Slack/Discord bot API code. In the example above, we would classify it as ("scheduled", "daily", "9am ET").
- Classifier #2: predicts the trigger location (specific channel; any channel based on message; direct message with user). In the example above, we would classify it as specific channel and extract #general 
- Classifier #3: predicts the string in input which corresponds to the type of message that bot should be generating. In the example above, it would correspond to the "creative affirmation message". Alternatively, we could just require that the user provides a few examples of the type of message they want to generate.
- Generative model: when bot is triggered, we use Cohere's generative endpoint to create a message based on classifier #3, the output of which is what our generated bot would send to Slack/Discord. 
- Business plan - the MVP could be used as a flexible team engagement tool. Beyond MVP, this could be extended in many ways to connect with arbitrary APIs and/or other slackbots (e.g. Polly) to create bots for ad-hoc needs without anyone needing to code. This could be sold as a general team engagement and productivity app for enterprises that use slack amongst different teams.

