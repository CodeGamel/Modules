def mood_responses(user_mood):
    mood = ['Happy', 'Sad','Excited', 'Angry', 'Confused', 'Love', 'Lonely' , 'Shame']

    if user_mood in ['Happy','Excited']:
        print('I am happy to hear that!')
        
    if user_mood in ['Sad','Confused','Lonely']:
        print('I understand and hope it gets better')

    elif user_mood in ['Angry', 'Shame']:
        print('I suggest taking a walk and breathing the fresh air.')
    else:
        ('Im not sure how to respond to that.')
