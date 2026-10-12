from pusher_push_notifications import PushNotifications

INSTANCE_ID = '2290f082-76c6-4712-bfca-bd71847cda6a'
SECRET_KEY = 'EB00E960F8AB025910B8CB326446C65E0CBD3E27127AFD44B91F9907078F1715'

def config_notify(title, content, icon, link):
    beams_client = PushNotifications(
        instance_id=INSTANCE_ID,
        secret_key=SECRET_KEY,
    )
    
    response = beams_client.publish_to_interests(
      interests=['Ayah'],
      publish_body={
        'web': {
          'notification': {
            'title': f'{title}',
            'body': f'{content}',
            'icon': f'{icon}',
            'deep_link': f'{link}',
          },
        },
      },
    )
    
    print(response['publishId'])
