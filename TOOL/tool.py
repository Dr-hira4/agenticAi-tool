## It is a non real-time data

## from agents import Agent, Runner
## from main import config


## agent = Agent(
##    name='General Agent',
##    instructions="You are a helpful assistant. Your task is to help the user with their queries"
##)

## result = Runner.run_sync(agent,
##                         'who is the founder of Pakistan?',
##                          run_config=config)

## print(result.final_output)



## It is a real-time data

##from agents import Agent, Runner
##from main import config


##agent = Agent(
   ## name='General Agent',
  ##  instructions="You are a helpful assistant. Your task is to help the user with their queries"
##)

##result = Runner.run_sync(agent,
        ##                 'What is the conversion rate of USD to PKR?'
      ##                   'What is the weather in Islamabad'
    ##                     'what is the date today',
  ##                       run_config=config)

##print(result.final_output)


#It is a personalised data

from agents import Agent, Runner
from main import config


agent = Agent(
    name='General Agent',
    instructions="You are a helpful assistant. Your task is to help the user with their queries"
)

result = Runner.run_sync(agent,
                         'show me the top 10 students of class 9?',
                          run_config=config)

print(result.final_output)

