# Send TFE notification to Rocket chat channel

Deploy function:

```gcloud functions deploy notify_rocket_chat --runtime python38 --trigger-http --allow-unauthenticated```

Configure the webhook in TFE:

Follow this guide: [Documentation](https://www.terraform.io/docs/cloud/workspaces/notifications.html)
