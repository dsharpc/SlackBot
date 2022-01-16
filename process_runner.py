import sys
import time
import random
from slack import post_start_process_to_slack, post_end_process_to_slack, post_failed_process_to_slack

def run_process(process_name: str, process_time: str):

    # Post message to slack to indicate process has started running
    post_start_process_to_slack(process_name)

    # Wait for process to execute
    for _ in range(int(process_time)):
        time.sleep(1)
        # Randomly define whether the process failed
        if random.random() < 0.1:
            # If process failed, notify Slack
            post_failed_process_to_slack(process_name)
            raise Exception("Process Failed!")
    
    # If process did not fail, notify of successful completion
    post_end_process_to_slack(process_name)

if __name__ == "__main__":
    name = sys.argv[1]
    _time = sys.argv[2]
    run_process(name, _time)