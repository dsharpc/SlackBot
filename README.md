# Slack Bot :robot:

Example code for building a Slack Bot for notifications and/or reporting. See full guide in this blog post:

```
https://medium.com/p/714283fd16e5
```

## Execution

After installing the requirements.txt and setting the environmental variables for SLACK_APP_TOKEN and SLACK_APP_CHANNEL, use the following commands to run the fake tasks.

### Fake task

```bash
python process_runner.py <task_name> <task_duration>
```

Where task_duration is number of seconds.

### Send Matplotlib plot
  
``` bash
python plot_maker.py
```