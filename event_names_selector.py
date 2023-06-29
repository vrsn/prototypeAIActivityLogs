import boto3


def get_all_activity_log_events():
    # Connect to AWS CloudTrail using the boto3 SDK
    client = boto3.client('cloudtrail', region_name='us-east-1')

    # Retrieve all existing event names
    response = client.describe_trails()

    # Extract event names from the response
    event_names = []
    for trail in response['trailList']:
        response = client.get_event_selectors(TrailName=trail['Name'])
        for event_selector in response['EventSelectors']:
            event_names.extend(event_selector['IncludeManagementEvents'])
            event_names.extend(event_selector['ReadWriteType'])

    return event_names
